import json
from pathlib import Path

from ..model import (
    CatalogProvenance,
    CatalogSource,
    PackageAlias,
    PackageCandidate,
    PackageFile,
    PackageIdentity,
    PackageRecord,
    PackageResolution,
    PortClassification,
    PortDecision,
    ReasonCode,
    RecordDisposition,
    SourceFamily,
)
from ..resolver import ResolutionResult, ResolvedPayload
from ..runner import (
    CheckerExecution,
    CheckerStatus,
    ExistingCheckerBackend,
    QACase,
    QARunner,
    StubSelection,
    StubSource,
    UnknownPortPolicy,
    UvStubProvisioner,
    WorkspaceRetention,
    plan_qa_matrix,
)


class InspectingChecker:
    def __init__(self, *, fail: bool = False, message: str = "fixture diagnostic") -> None:
        self.fail = fail
        self.message = message
        self.workspaces: list[Path] = []

    def run(self, workspace: Path, *, checker: str, version: str, portboard: str) -> CheckerExecution:
        _ = version, portboard
        self.workspaces.append(workspace)
        assert (workspace / "source" / "driver.py").is_file()
        assert not (workspace / "source" / "native.mpy").exists()
        assert (workspace / "typings" / "machine.pyi").is_file()
        config = (workspace / "pyproject.toml").read_text(encoding="utf-8")
        assert 'include = ["source"]' in config
        assert 'exclude = [".*", "__*", "**/typings"]' in config
        diagnostic = {
            "file": str(workspace / "source" / "driver.py"),
            "severity": "error" if self.fail else "information",
            "message": self.message,
            "range": {"start": {"line": 0, "character": 0}, "end": {"line": 0, "character": 1}},
        }
        return CheckerExecution(
            command=(checker, "check", "."),
            diagnostics=(diagnostic,),
            summary={"filesAnalyzed": 1},
        )


def _resolution(classification: PortDecision, source: bytes = b"raise RuntimeError('must not execute')\n") -> ResolutionResult:
    identity = PackageIdentity.repository("github", "example", "driver")
    candidate = PackageCandidate(
        identity=identity,
        display_name="driver",
        source_family=SourceFamily.MIP,
        install_reference="github:example/driver",
        aliases=(PackageAlias(CatalogSource.DIRECT, "github:example/driver"),),
        provenance=(
            CatalogProvenance(
                CatalogSource.DIRECT,
                "github:example/driver",
                identity.key,
                metadata=(("author", "Fixture Author"), ("api_key", "metadata-secret")),
            ),
        ),
    )
    python_file = PackageFile(identity, "driver.py", "https://fixtures.invalid/driver.py", sha256="a" * 64, size=len(source))
    mpy_file = PackageFile(identity, "native.mpy", "https://fixtures.invalid/native.mpy", sha256="b" * 64, size=3)
    package_resolution = PackageResolution(
        requested_reference=candidate.install_reference,
        canonical_reference=candidate.install_reference,
        requested_revision="v1",
        resolved_revision="abc123",
        manifest_reference="https://fixtures.invalid/package.json",
        manifest_sha256="c" * 64,
        dependencies=(),
        files=(python_file, mpy_file),
        package_version="2.0",
    )
    record = PackageRecord(
        candidate=candidate,
        resolution=package_resolution,
        classification=classification,
        disposition=RecordDisposition.CHECK,
    )
    return ResolutionResult(
        record,
        (
            ResolvedPayload(python_file, source),
            ResolvedPayload(mpy_file, b"MPY"),
        ),
    )


def _portable() -> PortDecision:
    return PortDecision(PortClassification.PORTABLE, (), (), ())


def _stub_fixture(tmp_path: Path) -> Path:
    path = tmp_path / "stub-fixture"
    path.mkdir()
    (path / "machine.pyi").write_text("class Pin: ...\n", encoding="utf-8")
    return path


def _runner(tmp_path: Path, checker: InspectingChecker) -> QARunner:
    return QARunner(
        workspace_root=tmp_path / "runs",
        config_root=Path(__file__).parents[2] / "_configs",
        stub_provisioner=UvStubProvisioner(Path(__file__).parents[4]),
        checker_backend=checker,
    )


