import json
from io import StringIO
from pathlib import Path
from typing import Mapping

import pytest
from rich.console import Console

from ..catalog import CatalogDiagnostic, CatalogInventory
from ..catalog_loader import (
    AWESOME_CATALOG_URL,
    MIM_SITEMAP_URL,
    CatalogLoadOptions,
    NetworkCatalogLoader,
    RateLimitedFetcher,
)
from ..cli import CliRuntime, _build_runtime, build_parser, main
from ..model import (
    CatalogProvenance,
    CatalogSource,
    ClassificationOverride,
    DependencyDisposition,
    DependencyEdge,
    PackageAlias,
    PackageCandidate,
    PackageIdentity,
    PackageFile,
    PackageRecord,
    PackageResolution,
    PortClassification,
    PortDecision,
    ReasonCode,
    RecordDisposition,
    SourceFamily,
)
from ..orchestrator import (
    BatchSelection,
    CatalogSelection,
    EcosystemOrchestrator,
    OrchestrationExit,
    OrchestrationReport,
    PackageOutcome,
    QARequest,
    select_inventory_records,
)
from ..progress import NullProgressReporter, RichProgressReporter
from ..resolver import CacheMode, FetchResponse, ResolutionResult, ResolvedPayload, ResolverError
from ..runner import (
    CheckerStatus,
    QACase,
    QACheckerResult,
    QARunReport,
    StubSource,
    UnknownPortPolicy,
    WorkspaceRetention,
)


def _record(
    name: str,
    catalog: CatalogSource,
    classification: PortClassification,
    *,
    ports: tuple[str, ...] = (),
    boards: tuple[str, ...] = (),
) -> PackageRecord:
    identity = PackageIdentity.repository("github", "example", name)
    install_reference = f"github:example/{name}"
    candidate = PackageCandidate(
        identity=identity,
        display_name=name,
        source_family=SourceFamily.MIP,
        install_reference=install_reference,
        aliases=(PackageAlias(catalog, install_reference),),
        provenance=(CatalogProvenance(catalog, f"https://catalog.invalid/{name}", identity.key),),
    )
    reason = ReasonCode.NO_PORT_EVIDENCE if classification is PortClassification.UNKNOWN else None
    decision = PortDecision(classification, ports, boards, (), reason)
    return PackageRecord(candidate=candidate, classification=decision)


def _inventory() -> CatalogInventory:
    return CatalogInventory(
        (
            _record("z-portable", CatalogSource.AWESOME_MICROPYTHON, PortClassification.PORTABLE),
            _record("a-esp32", CatalogSource.MIM, PortClassification.PORT_SPECIFIC, ports=("esp32",)),
            _record("m-pico", CatalogSource.MIM, PortClassification.PORT_SPECIFIC, boards=("rpi_pico",)),
            _record("n-unknown", CatalogSource.AWESOME_MICROPYTHON, PortClassification.UNKNOWN),
        ),
        (),
    )


def test_batch_selection_combines_catalog_package_classification_and_limit_filters():
    selected = select_inventory_records(
        _inventory(),
        BatchSelection(
            catalogs=CatalogSelection.MIM,
            package_query="github:example/",
            classification=PortClassification.PORT_SPECIFIC,
            limit=1,
        ),
    )

    assert [record.candidate.display_name for record in selected] == ["a-esp32"]


def test_batch_port_filter_includes_portable_and_matching_specific_packages():
    selected = select_inventory_records(_inventory(), BatchSelection(port="rp2-rpi_pico"))

    assert [record.candidate.display_name for record in selected] == ["m-pico", "z-portable"]


def test_batch_selection_rejects_invalid_limits_and_empty_filters():
    with pytest.raises(ValueError, match="limit"):
        BatchSelection(limit=0)
    with pytest.raises(ValueError, match="package query"):
        BatchSelection(package_query=" ")
    with pytest.raises(ValueError, match="port filter"):
        BatchSelection(port="")


class FakeResolver:
    def __init__(self) -> None:
        self.focused_references: list[str] = []
        self.candidates: list[str] = []

    def resolve_reference(self, reference: str, *, mode: CacheMode = CacheMode.USE_CACHE) -> ResolutionResult:
        _ = mode
        self.focused_references.append(reference)
        return _resolved(_record("focused", CatalogSource.DIRECT, PortClassification.UNKNOWN))

    def resolve_candidate(
        self,
        candidate: PackageCandidate,
        *,
        classification: PortDecision | None = None,
        mode: CacheMode = CacheMode.USE_CACHE,
    ) -> ResolutionResult:
        _ = mode
        self.candidates.append(candidate.display_name)
        if candidate.display_name == "a-esp32":
            return ResolutionResult(
                PackageRecord(
                    candidate=candidate,
                    classification=classification,
                    disposition=RecordDisposition.ERROR,
                    reason=ReasonCode.UNAVAILABLE,
                )
            )
        record = PackageRecord(candidate=candidate, classification=classification)
        return _resolved(record)


