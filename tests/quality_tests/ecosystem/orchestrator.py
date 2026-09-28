"""Selection and orchestration for ecosystem package QA."""

from __future__ import annotations

import json
from dataclasses import dataclass
from enum import Enum, IntEnum
from pathlib import Path
import time
from typing import Protocol

from .catalog import CatalogDiagnostic, CatalogInventory
from .model import CatalogSource, PackageCandidate, PackageRecord, PortClassification, PortDecision, ReasonCode, RecordDisposition
from .resolver import CacheMode, ResolutionResult, ResolverError
from .runner import (
    CheckerStatus,
    QACase,
    QARunReport,
    StubSource,
    UnknownPortPolicy,
    WorkspaceRetention,
    plan_qa_matrix,
)


class CatalogSelection(str, Enum):
    AWESOME = "awesome"
    MIM = "mim"
    BOTH = "both"

    @property
    def sources(self) -> frozenset[CatalogSource]:
        if self is CatalogSelection.AWESOME:
            return frozenset({CatalogSource.AWESOME_MICROPYTHON})
        if self is CatalogSelection.MIM:
            return frozenset({CatalogSource.MIM})
        return frozenset({CatalogSource.AWESOME_MICROPYTHON, CatalogSource.MIM})


@dataclass(frozen=True)
class BatchSelection:
    catalogs: CatalogSelection = CatalogSelection.BOTH
    package_query: str | None = None
    classification: PortClassification | None = None
    port: str | None = None
    limit: int | None = None

    def __post_init__(self) -> None:
        if self.package_query is not None and not self.package_query.strip():
            raise ValueError("package query must not be empty")
        if self.port is not None and not self.port.strip():
            raise ValueError("port filter must not be empty")
        if self.limit is not None and self.limit < 1:
            raise ValueError("limit must be at least 1")


class PackageOutcome(str, Enum):
    PASS = "pass"
    TYPE_CHECK_FAILURE = "type_check_failure"
    UNSUPPORTED = "unsupported"
    UNAVAILABLE = "unavailable"
    SKIPPED = "skipped"
    ERROR = "error"


class OrchestrationExit(IntEnum):
    SUCCESS = 0
    TYPE_CHECK_FAILURE = 1
    OPERATIONAL_FAILURE = 2


@dataclass(frozen=True)
class QARequest:
    versions: tuple[str, ...]
    portboards: tuple[str, ...]
    stub_source: StubSource
    checkers: tuple[str, ...]
    stub_path: Path | None = None
    cache_mode: CacheMode = CacheMode.USE_CACHE
    unknown_policy: UnknownPortPolicy = UnknownPortPolicy.SKIP
    retention: WorkspaceRetention = WorkspaceRetention.NEVER
    no_stub_cache: bool = False

    def __post_init__(self) -> None:
        versions = tuple(sorted(set(value.strip() for value in self.versions if value.strip())))
        portboards = tuple(sorted(set(value.strip().casefold() for value in self.portboards if value.strip())))
        checkers = tuple(dict.fromkeys(value.strip().casefold() for value in self.checkers if value.strip()))
        if not versions or not portboards or not checkers:
            raise ValueError("versions, portboards, and checkers must not be empty")
        if self.stub_source is StubSource.PATH and self.stub_path is None:
            raise ValueError("path stub source requires --stub-path")
        if self.stub_source is not StubSource.PATH and self.stub_path is not None:
            raise ValueError("--stub-path is only valid for path stub source")
        object.__setattr__(self, "versions", versions)
        object.__setattr__(self, "portboards", portboards)
        object.__setattr__(self, "checkers", checkers)


@dataclass(frozen=True)
class PackageQAResult:
    package_identity: str
    package_reference: str
    outcome: PackageOutcome
    reason: ReasonCode | None = None
    message: str = ""
    reports: tuple[QARunReport, ...] = ()

    def to_dict(self) -> dict[str, object]:
        return {
            "package_identity": self.package_identity,
            "package_reference": self.package_reference,
            "outcome": self.outcome.value,
            "reason": self.reason.value if self.reason else None,
            "message": self.message,
            "reports": [report.to_dict() for report in self.reports],
        }


