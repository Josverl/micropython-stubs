"""Command-line entry point for focused and batch ecosystem stub QA."""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
import json
import os
from pathlib import Path
import sys
import tempfile
from typing import Callable, Mapping, Protocol, Sequence

from .aggregate import AggregateReport
from .catalog import CatalogInventory
from .catalog_loader import CatalogLoadOptions, NetworkCatalogLoader, RateLimitedFetcher
from .markdown_report import render_markdown_reports
from .model import ClassificationOverride, PackageIdentity, PortClassification, load_classification_overrides
from .orchestrator import BatchSelection, CatalogSelection, EcosystemOrchestrator, OrchestrationReport, QARequest
from .progress import NullProgressReporter, ProgressReporter, RichProgressReporter
from .resolver import CacheMode, CachedFetcher, DestinationPolicy, MipResolver, UrlFetcher
from .runner import ExistingCheckerBackend, QARunner, StubSource, UnknownPortPolicy, UvStubProvisioner, WorkspaceRetention


class CliCatalogLoader(Protocol):
    def load(
        self,
        options: CatalogLoadOptions,
        *,
        overrides: Mapping[PackageIdentity, ClassificationOverride] | None = None,
    ) -> CatalogInventory: ...


class CliOrchestrator(Protocol):
    def run_focused(self, reference: str, request: QARequest) -> OrchestrationReport: ...

    def run_batch(
        self,
        inventory: CatalogInventory,
        selection: BatchSelection,
        request: QARequest,
    ) -> OrchestrationReport: ...


@dataclass(frozen=True)
class CliRuntime:
    catalog_loader: CliCatalogLoader
    orchestrator: CliOrchestrator
    progress: ProgressReporter = field(default_factory=NullProgressReporter)


RuntimeFactory = Callable[[argparse.Namespace], CliRuntime]

DEFAULT_CATALOG = CatalogSelection.MIM.value
DEFAULT_PORTBOARD = "esp32-esp32_generic"
DEFAULT_CHECKER = "pyright"
DEFAULT_REPORT_OUTPUT = Path("results")
DEFAULT_PACKAGE_LIMIT: int | None = None
DEFAULT_CATALOG_WORKERS = 4
DEFAULT_RATE_LIMIT = 2.0
STABLE_CHECKERS = ("pyright", "mypy", "ruff", "pyrefly")
CLI_STUB_SOURCES = (StubSource.LOCAL.value, StubSource.PYPI.value, StubSource.PYPI_PRE.value)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ecosystem-qa",
        description="Validate MicroPython stubs against focused or catalog ecosystem packages.",
    )
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--package", help="Direct package reference; bypasses catalog discovery")
    source.add_argument(
        "--catalog",
        choices=[item.value for item in CatalogSelection],
        default=DEFAULT_CATALOG,
        help=f"Batch catalog source (default: {DEFAULT_CATALOG})",
    )
    parser.add_argument(
        "--version",
        required=True,
        help="MicroPython version used for stubs and micropython-lib source",
    )
    parser.add_argument(
        "--portboard",
        action="append",
        help=f"Port or port-board stub target; repeatable (default: {DEFAULT_PORTBOARD})",
    )
    parser.add_argument("--stub-source", choices=CLI_STUB_SOURCES, default=StubSource.LOCAL.value)
    parser.add_argument(
        "--checker",
        action="append",
        choices=STABLE_CHECKERS,
        help=f"Checker name; repeatable (default: {DEFAULT_CHECKER})",
    )
    parser.add_argument("--no-stub-cache", action="store_true", help="Disable uv's cache while provisioning stubs")

    parser.add_argument("--cache-mode", choices=[item.value for item in CacheMode], default=CacheMode.USE_CACHE.value)
    parser.add_argument("--refresh", action="store_true", help="Refresh catalog and package response cache entries")
    parser.add_argument("--cache-dir", type=Path, default=Path("tests/quality_tests/.ecosystem-cache"))
    parser.add_argument("--workspace-dir", type=Path, default=Path("tests/quality_tests/.ecosystem-cache/runs"))
    parser.add_argument("--no-progress", action="store_true", help="Disable interactive progress reporting")
    parser.add_argument(
        "--retain",
        choices=[item.value for item in WorkspaceRetention],
        default=WorkspaceRetention.ON_FAILURE.value,
        help=f"Workspace retention policy (default: {WorkspaceRetention.ON_FAILURE.value})",
    )
    parser.add_argument(
        "--unknown-policy",
        choices=[item.value for item in UnknownPortPolicy],
        help=f"Handling for unknown or ambiguous compatibility (default: {UnknownPortPolicy.USE_REQUESTED.value})",
    )

    parser.add_argument("--package-filter", help="Case-insensitive batch package substring")
    parser.add_argument("--classification", choices=[item.value for item in PortClassification])
    parser.add_argument("--port-filter", help="Batch compatibility filter for a port or port-board")

    parser.add_argument(
        "--report",
        action="store_true",
        help="Write JSON and Markdown ecosystem reports, including one detail report per checker",
    )
    parser.add_argument(
        "--report-output",
        type=Path,
        default=DEFAULT_REPORT_OUTPUT,
        help=f"Report output directory (default: {DEFAULT_REPORT_OUTPUT.as_posix()})",
    )
    parser.add_argument(
        "--report-mode",
        choices=("replace", "aggregate"),
        default="replace",
        help="JSON report behavior; aggregate combines compatible runs and regenerates Markdown (default: replace)",
    )
    return parser