class FakeRunner:
    def __init__(
        self,
        failing: set[str] | None = None,
        skipped: set[str] | None = None,
        retained_workspace: Path | None = None,
    ) -> None:
        self.failing = failing or set()
        self.skipped = skipped or set()
        self.retained_workspace = retained_workspace
        self.identities: list[str] = []

    def run(
        self,
        resolution: ResolutionResult,
        case: QACase,
        *,
        retention: WorkspaceRetention = WorkspaceRetention.NEVER,
    ) -> QARunReport:
        _ = retention
        identity = resolution.record.candidate.identity.key
        self.identities.append(identity)
        failed = resolution.record.candidate.display_name in self.failing
        skipped = resolution.record.candidate.display_name in self.skipped
        checker_result = QACheckerResult(
            checker=case.checkers[0],
            command=(case.checkers[0], "check"),
            status=CheckerStatus.SKIP if skipped else CheckerStatus.FAIL if failed else CheckerStatus.PASS,
            diagnostics=(),
            error_count=1 if failed else 0,
            warning_count=0,
            files_analyzed=1,
            duration_seconds=0.01,
        )
        return QARunReport(
            package_identity=identity,
            provenance=(),
            requested_reference=resolution.record.candidate.install_reference,
            resolved_revision="fixture",
            version=case.stubs.version,
            portboard=case.stubs.portboard,
            stub_source=case.stubs.source,
            stub_command=("fixture",),
            results=(checker_result,),
            duration_seconds=0.01,
            retained_workspace=self.retained_workspace if failed else None,
        )


def _resolved(record: PackageRecord) -> ResolutionResult:
    source = b"value = 1\n"
    package_file = PackageFile(
        record.candidate.identity,
        "driver.py",
        "https://fixtures.invalid/driver.py",
        sha256="a" * 64,
        size=len(source),
    )
    resolution = PackageResolution(
        requested_reference=record.candidate.install_reference,
        canonical_reference=record.candidate.install_reference,
        requested_revision=None,
        resolved_revision="fixture",
        manifest_reference="https://fixtures.invalid/package.json",
        manifest_sha256="b" * 64,
        dependencies=(
            DependencyEdge(
                requested_reference="package:fixture-dependency",
                requested_revision="1.0",
                depth=1,
                disposition=DependencyDisposition.RESOLVED,
                identity=PackageIdentity.index("fixture-dependency"),
                resolved_revision="d" * 40,
            ),
        ),
        files=(package_file,),
        package_version="1.0",
    )
    resolved_record = PackageRecord(
        candidate=record.candidate,
        resolution=resolution,
        classification=record.classification,
        disposition=RecordDisposition.CHECK,
    )
    return ResolutionResult(resolved_record, (ResolvedPayload(package_file, source),))


def _request(*, unknown_policy: UnknownPortPolicy = UnknownPortPolicy.SKIP) -> QARequest:
    return QARequest(
        versions=("v1.28.0",),
        portboards=("esp32",),
        stub_source=StubSource.PATH,
        stub_path=Path(__file__).parent,
        checkers=("pyright",),
        unknown_policy=unknown_policy,
    )


def test_qa_request_uses_requested_ports_for_unknown_packages_by_default():
    request = QARequest(
        versions=("v1.28.0",),
        portboards=("esp32-esp32_generic",),
        stub_source=StubSource.PATH,
        stub_path=Path(__file__).parent,
        checkers=("pyright",),
    )

    assert request.unknown_policy is UnknownPortPolicy.USE_REQUESTED


def test_batch_orchestration_isolates_unavailable_and_type_failures():
    resolver = FakeResolver()
    runner = FakeRunner(failing={"z-portable"})

    report = EcosystemOrchestrator(resolver, runner).run_batch(_inventory(), BatchSelection(), _request())

    outcomes = {result.package_identity: result.outcome for result in report.results}
    assert outcomes["repository:github:example/a-esp32"] is PackageOutcome.UNAVAILABLE
    assert outcomes["repository:github:example/n-unknown"] is PackageOutcome.SKIPPED
    assert outcomes["repository:github:example/z-portable"] is PackageOutcome.TYPE_CHECK_FAILURE
    assert "repository:github:example/z-portable" in runner.identities
    assert report.exit_code is OrchestrationExit.OPERATIONAL_FAILURE
    assert report.counts["unavailable"] == 1
    assert '"exit_code": 2' in report.to_json()
    document = json.loads(report.to_json())
    unavailable = next(result for result in document["results"] if result["outcome"] == "unavailable")
    assert unavailable["resolution"] is None
    assert unavailable["stages"] == {
        "checker_execution": "not_run",
        "resolution": "not_available",
        "typings_provisioning": "not_run",
    }