def test_matrix_portable_uses_all_requested_ports_deterministically(tmp_path: Path):
    plan = plan_qa_matrix(
        _resolution(_portable()).record,
        versions=["v1.28.0"],
        available_portboards=["stm32", "rp2-rpi_pico"],
        stub_source=StubSource.PATH,
        stub_path=_stub_fixture(tmp_path),
        checkers=["pyright"],
    )

    assert plan.disposition is RecordDisposition.CHECK
    assert [case.stubs.portboard for case in plan.cases] == ["rp2-rpi_pico", "stm32"]


def test_matrix_port_specific_filters_ports_and_boards(tmp_path: Path):
    classification = PortDecision(PortClassification.PORT_SPECIFIC, ("esp32",), ("rpi_pico",), ())

    plan = plan_qa_matrix(
        _resolution(classification).record,
        versions=["v1.28.0"],
        available_portboards=["stm32", "esp32-generic", "rp2-rpi_pico"],
        stub_source=StubSource.PATH,
        stub_path=_stub_fixture(tmp_path),
        checkers=["pyright"],
    )

    assert [case.stubs.portboard for case in plan.cases] == ["esp32-generic", "rp2-rpi_pico"]


def test_matrix_unknown_requires_explicit_policy(tmp_path: Path):
    unknown = PortDecision(PortClassification.UNKNOWN, (), (), (), ReasonCode.NO_PORT_EVIDENCE)
    arguments = {
        "versions": ["v1.28.0"],
        "available_portboards": ["rp2"],
        "stub_source": StubSource.PATH,
        "stub_path": _stub_fixture(tmp_path),
        "checkers": ["pyright"],
    }

    skipped = plan_qa_matrix(_resolution(unknown).record, **arguments)
    explicit = plan_qa_matrix(_resolution(unknown).record, unknown_policy=UnknownPortPolicy.USE_REQUESTED, **arguments)

    assert skipped.disposition is RecordDisposition.SKIP
    assert skipped.reason is ReasonCode.NO_PORT_EVIDENCE
    assert [case.stubs.portboard for case in explicit.cases] == ["rp2"]


def test_matrix_skips_when_no_requested_port_is_compatible(tmp_path: Path):
    classification = PortDecision(PortClassification.PORT_SPECIFIC, ("esp32",), (), ())

    plan = plan_qa_matrix(
        _resolution(classification).record,
        versions=["v1.28.0"],
        available_portboards=["rp2-rpi_pico"],
        stub_source=StubSource.PATH,
        stub_path=_stub_fixture(tmp_path),
        checkers=["pyright"],
    )

    assert plan.disposition is RecordDisposition.SKIP
    assert plan.reason is ReasonCode.NO_COMPATIBLE_PORT
    assert plan.cases == ()


def test_runner_isolates_source_and_stubs_without_executing_package(tmp_path: Path):
    checker = InspectingChecker()
    runner = _runner(tmp_path, checker)
    case = QACase(StubSelection("v1.28.0", "rp2", StubSource.PATH, _stub_fixture(tmp_path)), ("pyright",))

    report = runner.run(_resolution(_portable()), case)

    assert report.status is CheckerStatus.PASS
    assert report.retained_workspace is None
    assert not checker.workspaces[0].exists()
    data = json.loads(report.to_json())
    assert data["schema_version"] == 2
    assert data["package_identity"] == "repository:github:example/driver"
    assert data["resolved_revision"] == "abc123"
    assert data["package_version"] == "2.0"
    assert data["provenance"][0]["metadata"] == {
        "api_key": "<redacted>",
        "author": "Fixture Author",
    }
    assert data["resolution"]["manifest"]["sha256"] == "c" * 64
    assert data["resolution"]["files"][0]["target"] == "driver.py"
    assert data["resolution"]["files"][1]["kind"] == "mpy"
    assert data["typings"] == {
        "command": ["copy", "<path>", "<path>"],
        "portboard": "rp2",
        "source": "path",
        "status": "completed",
        "version": "v1.28.0",
    }
    assert data["workspace_retained"] is False
    assert data["retained_workspace"] is None
    assert data["results"][0]["command"] == ["pyright", "check", "."]
    assert "pyright: PASS" in report.render_text()
    assert "typings: path completed" in report.render_text()
    assert "command: copy <path> <path>" in report.render_text()
    assert "command: pyright check ." in report.render_text()