def main(argv: Sequence[str] | None = None, *, runtime_factory: RuntimeFactory | None = None) -> int:
    parser = build_parser()
    arguments = parser.parse_args(argv)
    try:
        _validate_arguments(arguments)
        runtime = (runtime_factory or _build_runtime)(arguments)
        request = _qa_request(arguments)
        with runtime.progress:
            if arguments.package is not None:
                report = runtime.orchestrator.run_focused(arguments.package, request)
            else:
                catalog = CatalogSelection(arguments.catalog)
                project_root = _project_root()
                overrides = load_classification_overrides(
                    project_root / "tests" / "quality_tests" / "ecosystem" / "classification_overrides.json"
                )
                inventory = runtime.catalog_loader.load(
                    CatalogLoadOptions(catalog, request.cache_mode, _micropython_lib_tag(arguments.version)),
                    overrides=overrides,
                )
                selection = BatchSelection(
                    catalogs=catalog,
                    package_query=arguments.package_filter,
                    classification=PortClassification(arguments.classification) if arguments.classification else None,
                    port=arguments.port_filter,
                    limit=DEFAULT_PACKAGE_LIMIT,
                )
                report = runtime.orchestrator.run_batch(inventory, selection, request)
        if arguments.report:
            _write_reports(
                report,
                _absolute_from_project(arguments.report_output, _project_root()),
                arguments.report_mode,
            )
        print(report.render_text())
        return int(report.exit_code)
    except (OSError, RuntimeError, ValueError) as error:
        print(f"ecosystem QA error: {error}", file=sys.stderr)
        return 2


def _validate_arguments(arguments: argparse.Namespace) -> None:
    if arguments.refresh and arguments.cache_mode == CacheMode.OFFLINE.value:
        raise ValueError("--refresh cannot be combined with --cache-mode offline")
    batch_filters = (arguments.package_filter, arguments.classification, arguments.port_filter)
    if arguments.package is not None and any(value is not None for value in batch_filters):
        raise ValueError("batch filters require --catalog")
    if arguments.report_mode == "aggregate" and not arguments.report:
        raise ValueError("--report-mode aggregate requires --report")
    if not arguments.version.strip():
        raise ValueError("--version must not be empty")