def test_orchestration_reports_batch_and_focused_package_progress():
    batch_progress = RecordingProgressReporter()
    batch = EcosystemOrchestrator(FakeResolver(), FakeRunner(), progress=batch_progress)

    batch.run_batch(_inventory(), BatchSelection(), _request())

    selected = [record.candidate.identity.key for record in select_inventory_records(_inventory(), BatchSelection())]
    assert batch_progress.events[0] == ("testing_started", len(selected))
    assert [value for event, value in batch_progress.events if event == "package_started"] == selected
    assert [value for event, value in batch_progress.events if event == "package_finished"] == selected
    assert batch_progress.events[-1] == ("testing_finished", None)

    focused_progress = RecordingProgressReporter()
    reference = "github:howmanyoliversarethere/micropython-joystick-2-unit"

    EcosystemOrchestrator(FakeResolver(), FakeRunner(), progress=focused_progress).run_focused(reference, _request())

    assert focused_progress.events == [
        ("testing_started", 1),
        ("package_started", reference),
        ("package_finished", reference),
        ("testing_finished", None),
    ]


def test_orchestration_exit_codes_distinguish_type_failures_and_intentional_skips():
    orchestrator = EcosystemOrchestrator(FakeResolver(), FakeRunner(failing={"z-portable"}))

    type_failure = orchestrator.run_batch(_inventory(), BatchSelection(package_query="z-portable"), _request())
    skipped = orchestrator.run_batch(_inventory(), BatchSelection(package_query="n-unknown"), _request())

    assert type_failure.exit_code is OrchestrationExit.TYPE_CHECK_FAILURE
    assert skipped.exit_code is OrchestrationExit.SUCCESS
    assert skipped.results[0].outcome is PackageOutcome.SKIPPED
    skipped_result = json.loads(skipped.to_json())["results"][0]
    assert skipped_result["stages"] == {
        "checker_execution": "not_run",
        "resolution": "completed",
        "typings_provisioning": "not_run",
    }
    assert "typings_provisioning=not_run" in skipped.render_text()


def test_orchestration_preserves_intentionally_retained_workspace(tmp_path: Path):
    retained_workspace = tmp_path / "runs" / "failed-package"
    retained_workspace.mkdir(parents=True)
    runner = FakeRunner(failing={"z-portable"}, retained_workspace=retained_workspace)

    report = EcosystemOrchestrator(FakeResolver(), runner).run_batch(
        _inventory(),
        BatchSelection(package_query="z-portable"),
        _request(),
    )

    run = json.loads(report.to_json())["results"][0]["reports"][0]
    assert run["retained_workspace"] == str(retained_workspace)
    assert f"workspace retained: {retained_workspace}" in report.render_text()


def test_all_skipped_checker_results_report_checker_stage_not_run():
    report = EcosystemOrchestrator(FakeResolver(), FakeRunner(skipped={"z-portable"})).run_batch(
        _inventory(),
        BatchSelection(package_query="z-portable"),
        _request(),
    )

    result = json.loads(report.to_json())["results"][0]
    assert result["outcome"] == "skipped"
    assert result["stages"] == {
        "checker_execution": "not_run",
        "resolution": "completed",
        "typings_provisioning": "completed",
    }


def test_catalog_diagnostics_make_partial_batch_operationally_incomplete():
    diagnostic = CatalogDiagnostic(
        catalog=CatalogSource.MIM,
        entry_key="missing-package",
        source_url="https://checkmim.com/packages/missing-package",
        disposition=RecordDisposition.ERROR,
        reason=ReasonCode.UNAVAILABLE,
        detail="fixture unavailable",
    )
    inventory = CatalogInventory((_record("z-portable", CatalogSource.MIM, PortClassification.PORTABLE),), (diagnostic,))

    report = EcosystemOrchestrator(FakeResolver(), FakeRunner()).run_batch(inventory, BatchSelection(), _request())

    assert report.results[0].outcome is PackageOutcome.PASS
    assert report.exit_code is OrchestrationExit.OPERATIONAL_FAILURE
    assert "mim:missing-package: error [unavailable]" in report.render_text()