@dataclass(frozen=True)
class OrchestrationReport:
    mode: str
    results: tuple[PackageQAResult, ...]
    catalog_diagnostics: tuple[CatalogDiagnostic, ...]
    duration_seconds: float

    @property
    def counts(self) -> dict[str, int]:
        return {outcome.value: sum(result.outcome is outcome for result in self.results) for outcome in PackageOutcome}

    @property
    def exit_code(self) -> OrchestrationExit:
        outcomes = {result.outcome for result in self.results}
        has_catalog_errors = any(diagnostic.disposition is RecordDisposition.ERROR for diagnostic in self.catalog_diagnostics)
        if not outcomes or has_catalog_errors or outcomes & {PackageOutcome.UNSUPPORTED, PackageOutcome.UNAVAILABLE, PackageOutcome.ERROR}:
            return OrchestrationExit.OPERATIONAL_FAILURE
        if PackageOutcome.TYPE_CHECK_FAILURE in outcomes:
            return OrchestrationExit.TYPE_CHECK_FAILURE
        return OrchestrationExit.SUCCESS

    def to_dict(self) -> dict[str, object]:
        return {
            "schema_version": 1,
            "mode": self.mode,
            "exit_code": int(self.exit_code),
            "counts": self.counts,
            "results": [result.to_dict() for result in self.results],
            "catalog_diagnostics": [_catalog_diagnostic_to_dict(item) for item in self.catalog_diagnostics],
            "duration_seconds": self.duration_seconds,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2, sort_keys=True) + "\n"

    def render_text(self) -> str:
        lines = [f"ecosystem QA ({self.mode})"]
        for result in self.results:
            detail = f" [{result.reason.value}]" if result.reason else ""
            lines.append(f"  {result.package_identity}: {result.outcome.value}{detail}")
            if result.message:
                lines.append(f"    {result.message.strip()}")
        for diagnostic in self.catalog_diagnostics:
            lines.append(f"  {diagnostic.catalog.value}:{diagnostic.entry_key}: {diagnostic.disposition.value} [{diagnostic.reason.value}]")
            lines.append(f"    {diagnostic.detail.strip()}")
        counts = ", ".join(f"{name}={count}" for name, count in self.counts.items())
        lines.append(f"summary: {counts}; exit={int(self.exit_code)}; {self.duration_seconds:.3f}s")
        return "\n".join(lines)


class PackageResolver(Protocol):
    def resolve_reference(self, reference: str, *, mode: CacheMode = CacheMode.USE_CACHE) -> ResolutionResult: ...

    def resolve_candidate(
        self,
        candidate: PackageCandidate,
        *,
        classification: PortDecision | None = None,
        mode: CacheMode = CacheMode.USE_CACHE,
    ) -> ResolutionResult: ...


class PackageRunner(Protocol):
    def run(
        self,
        resolution: ResolutionResult,
        case: QACase,
        *,
        retention: WorkspaceRetention = WorkspaceRetention.NEVER,
    ) -> QARunReport: ...


class EcosystemOrchestrator:
    def __init__(self, resolver: PackageResolver, runner: PackageRunner) -> None:
        self.resolver = resolver
        self.runner = runner

    def run_focused(self, reference: str, request: QARequest) -> OrchestrationReport:
        started = time.perf_counter()
        try:
            resolution = self.resolver.resolve_reference(reference, mode=request.cache_mode)
            result = self._run_resolution(resolution, request)
        except Exception as error:
            result = _exception_result(reference, reference, error)
        return OrchestrationReport("focused", (result,), (), time.perf_counter() - started)

    def run_batch(
        self,
        inventory: CatalogInventory,
        selection: BatchSelection,
        request: QARequest,
    ) -> OrchestrationReport:
        started = time.perf_counter()
        results: list[PackageQAResult] = []
        for record in select_inventory_records(inventory, selection):
            candidate = record.candidate
            try:
                resolution = self.resolver.resolve_candidate(
                    candidate,
                    classification=record.classification,
                    mode=request.cache_mode,
                )
                results.append(self._run_resolution(resolution, request))
            except Exception as error:
                results.append(_exception_result(candidate.identity.key, candidate.install_reference, error))
        return OrchestrationReport("batch", tuple(results), inventory.diagnostics, time.perf_counter() - started)

    def _run_resolution(self, resolution: ResolutionResult, request: QARequest) -> PackageQAResult:
        record = resolution.record
        candidate = record.candidate
        if record.disposition is not RecordDisposition.CHECK:
            return PackageQAResult(
                candidate.identity.key,
                candidate.install_reference,
                _record_outcome(record),
                record.reason,
            )

        plan = plan_qa_matrix(
            record,
            versions=request.versions,
            available_portboards=request.portboards,
            stub_source=request.stub_source,
            stub_path=request.stub_path,
            no_stub_cache=request.no_stub_cache,
            checkers=request.checkers,
            unknown_policy=request.unknown_policy,
        )
        if plan.disposition is not RecordDisposition.CHECK:
            return PackageQAResult(
                candidate.identity.key,
                candidate.install_reference,
                PackageOutcome.SKIPPED,
                plan.reason,
            )

        reports = tuple(self.runner.run(resolution, case, retention=request.retention) for case in plan.cases)
        statuses = {report.status for report in reports}
        if CheckerStatus.ERROR in statuses:
            outcome = PackageOutcome.ERROR
        elif CheckerStatus.FAIL in statuses:
            outcome = PackageOutcome.TYPE_CHECK_FAILURE
        elif statuses == {CheckerStatus.SKIP}:
            outcome = PackageOutcome.SKIPPED
        else:
            outcome = PackageOutcome.PASS
        messages = tuple(result.message for report in reports for result in report.results if result.message)
        return PackageQAResult(
            candidate.identity.key,
            candidate.install_reference,
            outcome,
            message="; ".join(dict.fromkeys(messages)),
            reports=reports,
        )