def _qa_request(arguments: argparse.Namespace) -> QARequest:
    cache_mode = CacheMode.REFRESH if arguments.refresh else CacheMode(arguments.cache_mode)
    if arguments.unknown_policy is not None:
        unknown_policy = UnknownPortPolicy(arguments.unknown_policy)
    else:
        unknown_policy = UnknownPortPolicy.USE_REQUESTED
    return QARequest(
        versions=(arguments.version,),
        portboards=tuple(arguments.portboard or (DEFAULT_PORTBOARD,)),
        stub_source=StubSource(arguments.stub_source),
        checkers=tuple(arguments.checker or (DEFAULT_CHECKER,)),
        cache_mode=cache_mode,
        unknown_policy=unknown_policy,
        retention=WorkspaceRetention(arguments.retain),
        no_stub_cache=arguments.no_stub_cache,
        portboards_explicit=arguments.portboard is not None,
    )


def _build_runtime(arguments: argparse.Namespace) -> CliRuntime:
    project_root = _project_root()
    cache_dir = _absolute_from_project(arguments.cache_dir, project_root)
    workspace_dir = _absolute_from_project(arguments.workspace_dir, project_root)
    progress = RichProgressReporter(enabled=False if arguments.no_progress else None)
    upstream = RateLimitedFetcher(UrlFetcher(destination_policy=DestinationPolicy()), DEFAULT_RATE_LIMIT)
    fetcher = CachedFetcher(cache_dir, upstream)
    catalog_loader = NetworkCatalogLoader(fetcher, max_workers=DEFAULT_CATALOG_WORKERS, progress=progress)
    resolver = MipResolver(fetcher, micropython_lib_revision=_micropython_lib_tag(arguments.version))
    runner = QARunner(
        workspace_root=workspace_dir,
        config_root=project_root / "tests" / "quality_tests" / "_configs",
        stub_provisioner=UvStubProvisioner(project_root),
        checker_backend=ExistingCheckerBackend(),
    )
    return CliRuntime(catalog_loader, EcosystemOrchestrator(resolver, runner, progress=progress), progress)


def _write_reports(report: OrchestrationReport, destination: Path, report_mode: str) -> None:
    json_path = destination / "ecosystem.json"
    if report_mode == "aggregate":
        aggregate = AggregateReport.from_path(json_path) if json_path.exists() else AggregateReport()
        report_document = aggregate.append(report.to_dict()).to_dict()
    else:
        report_document = report.to_dict()

    markdown = render_markdown_reports(report_document)
    json_content = json.dumps(report_document, indent=2, sort_keys=True) + "\n"
    _atomic_write_text(json_path, json_content)
    _atomic_write_text(destination / "ecosystem.md", markdown.overview)
    for checker, content in markdown.checker_details.items():
        _atomic_write_text(destination / markdown.detail_filenames[checker], content)
    expected_details = {destination / filename for filename in markdown.detail_filenames.values()}
    for existing_detail in destination.glob("ecosystem_*.md"):
        if existing_detail not in expected_details:
            existing_detail.unlink()


def _atomic_write_text(destination: Path, content: str) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            "w",
            encoding="utf-8",
            newline="\n",
            dir=destination.parent,
            prefix=f".{destination.name}.",
            suffix=".tmp",
            delete=False,
        ) as temporary:
            temporary.write(content)
            temporary.flush()
            os.fsync(temporary.fileno())
            temporary_path = Path(temporary.name)
        os.replace(temporary_path, destination)
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


def _absolute_from_project(path: Path, project_root: Path) -> Path:
    return path.resolve() if path.is_absolute() else (project_root / path).resolve()


def _micropython_lib_tag(version: str) -> str:
    version = version.strip()
    return version if version.casefold().startswith("v") else f"v{version}"


def _project_root() -> Path:
    return Path(__file__).resolve().parents[3]


if __name__ == "__main__":
    raise SystemExit(main())
