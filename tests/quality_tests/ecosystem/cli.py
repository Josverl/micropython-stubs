"""Command-line entry point for focused and batch ecosystem stub QA."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import sys
from typing import Callable, Mapping, Protocol, Sequence

from .catalog import CatalogInventory
from .catalog_loader import CatalogLoadOptions, MAX_CATALOG_WORKERS, NetworkCatalogLoader, RateLimitedFetcher
from .model import ClassificationOverride, PackageIdentity, PortClassification, load_classification_overrides
from .orchestrator import BatchSelection, CatalogSelection, EcosystemOrchestrator, OrchestrationReport, QARequest
from .resolver import CacheMode, CachedFetcher, MipResolver, UrlFetcher
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


RuntimeFactory = Callable[[argparse.Namespace], CliRuntime]

DEFAULT_CATALOG = CatalogSelection.MIM.value
DEFAULT_PORTBOARD = "esp32-esp32_generic"
DEFAULT_CHECKER = "pyright"
STABLE_CHECKERS = ("pyright", "mypy", "ruff", "pyrefly")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ecosystem-qa",
        description="Validate MicroPython stubs against focused or catalog ecosystem packages.",
    )
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--package", help="Direct MIP package reference; bypasses catalog discovery")
    source.add_argument(
        "--catalog",
        choices=[item.value for item in CatalogSelection],
        default=DEFAULT_CATALOG,
        help=f"Batch catalog source (default: {DEFAULT_CATALOG})",
    )

    parser.add_argument("--version", dest="versions", action="append", required=True, help="MicroPython version; repeatable")
    parser.add_argument(
        "--portboard",
        action="append",
        help=f"Port or port-board stub target; repeatable (default: {DEFAULT_PORTBOARD})",
    )
    parser.add_argument("--stub-source", choices=[item.value for item in StubSource], default=StubSource.LOCAL.value)
    parser.add_argument("--stub-path", type=Path, help="Stub tree used with --stub-source path")
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
    parser.add_argument(
        "--retain",
        choices=[item.value for item in WorkspaceRetention],
        default=WorkspaceRetention.ON_FAILURE.value,
        help=f"Workspace retention policy (default: {WorkspaceRetention.ON_FAILURE.value})",
    )
    parser.add_argument("--unknown-policy", choices=[item.value for item in UnknownPortPolicy])

    parser.add_argument("--package-filter", help="Case-insensitive batch package substring")
    parser.add_argument("--classification", choices=[item.value for item in PortClassification])
    parser.add_argument("--port-filter", help="Batch compatibility filter for a port or port-board")
    parser.add_argument("--limit", type=int, help="Maximum number of selected batch packages")
    parser.add_argument("--workers", type=int, default=4, help=f"MIM page fetch workers (1-{MAX_CATALOG_WORKERS})")
    parser.add_argument("--rate-limit", type=float, default=2.0, help="Upstream request starts per second (greater than 0, at most 100)")

    parser.add_argument("--report", choices=("text", "json"), default="text")
    parser.add_argument("--report-file", type=Path, help="Write the selected report format to this path")
    return parser


def main(argv: Sequence[str] | None = None, *, runtime_factory: RuntimeFactory | None = None) -> int:
    parser = build_parser()
    arguments = parser.parse_args(argv)
    try:
        _validate_arguments(arguments)
        runtime = (runtime_factory or _build_runtime)(arguments)
        request = _qa_request(arguments)
        if arguments.package is not None:
            report = runtime.orchestrator.run_focused(arguments.package, request)
        else:
            catalog = CatalogSelection(arguments.catalog)
            project_root = _project_root()
            overrides = load_classification_overrides(
                project_root / "tests" / "quality_tests" / "ecosystem" / "classification_overrides.json"
            )
            inventory = runtime.catalog_loader.load(
                CatalogLoadOptions(catalog, request.cache_mode),
                overrides=overrides,
            )
            selection = BatchSelection(
                catalogs=catalog,
                package_query=arguments.package_filter,
                classification=PortClassification(arguments.classification) if arguments.classification else None,
                port=arguments.port_filter,
                limit=arguments.limit,
            )
            report = runtime.orchestrator.run_batch(inventory, selection, request)
        _write_report(report, arguments.report, arguments.report_file)
        return int(report.exit_code)
    except (OSError, RuntimeError, ValueError) as error:
        print(f"ecosystem QA error: {error}", file=sys.stderr)
        return 2


def _validate_arguments(arguments: argparse.Namespace) -> None:
    if not 1 <= arguments.workers <= MAX_CATALOG_WORKERS:
        raise ValueError(f"workers must be between 1 and {MAX_CATALOG_WORKERS}")
    if arguments.rate_limit <= 0 or arguments.rate_limit > 100:
        raise ValueError("rate limit must be greater than 0 and at most 100")
    if arguments.limit is not None and arguments.limit < 1:
        raise ValueError("limit must be at least 1")
    if arguments.refresh and arguments.cache_mode == CacheMode.OFFLINE.value:
        raise ValueError("--refresh cannot be combined with --cache-mode offline")
    batch_filters = (arguments.package_filter, arguments.classification, arguments.port_filter, arguments.limit)
    if arguments.package is not None and any(value is not None for value in batch_filters):
        raise ValueError("batch filters require --catalog")


def _qa_request(arguments: argparse.Namespace) -> QARequest:
    cache_mode = CacheMode.REFRESH if arguments.refresh else CacheMode(arguments.cache_mode)
    if arguments.unknown_policy is not None:
        unknown_policy = UnknownPortPolicy(arguments.unknown_policy)
    elif arguments.package is not None:
        unknown_policy = UnknownPortPolicy.USE_REQUESTED
    else:
        unknown_policy = UnknownPortPolicy.SKIP
    return QARequest(
        versions=tuple(arguments.versions),
        portboards=tuple(arguments.portboard or (DEFAULT_PORTBOARD,)),
        stub_source=StubSource(arguments.stub_source),
        stub_path=arguments.stub_path,
        checkers=tuple(arguments.checker or (DEFAULT_CHECKER,)),
        cache_mode=cache_mode,
        unknown_policy=unknown_policy,
        retention=WorkspaceRetention(arguments.retain),
        no_stub_cache=arguments.no_stub_cache,
    )


def _build_runtime(arguments: argparse.Namespace) -> CliRuntime:
    project_root = _project_root()
    cache_dir = _absolute_from_project(arguments.cache_dir, project_root)
    workspace_dir = _absolute_from_project(arguments.workspace_dir, project_root)
    upstream = RateLimitedFetcher(UrlFetcher(), arguments.rate_limit)
    fetcher = CachedFetcher(cache_dir, upstream)
    catalog_loader = NetworkCatalogLoader(fetcher, max_workers=arguments.workers)
    resolver = MipResolver(fetcher)
    runner = QARunner(
        workspace_root=workspace_dir,
        config_root=project_root / "tests" / "quality_tests" / "_configs",
        stub_provisioner=UvStubProvisioner(project_root),
        checker_backend=ExistingCheckerBackend(),
    )
    return CliRuntime(catalog_loader, EcosystemOrchestrator(resolver, runner))


def _write_report(report: OrchestrationReport, report_format: str, destination: Path | None) -> None:
    content = report.to_json() if report_format == "json" else report.render_text() + "\n"
    if destination is None:
        print(content, end="")
        return
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(content, encoding="utf-8")


def _absolute_from_project(path: Path, project_root: Path) -> Path:
    return path.resolve() if path.is_absolute() else (project_root / path).resolve()


def _project_root() -> Path:
    return Path(__file__).resolve().parents[3]


if __name__ == "__main__":
    raise SystemExit(main())