def test_skipped_catalog_diagnostics_do_not_fail_successful_batch():
    diagnostic = CatalogDiagnostic(
        catalog=CatalogSource.MIM,
        entry_key="retired-package",
        source_url="https://checkmim.com/packages/retired-package",
        disposition=RecordDisposition.SKIP,
        reason=ReasonCode.DEPRECATED_PACKAGE,
        detail="fixture package is deprecated",
    )
    inventory = CatalogInventory((_record("z-portable", CatalogSource.MIM, PortClassification.PORTABLE),), (diagnostic,))

    report = EcosystemOrchestrator(FakeResolver(), FakeRunner()).run_batch(inventory, BatchSelection(), _request())

    assert report.results[0].outcome is PackageOutcome.PASS
    assert report.exit_code is OrchestrationExit.SUCCESS
    assert "mim:retired-package: skip [deprecated_package]" in report.render_text()


def test_focused_orchestration_bypasses_catalog_and_uses_explicit_unknown_policy():
    resolver = FakeResolver()
    runner = FakeRunner()
    reference = "github:howmanyoliversarethere/micropython-joystick-2-unit"

    report = EcosystemOrchestrator(resolver, runner).run_focused(
        reference,
        _request(unknown_policy=UnknownPortPolicy.USE_REQUESTED),
    )

    assert resolver.focused_references == [reference]
    assert report.results[0].outcome is PackageOutcome.PASS
    assert report.exit_code is OrchestrationExit.SUCCESS
    assert "focused" in report.render_text()
    document = json.loads(report.to_json())
    assert document["schema_version"] == 2
    assert document["discovery"]["requested_package"] == reference
    assert document["discovery"]["selected_packages"] == ["repository:github:example/focused"]
    assert document["cache_mode"] == "use_cache"
    assert document["qa_matrix"] == {
        "checkers": ["pyright"],
        "portboards": ["esp32"],
        "stub_path_configured": True,
        "stub_source": "path",
        "versions": ["v1.28.0"],
    }
    resolution = document["results"][0]["resolution"]
    assert resolution["resolved_revision"] == "fixture"
    assert resolution["package_version"] == "1.0"
    assert resolution["manifest"] == {
        "reference": "https://fixtures.invalid/package.json",
        "sha256": "b" * 64,
    }
    assert resolution["dependencies"] == [
        {
            "depth": 1,
            "disposition": "resolved",
            "identity": "index:fixture-dependency",
            "reason": None,
            "requested_reference": "package:fixture-dependency",
            "requested_revision": "1.0",
            "resolved_revision": "d" * 40,
        }
    ]
    assert resolution["files"][0] == {
        "dependency_depth": 0,
        "kind": "py",
        "owner": "repository:github:example/focused",
        "sha256": "a" * 64,
        "size": 10,
        "source": "https://fixtures.invalid/driver.py",
        "target": "driver.py",
    }
    assert "closure: 1 dependencies, 1 files" in report.render_text()
    assert "dependency[1]: package:fixture-dependency" in report.render_text()


def test_reports_redact_discovery_credentials_and_sensitive_query_values():
    reference = "https://report-user:report-password@example.invalid/package.json?token=report-token&ref=main"

    report = EcosystemOrchestrator(FakeResolver(), FakeRunner()).run_focused(
        reference,
        _request(unknown_policy=UnknownPortPolicy.USE_REQUESTED),
    )

    for rendered in (report.to_json(), report.render_text()):
        assert "report-user" not in rendered
        assert "report-password" not in rendered
        assert "report-token" not in rendered
        assert "ref=main" in rendered


def test_offline_report_records_cache_mode_and_complete_run_configuration():
    request = QARequest(
        versions=("v1.28.0",),
        portboards=("rp2-rpi_pico",),
        stub_source=StubSource.PYPI_PRE,
        checkers=("pyright", "mypy"),
        cache_mode=CacheMode.OFFLINE,
        unknown_policy=UnknownPortPolicy.USE_REQUESTED,
        retention=WorkspaceRetention.ON_FAILURE,
        no_stub_cache=True,
    )

    report = EcosystemOrchestrator(FakeResolver(), FakeRunner()).run_focused("github:example/offline", request)

    document = json.loads(report.to_json())
    assert document["cache_mode"] == "offline"
    assert document["configuration"] == {
        "cache_mode": "offline",
        "stub_cache_enabled": False,
        "unknown_port_policy": "use_requested",
        "workspace_retention": "on_failure",
    }
    assert document["qa_matrix"]["checkers"] == ["pyright", "mypy"]
    assert "cache: offline" in report.render_text()
    assert '"workspace_retention": "on_failure"' in report.render_text()
    assert "typings: pypi-pre completed" in report.render_text()