def select_inventory_records(inventory: CatalogInventory, selection: BatchSelection) -> tuple[PackageRecord, ...]:
    """Select normalized records deterministically without resolving packages."""
    records = (
        record
        for record in inventory.records
        if _matches_catalog(record, selection.catalogs.sources)
        and _matches_package(record, selection.package_query)
        and _matches_classification(record, selection.classification)
        and _matches_port(record, selection.port)
    )
    selected = tuple(sorted(records, key=lambda record: record.candidate.identity.key))
    return selected[: selection.limit] if selection.limit is not None else selected


def _matches_catalog(record: PackageRecord, sources: frozenset[CatalogSource]) -> bool:
    return any(item.catalog in sources for item in record.candidate.provenance)


def _matches_package(record: PackageRecord, query: str | None) -> bool:
    if query is None:
        return True
    query = query.strip().casefold()
    candidate = record.candidate
    values = (
        candidate.identity.key,
        candidate.display_name,
        candidate.install_reference,
        *(alias.reference for alias in candidate.aliases),
    )
    return any(query in value.casefold() for value in values)


def _matches_classification(record: PackageRecord, classification: PortClassification | None) -> bool:
    return classification is None or (record.classification is not None and record.classification.classification is classification)


def _matches_port(record: PackageRecord, requested: str | None) -> bool:
    if requested is None:
        return True
    decision = record.classification
    if decision is None or decision.classification is PortClassification.UNKNOWN:
        return False
    if decision.classification is PortClassification.PORTABLE:
        return True
    requested = requested.strip().casefold()
    port, separator, board = requested.partition("-")
    return (
        requested in decision.ports
        or requested in decision.boards
        or port in decision.ports
        or (bool(separator) and board in decision.boards)
    )


def _record_outcome(record: PackageRecord) -> PackageOutcome:
    if record.disposition in {RecordDisposition.SKIP, RecordDisposition.DEFERRED}:
        return PackageOutcome.SKIPPED
    return _reason_outcome(record.reason)


def _reason_outcome(reason: ReasonCode | None) -> PackageOutcome:
    if reason in {ReasonCode.UNSUPPORTED_REFERENCE, ReasonCode.UNSUPPORTED_SOURCE}:
        return PackageOutcome.UNSUPPORTED
    if reason in {
        ReasonCode.UNAVAILABLE,
        ReasonCode.DEPENDENCY_UNAVAILABLE,
        ReasonCode.CACHE_MISS,
        ReasonCode.CACHE_CORRUPT,
    }:
        return PackageOutcome.UNAVAILABLE
    return PackageOutcome.ERROR


def _exception_result(identity: str, reference: str, error: Exception) -> PackageQAResult:
    reason = error.reason if isinstance(error, ResolverError) else None
    return PackageQAResult(identity, reference, _reason_outcome(reason), reason, str(error))


def _catalog_diagnostic_to_dict(diagnostic: CatalogDiagnostic) -> dict[str, object]:
    return {
        "catalog": diagnostic.catalog.value,
        "entry_key": diagnostic.entry_key,
        "source_url": diagnostic.source_url,
        "disposition": diagnostic.disposition.value,
        "reason": diagnostic.reason.value,
        "detail": diagnostic.detail,
        "reference": diagnostic.reference,
    }