def test_runner_retains_failed_workspace_for_debugging(tmp_path: Path):
    checker = InspectingChecker(fail=True)
    runner = _runner(tmp_path, checker)
    case = QACase(StubSelection("v1.28.0", "rp2", StubSource.PATH, _stub_fixture(tmp_path)), ("pyright",))

    report = runner.run(_resolution(_portable()), case, retention=WorkspaceRetention.ON_FAILURE)

    assert report.status is CheckerStatus.FAIL
    retained_workspace = report.retained_workspace
    assert retained_workspace is not None
    assert retained_workspace == checker.workspaces[0]
    assert retained_workspace.is_dir()
    assert report.results[0].diagnostics[0]["file"] == "source/driver.py"
    data = json.loads(report.to_json())
    assert data["retained_workspace"] == str(retained_workspace)
    rendered = report.render_text()
    assert f"workspace retained: {retained_workspace}" in rendered
    assert "diagnostic: source/driver.py:1:1: error: fixture diagnostic" in rendered


def test_failed_diagnostics_redact_credentials_while_preserving_retained_workspace(tmp_path: Path):
    checker = InspectingChecker(
        fail=True,
        message="request failed: token=diagnostic-secret https://user:password@fixtures.invalid/source.py",
    )
    runner = _runner(tmp_path, checker)
    case = QACase(StubSelection("v1.28.0", "rp2", StubSource.PATH, _stub_fixture(tmp_path)), ("pyright",))

    report = runner.run(_resolution(_portable()), case, retention=WorkspaceRetention.ON_FAILURE)

    retained_workspace = report.retained_workspace
    assert retained_workspace is not None
    assert json.loads(report.to_json())["retained_workspace"] == str(retained_workspace)
    assert str(retained_workspace) in report.render_text()
    for rendered in (report.to_json(), report.render_text()):
        assert "diagnostic-secret" not in rendered
        assert "password" not in rendered
        assert "token=<redacted>" in rendered


def test_runner_skips_uncheckable_resolution_without_workspace(tmp_path: Path):
    resolution = _resolution(_portable())
    skipped_record = PackageRecord(
        candidate=resolution.record.candidate,
        classification=resolution.record.classification,
        disposition=RecordDisposition.SKIP,
        reason=ReasonCode.MPY_ONLY,
    )
    checker = InspectingChecker()
    case = QACase(StubSelection("v1.28.0", "rp2", StubSource.PATH, _stub_fixture(tmp_path)), ("pyright",))

    report = _runner(tmp_path, checker).run(ResolutionResult(skipped_record), case)

    assert report.status is CheckerStatus.SKIP
    assert report.results[0].message == "mpy_only"
    assert checker.workspaces == []


def test_runner_reports_provisioning_errors_and_retains_workspace(tmp_path: Path):
    checker = InspectingChecker()
    runner = _runner(tmp_path, checker)
    missing_stubs = tmp_path / "missing-stubs"
    case = QACase(StubSelection("v1.28.0", "rp2", StubSource.PATH, missing_stubs), ("pyright",))

    report = runner.run(_resolution(_portable()), case, retention=WorkspaceRetention.ON_FAILURE)

    assert report.status is CheckerStatus.ERROR
    assert str(missing_stubs.resolve()) in report.results[0].message
    assert "Stub path does not exist: <path>" in report.render_text()
    retained_workspace = report.retained_workspace
    assert retained_workspace is not None
    assert (retained_workspace / "source" / "driver.py").is_file()
    assert checker.workspaces == []
    data = json.loads(report.to_json())
    assert data["retained_workspace"] == str(retained_workspace)
    assert f"workspace retained: {retained_workspace}" in report.render_text()
    for rendered in (report.to_json(), report.render_text()):
        assert str(missing_stubs.resolve()) not in rendered
        assert "<path>" in rendered


def test_runner_executes_existing_pyright_with_local_stubs(tmp_path: Path):
    project_root = Path(__file__).parents[4]
    runner = QARunner(
        workspace_root=tmp_path / "runs",
        config_root=Path(__file__).parents[2] / "_configs",
        stub_provisioner=UvStubProvisioner(project_root),
        checker_backend=ExistingCheckerBackend(),
    )
    case = QACase(
        StubSelection(
            "v1.28.0",
            "stdlib",
            StubSource.PATH,
            project_root / "publish" / "micropython-stdlib-stubs",
        ),
        ("pyright",),
    )
    source = b"import sys\nvalue: str = sys.platform\nif False:\n    raise RuntimeError('must not execute')\n"

    report = runner.run(_resolution(_portable(), source), case)

    assert report.status is CheckerStatus.PASS, report.to_json()
    assert report.results[0].files_analyzed == 1
    assert report.results[0].diagnostics == ()
    assert report.retained_workspace is None