class FixtureCatalogFetcher:
    def __init__(self, responses: dict[str, bytes]) -> None:
        self.responses = responses
        self.calls: list[tuple[str, CacheMode]] = []

    def fetch(self, reference: str, mode: CacheMode = CacheMode.USE_CACHE) -> FetchResponse:
        self.calls.append((reference, mode))
        try:
            data = self.responses[reference]
        except KeyError as error:
            raise ResolverError(ReasonCode.UNAVAILABLE, f"fixture unavailable: {reference}") from error
        return FetchResponse(data, reference)


class RecordingProgressReporter(NullProgressReporter):
    def __init__(self) -> None:
        self.events: list[tuple[str, object]] = []

    def start_catalog(self, catalog: str) -> None:
        self.events.append(("catalog_started", catalog))

    def set_catalog_total(self, total: int) -> None:
        self.events.append(("catalog_total", total))

    def advance_catalog(self, item: str) -> None:
        self.events.append(("catalog_advanced", item))

    def finish_catalog(self) -> None:
        self.events.append(("catalog_finished", None))

    def start_testing(self, total: int) -> None:
        self.events.append(("testing_started", total))

    def start_package(self, package: str) -> None:
        self.events.append(("package_started", package))

    def finish_package(self, package: str) -> None:
        self.events.append(("package_finished", package))

    def finish_testing(self) -> None:
        self.events.append(("testing_finished", None))


def _catalog_responses() -> dict[str, bytes]:
    fixtures = Path(__file__).parent.parent / "fixtures"
    joystick_page = "https://checkmim.com/packages/howmanyoliversarethere+micropython-joystick-2-unit"
    official_page = "https://checkmim.com/packages/ntptime"
    return {
        AWESOME_CATALOG_URL: (fixtures / "awesome" / "readme.md.txt").read_bytes(),
        MIM_SITEMAP_URL: (fixtures / "mim" / "sitemap.xml").read_bytes(),
        joystick_page: (fixtures / "mim" / "community-package.html").read_bytes(),
        official_page: (fixtures / "mim" / "official-package.html").read_bytes(),
    }


def test_catalog_loader_combines_sources_deduplicates_and_forwards_refresh():
    fetcher = FixtureCatalogFetcher(_catalog_responses())

    inventory = NetworkCatalogLoader(fetcher, max_workers=2).load(CatalogLoadOptions(CatalogSelection.BOTH, CacheMode.REFRESH))

    identities = [record.candidate.identity.key for record in inventory.records]
    assert len(identities) == len(set(identities))
    joystick = next(record for record in inventory.records if "joystick-2-unit" in record.candidate.identity.key)
    assert {item.catalog for item in joystick.candidate.provenance} == {
        CatalogSource.AWESOME_MICROPYTHON,
        CatalogSource.MIM,
    }
    assert all(mode is CacheMode.REFRESH for _, mode in fetcher.calls)


def test_catalog_loader_isolates_one_unavailable_mim_page():
    responses = _catalog_responses()
    responses.pop("https://checkmim.com/packages/ntptime")

    inventory = NetworkCatalogLoader(FixtureCatalogFetcher(responses), max_workers=2).load(CatalogLoadOptions(CatalogSelection.MIM))

    assert any("joystick-2-unit" in record.candidate.identity.key for record in inventory.records)
    assert inventory.diagnostics[0].reason is ReasonCode.UNAVAILABLE
    assert inventory.diagnostics[0].entry_key == "ntptime"


def test_catalog_loader_reports_mim_sitemap_and_page_progress():
    progress = RecordingProgressReporter()

    NetworkCatalogLoader(FixtureCatalogFetcher(_catalog_responses()), max_workers=2, progress=progress).load(
        CatalogLoadOptions(CatalogSelection.MIM)
    )

    assert progress.events[0] == ("catalog_started", "mim")
    assert ("catalog_total", 3) in progress.events
    advanced = [value for event, value in progress.events if event == "catalog_advanced"]
    assert advanced[0] == "MIM sitemap"
    assert set(advanced[1:]) == {"howmanyoliversarethere+micropython-joystick-2-unit", "ntptime"}
    assert progress.events[-1] == ("catalog_finished", None)


class RecordingFetcher:
    def __init__(self) -> None:
        self.calls: list[str] = []

    def fetch(self, reference: str) -> FetchResponse:
        self.calls.append(reference)
        return FetchResponse(b"ok", reference)


