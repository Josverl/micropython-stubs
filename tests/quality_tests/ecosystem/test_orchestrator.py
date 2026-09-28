from pathlib import Path
from typing import Mapping

import pytest

from .catalog import CatalogDiagnostic, CatalogInventory
from .catalog_loader import (
    AWESOME_CATALOG_URL,
    MIM_SITEMAP_URL,
    CatalogLoadOptions,
    NetworkCatalogLoader,
    RateLimitedFetcher,
)
from .cli import CliRuntime, build_parser, main
from .model import (
    CatalogProvenance,
    CatalogSource,
    ClassificationOverride,
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
from .orchestrator import (
    BatchSelection,
    CatalogSelection,
    EcosystemOrchestrator,
    OrchestrationExit,
    OrchestrationReport,
    PackageOutcome,
    QARequest,
    select_inventory_records,
)
from .resolver import CacheMode, FetchResponse, ResolutionResult, ResolvedPayload, ResolverError
from .runner import (
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
    def __init__(self, failing: set[str] | None = None) -> None:
        self.failing = failing or set()
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
        checker_result = QACheckerResult(
            checker=case.checkers[0],
            command=(case.checkers[0], "check"),
            status=CheckerStatus.FAIL if failed else CheckerStatus.PASS,
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
            retained_workspace=None,
        )


def _resolved(record: PackageRecord) -> ResolutionResult:
    source = b"value = 1\n"
    package_file = PackageFile(record.candidate.identity, "driver.py", "https://fixtures.invalid/driver.py", size=len(source))
    resolution = PackageResolution(
        requested_reference=record.candidate.install_reference,
        canonical_reference=record.candidate.install_reference,
        requested_revision=None,
        resolved_revision="fixture",
        manifest_reference="https://fixtures.invalid/package.json",
        manifest_sha256=None,
        dependencies=(),
        files=(package_file,),
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


def test_orchestration_exit_codes_distinguish_type_failures_and_intentional_skips():
    orchestrator = EcosystemOrchestrator(FakeResolver(), FakeRunner(failing={"z-portable"}))

    type_failure = orchestrator.run_batch(_inventory(), BatchSelection(package_query="z-portable"), _request())
    skipped = orchestrator.run_batch(_inventory(), BatchSelection(package_query="n-unknown"), _request())

    assert type_failure.exit_code is OrchestrationExit.TYPE_CHECK_FAILURE
    assert skipped.exit_code is OrchestrationExit.SUCCESS
    assert skipped.results[0].outcome is PackageOutcome.SKIPPED


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


def _catalog_responses() -> dict[str, bytes]:
    fixtures = Path(__file__).parent / "fixtures"
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
            "json",
        ]
    )

    assert arguments.package == reference
    assert arguments.versions == ["v1.28.0"]
    assert arguments.portboard == ["rp2-rpi_pico"]
    assert arguments.stub_source == "pypi-pre"
    assert arguments.cache_mode == "offline"
    assert arguments.report == "json"


def test_focused_cli_bypasses_catalog_and_emits_json(capsys):
    loader = RecordingCliLoader()
    orchestrator = RecordingCliOrchestrator()
    reference = "github:howmanyoliversarethere/micropython-joystick-2-unit"

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
            "json",
        ],
        runtime_factory=runtime_factory,
    )

    assert exit_code == 0
    assert loader.options == []
    assert orchestrator.focused[0][0] == reference
    assert orchestrator.focused[0][1].unknown_policy is UnknownPortPolicy.USE_REQUESTED
    assert '"mode": "focused"' in capsys.readouterr().out


def test_batch_cli_forwards_filters_refresh_and_report_path(tmp_path: Path):
    loader = RecordingCliLoader()
    orchestrator = RecordingCliOrchestrator()
    report_path = tmp_path / "reports" / "ecosystem.json"

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
            "--report",
            "json",
            "--report-file",
            str(report_path),
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
    assert '"mode": "batch"' in report_path.read_text(encoding="utf-8")


def test_cli_rejects_unbounded_or_conflicting_network_options(capsys):
    def runtime_factory(arguments):
        _ = arguments
        return CliRuntime(RecordingCliLoader(), RecordingCliOrchestrator())

    base = ["--catalog", "awesome", "--version", "v1.28.0", "--portboard", "rp2"]

    assert main([*base, "--workers", "17"], runtime_factory=runtime_factory) == 2
    assert main([*base, "--cache-mode", "offline", "--refresh"], runtime_factory=runtime_factory) == 2
    assert "ecosystem QA error" in capsys.readouterr().err