def test_rate_limiter_spaces_requests_and_worker_bound_is_enforced():
    now = [10.0]
    sleeps: list[float] = []

    def sleep(seconds: float) -> None:
        sleeps.append(seconds)
        now[0] += seconds

    upstream = RecordingFetcher()
    fetcher = RateLimitedFetcher(upstream, 2.0, clock=lambda: now[0], sleeper=sleep)
    fetcher.fetch("https://example.invalid/one")
    fetcher.fetch("https://example.invalid/two")

    assert upstream.calls == ["https://example.invalid/one", "https://example.invalid/two"]
    assert sleeps == [0.5]
    with pytest.raises(ValueError, match="between 1 and 16"):
        NetworkCatalogLoader(FixtureCatalogFetcher({}), max_workers=17)


class RecordingCliLoader:
    def __init__(self) -> None:
        self.options: list[CatalogLoadOptions] = []

    def load(
        self,
        options: CatalogLoadOptions,
        *,
        overrides: Mapping[PackageIdentity, ClassificationOverride] | None = None,
    ) -> CatalogInventory:
        _ = overrides
        self.options.append(options)
        return _inventory()


class RecordingCliOrchestrator:
    def __init__(self) -> None:
        self.focused: list[tuple[str, QARequest]] = []
        self.batch: list[tuple[BatchSelection, QARequest]] = []

    def run_focused(self, reference: str, request: QARequest) -> OrchestrationReport:
        self.focused.append((reference, request))
        return EcosystemOrchestrator(FakeResolver(), FakeRunner()).run_focused(reference, request)

    def run_batch(
        self,
        inventory: CatalogInventory,
        selection: BatchSelection,
        request: QARequest,
    ) -> OrchestrationReport:
        self.batch.append((selection, request))
        return EcosystemOrchestrator(FakeResolver(), FakeRunner()).run_batch(inventory, selection, request)


def test_cli_parser_exposes_focused_package_controls():
    reference = "github:howmanyoliversarethere/micropython-joystick-2-unit"
    arguments = build_parser().parse_args(
        [
            "--package",
            reference,
            "--version",
            "v1.28.0",
            "--portboard",
            "rp2-rpi_pico",
            "--stub-source",
            "pypi-pre",
            "--checker",
            "pyright",
            "--cache-mode",
            "offline",
            "--report",
            "--report-output",
            "custom-results",
        ]
    )

    assert arguments.package == reference
    assert arguments.versions == ["v1.28.0"]
    assert arguments.portboard == ["rp2-rpi_pico"]
    assert arguments.stub_source == "pypi-pre"
    assert arguments.cache_mode == "offline"
    assert arguments.report is True
    assert arguments.report_output == Path("custom-results")
    assert arguments.report_mode == "replace"


def test_cli_no_progress_flag_disables_the_shared_runtime_reporter():
    arguments = build_parser().parse_args(["--version", "v1.28.0", "--no-progress"])

    runtime = _build_runtime(arguments)

    assert isinstance(runtime.progress, RichProgressReporter)
    assert runtime.progress.enabled is False
    assert getattr(runtime.catalog_loader, "progress") is runtime.progress
    assert getattr(runtime.orchestrator, "progress") is runtime.progress


def test_cli_defaults_to_mim_esp32_pyright_and_failure_retention():
    loader = RecordingCliLoader()
    orchestrator = RecordingCliOrchestrator()

    exit_code = main(
        ["--version", "v1.28.0", "--stub-source", "path", "--stub-path", "."],
        runtime_factory=lambda _arguments: CliRuntime(loader, orchestrator),
    )

    assert exit_code == 2
    assert loader.options == [CatalogLoadOptions(CatalogSelection.MIM, CacheMode.USE_CACHE)]
    selection, request = orchestrator.batch[0]
    assert selection.catalogs is CatalogSelection.MIM
    assert request.portboards == ("esp32-esp32_generic",)
    assert request.checkers == ("pyright",)
    assert request.unknown_policy is UnknownPortPolicy.USE_REQUESTED
    assert request.retention is WorkspaceRetention.ON_FAILURE


@pytest.mark.parametrize("checker", ["ty", "zuban"])
def test_cli_rejects_xfail_checkers(checker: str):
    with pytest.raises(SystemExit):
        build_parser().parse_args(
            [
                "--catalog",
                "mim",
                "--version",
                "v1.28.0",
                "--portboard",
                "esp32-esp32_generic",
                "--checker",
                checker,
            ]
        )


@pytest.mark.parametrize("checker", ["pyright", "mypy", "ruff", "pyrefly"])
def test_cli_accepts_stable_checkers(checker: str):
    arguments = build_parser().parse_args(
        [
            "--catalog",
            "mim",
            "--version",
            "v1.28.0",
            "--portboard",
            "esp32-esp32_generic",
            "--checker",
            checker,
        ]
    )

    assert arguments.checker == [checker]


def test_focused_cli_bypasses_catalog_and_writes_report_bundle(tmp_path: Path, capsys):
    loader = RecordingCliLoader()
    orchestrator = RecordingCliOrchestrator()
    reference = "github:howmanyoliversarethere/micropython-joystick-2-unit"
    stale_detail = tmp_path / "ecosystem_mypy.md"
    stale_detail.write_text("stale", encoding="utf-8")

    def runtime_factory(_arguments):
        _ = _arguments
        return CliRuntime(loader, orchestrator)

    exit_code = main(
        [
            "--package",
            reference,
            "--version",
            "v1.28.0",
            "--portboard",
            "rp2",
            "--stub-source",
            "path",
            "--stub-path",
            ".",
            "--report",
            "--report-output",
            str(tmp_path),
        ],
        runtime_factory=runtime_factory,
    )

    assert exit_code == 0
    assert loader.options == []
    assert orchestrator.focused[0][0] == reference
    assert orchestrator.focused[0][1].unknown_policy is UnknownPortPolicy.USE_REQUESTED
    assert "ecosystem QA report v2 (focused)" in capsys.readouterr().out
    assert json.loads((tmp_path / "ecosystem.json").read_text(encoding="utf-8"))["mode"] == "focused"
    overview = (tmp_path / "ecosystem.md").read_text(encoding="utf-8")
    assert "# Ecosystem type checker report" in overview
    assert "ecosystem_pyright.md" in overview
    assert (tmp_path / "ecosystem_pyright.md").is_file()
    assert not stale_detail.exists()


def test_cli_keeps_rich_progress_out_of_reports(tmp_path: Path, capsys):
    progress_output = StringIO()
    progress = RichProgressReporter(
        console=Console(file=progress_output, force_terminal=True, color_system=None, width=100),
        enabled=True,
    )
    runtime = CliRuntime(
        RecordingCliLoader(),
        EcosystemOrchestrator(FakeResolver(), FakeRunner(), progress=progress),
        progress,
    )

    exit_code = main(
        [
            "--package",
            "github:howmanyoliversarethere/micropython-joystick-2-unit",
            "--version",
            "v1.28.0",
            "--stub-source",
            "path",
            "--stub-path",
            ".",
            "--report",
            "--report-output",
            str(tmp_path),
        ],
        runtime_factory=lambda _arguments: runtime,
    )

    assert exit_code == 0
    assert "Testing packages" not in capsys.readouterr().out
    assert json.loads((tmp_path / "ecosystem.json").read_text(encoding="utf-8"))["mode"] == "focused"
    assert "Testing packages" in progress_output.getvalue()


def test_batch_cli_forwards_filters_refresh_and_report_path(tmp_path: Path):
    loader = RecordingCliLoader()
    orchestrator = RecordingCliOrchestrator()
    report_output = tmp_path / "reports"

    def runtime_factory(_arguments):
        _ = _arguments
        return CliRuntime(loader, orchestrator)

    exit_code = main(
        [
            "--catalog",
            "mim",
            "--version",
            "v1.28.0",
            "--portboard",
            "esp32",
            "--stub-source",
            "path",
            "--stub-path",
            ".",
            "--package-filter",
            "esp32",
            "--classification",
            "port_specific",
            "--port-filter",
            "esp32",
            "--limit",
            "1",
            "--refresh",
            "--workers",
            "2",
            "--rate-limit",
            "3",
            "--unknown-policy",
            "skip",
            "--report",
            "--report-output",
            str(report_output),
        ],
        runtime_factory=runtime_factory,
    )

    assert exit_code == 2
    assert loader.options == [CatalogLoadOptions(CatalogSelection.MIM, CacheMode.REFRESH)]
    selection, request = orchestrator.batch[0]
    assert selection.classification is PortClassification.PORT_SPECIFIC
    assert selection.port == "esp32"
    assert selection.limit == 1
    assert request.cache_mode is CacheMode.REFRESH
    assert request.unknown_policy is UnknownPortPolicy.SKIP
    document = json.loads((report_output / "ecosystem.json").read_text(encoding="utf-8"))
    assert document["mode"] == "batch"
    assert document["cache_mode"] == "refresh"
    assert document["discovery"] == {
        "catalogs": "mim",
        "classification": "port_specific",
        "discovered_packages": 4,
        "limit": 1,
        "package_query": "esp32",
        "port": "esp32",
        "requested_package": None,
        "selected_packages": ["repository:github:example/a-esp32"],
    }


def test_cli_aggregates_repeated_json_runs_and_can_replace_them(tmp_path: Path):
    loader = RecordingCliLoader()
    orchestrator = RecordingCliOrchestrator()
    report_output = tmp_path / "reports"
    report_path = report_output / "ecosystem.json"
    common = [
        "--version",
        "v1.28.0",
        "--stub-source",
        "path",
        "--stub-path",
        ".",
        "--cache-mode",
        "offline",
        "--report",
        "--report-output",
        str(report_output),
        "--report-mode",
        "aggregate",
    ]

    def runtime_factory(_arguments):
        return CliRuntime(loader, orchestrator)

    assert main(["--package", "github:example/first", *common], runtime_factory=runtime_factory) == 0
    assert main(["--catalog", "mim", *common], runtime_factory=runtime_factory) == 2

    document = json.loads(report_path.read_text(encoding="utf-8"))
    assert document["schema_version"] == 1
    assert document["report_type"] == "ecosystem_qa_aggregate"
    assert document["run_schema_version"] == 2
    assert document["run_count"] == 2
    assert [run["mode"] for run in document["runs"]] == ["focused", "batch"]
    assert document["counts"] == {
        outcome: sum(run["counts"][outcome] for run in document["runs"])
        for outcome in ("pass", "type_check_failure", "unsupported", "unavailable", "skipped", "error")
    }
    assert document["exit_code"] == 2
    assert report_path.read_text(encoding="utf-8") == json.dumps(document, indent=2, sort_keys=True) + "\n"
    assert "| Runs | 2 |" in (report_output / "ecosystem.md").read_text(encoding="utf-8")
    assert (report_output / "ecosystem_pyright.md").is_file()

    replacement = [argument for argument in common if argument not in {"--report-mode", "aggregate"}]
    assert main(["--package", "github:example/replacement", *replacement], runtime_factory=runtime_factory) == 0
    replaced = json.loads(report_path.read_text(encoding="utf-8"))
    assert replaced["schema_version"] == 2
    assert replaced["mode"] == "focused"
    assert "runs" not in replaced

    assert main(["--catalog", "mim", *common], runtime_factory=runtime_factory) == 2
    promoted = json.loads(report_path.read_text(encoding="utf-8"))
    assert promoted["run_count"] == 2
    assert [run["mode"] for run in promoted["runs"]] == ["focused", "batch"]


@pytest.mark.parametrize(
    ("existing", "expected_error"),
    [
        ("{not-json\n", "valid JSON"),
        ('{"schema_version": 99}\n', "compatible ecosystem QA report"),
        (
            json.dumps(
                {
                    "schema_version": 1,
                    "report_type": "ecosystem_qa_aggregate",
                    "run_schema_version": 2,
                    "run_count": 0,
                    "counts": {},
                    "exit_code": 0,
                    "runs": [],
                }
            ),
            "runs must be a non-empty list",
        ),
    ],
)
def test_cli_aggregate_rejects_invalid_existing_report_atomically(
    tmp_path: Path,
    capsys,
    existing: str,
    expected_error: str,
):
    report_path = tmp_path / "ecosystem.json"
    report_path.write_text(existing, encoding="utf-8")
    original = report_path.read_bytes()

    exit_code = main(
        [
            "--package",
            "github:example/driver",
            "--version",
            "v1.28.0",
            "--report",
            "--report-output",
            str(tmp_path),
            "--report-mode",
            "aggregate",
        ],
        runtime_factory=lambda _arguments: CliRuntime(RecordingCliLoader(), RecordingCliOrchestrator()),
    )

    assert exit_code == 2
    assert report_path.read_bytes() == original
    assert expected_error in capsys.readouterr().err


def test_cli_aggregate_requires_report(tmp_path: Path, capsys):
    exit_code = main(
        [
            "--package",
            "github:example/driver",
            "--version",
            "v1.28.0",
            "--report-output",
            str(tmp_path),
            "--report-mode",
            "aggregate",
        ],
        runtime_factory=lambda _arguments: CliRuntime(RecordingCliLoader(), RecordingCliOrchestrator()),
    )

    assert exit_code == 2
    assert not (tmp_path / "ecosystem.json").exists()
    assert "requires --report" in capsys.readouterr().err


def test_cli_rejects_unbounded_or_conflicting_network_options(capsys):
    def runtime_factory(arguments):
        _ = arguments
        return CliRuntime(RecordingCliLoader(), RecordingCliOrchestrator())

    base = ["--catalog", "awesome", "--version", "v1.28.0", "--portboard", "rp2"]

    assert main([*base, "--workers", "17"], runtime_factory=runtime_factory) == 2
    assert main([*base, "--cache-mode", "offline", "--refresh"], runtime_factory=runtime_factory) == 2
    assert "ecosystem QA error" in capsys.readouterr().err
