"""Isolated type-checking runner for resolved ecosystem packages."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from itertools import product
from pathlib import Path, PurePosixPath
from typing import Iterable, Mapping, Protocol

from mpflash.versions import clean_version

if __package__ == "ecosystem":
    from typecheck import filter_issues, invoke_typechecker
else:
    from ..typecheck import filter_issues, invoke_typechecker

from .model import FileKind, IdentityKind, PackageRecord, PackageResolution, PortClassification, ReasonCode, RecordDisposition
from .reporting import (
    REPORT_SCHEMA_VERSION,
    resolution_text,
    resolution_to_dict,
    sanitize_report_command,
    sanitize_report_document,
    sanitize_report_text,
)
from .resolver import ResolutionResult


_REPOSITORY_WEB_ROOTS = {
    "codeberg": "https://codeberg.org",
    "github": "https://github.com",
    "gitlab": "https://gitlab.com",
}


class StubSource(str, Enum):
    LOCAL = "local"
    PYPI = "pypi"
    PYPI_PRE = "pypi-pre"
    PATH = "path"


class UnknownPortPolicy(str, Enum):
    SKIP = "skip"
    USE_REQUESTED = "use_requested"


class WorkspaceRetention(str, Enum):
    NEVER = "never"
    ON_FAILURE = "on_failure"
    ALWAYS = "always"


class CheckerStatus(str, Enum):
    PASS = "pass"
    FAIL = "fail"
    ERROR = "error"
    SKIP = "skip"


@dataclass(frozen=True)
class StubSelection:
    version: str
    portboard: str
    source: StubSource
    path: Path | None = None
    no_cache: bool = False

    def __post_init__(self) -> None:
        if not self.version.strip() or not self.portboard.strip():
            raise ValueError("stub version and portboard must be explicit")
        if self.source is StubSource.PATH and self.path is None:
            raise ValueError("path stub source requires a path")
        if self.source is not StubSource.PATH and self.path is not None:
            raise ValueError("stub path is only valid for path source")


@dataclass(frozen=True)
class QACase:
    stubs: StubSelection
    checkers: tuple[str, ...]

    def __post_init__(self) -> None:
        normalized = tuple(dict.fromkeys(checker.strip().casefold() for checker in self.checkers if checker.strip()))
        if not normalized:
            raise ValueError("at least one checker is required")
        object.__setattr__(self, "checkers", normalized)


@dataclass(frozen=True)
class QAMatrixPlan:
    cases: tuple[QACase, ...]
    disposition: RecordDisposition
    reason: ReasonCode | None = None


@dataclass(frozen=True)
class StubProvisionResult:
    command: tuple[str, ...]


class StubProvisioner(Protocol):
    def provision(self, selection: StubSelection, target: Path) -> StubProvisionResult: ...


@dataclass(frozen=True)
class CheckerExecution:
    command: tuple[str, ...]
    diagnostics: tuple[dict[str, object], ...]
    summary: Mapping[str, object]


class CheckerBackend(Protocol):
    def run(self, workspace: Path, *, checker: str, version: str, portboard: str) -> CheckerExecution: ...


@dataclass(frozen=True)
class QACheckerResult:
    checker: str
    command: tuple[str, ...]
    status: CheckerStatus
    diagnostics: tuple[dict[str, object], ...]
    error_count: int
    warning_count: int
    files_analyzed: int
    duration_seconds: float
    message: str = ""

    def to_dict(self) -> dict[str, object]:
        return {
            "checker": self.checker,
            "command": list(self.command),
            "status": self.status.value,
            "diagnostics": list(self.diagnostics),
            "error_count": self.error_count,
            "warning_count": self.warning_count,
            "files_analyzed": self.files_analyzed,
            "duration_seconds": self.duration_seconds,
            "message": self.message,
        }


@dataclass(frozen=True)
class QARunReport:
    package_identity: str
    provenance: tuple[dict[str, object], ...]
    requested_reference: str | None
    resolved_revision: str | None
    version: str
    portboard: str
    stub_source: StubSource
    stub_command: tuple[str, ...]
    results: tuple[QACheckerResult, ...]
    duration_seconds: float
    retained_workspace: Path | None
    package_version: str | None = None
    package_resolution: PackageResolution | None = None

    @property
    def status(self) -> CheckerStatus:
        statuses = {result.status for result in self.results}
        for status in (CheckerStatus.ERROR, CheckerStatus.FAIL, CheckerStatus.SKIP):
            if status in statuses:
                return status
        return CheckerStatus.PASS

    @property
    def provisioning_status(self) -> str:
        if self.stub_command:
            return "completed"
        if any(result.status is CheckerStatus.ERROR for result in self.results):
            return "error"
        return "not_run"

    def to_dict(self, *, include_resolution: bool = True) -> dict[str, object]:
        document: dict[str, object] = {
            "schema_version": REPORT_SCHEMA_VERSION,
            "package_identity": self.package_identity,
            "provenance": list(self.provenance),
            "requested_reference": self.requested_reference,
            "resolved_revision": self.resolved_revision,
            "package_version": self.package_version,
            "version": self.version,
            "portboard": self.portboard,
            "stub_source": self.stub_source.value,
            "stub_command": list(self.stub_command),
            "typings": {
                "status": self.provisioning_status,
                "version": self.version,
                "portboard": self.portboard,
                "source": self.stub_source.value,
                "command": list(self.stub_command),
            },
            "status": self.status.value,
            "results": [result.to_dict() for result in self.results],
            "duration_seconds": self.duration_seconds,
            "workspace_retained": self.retained_workspace is not None,
            "retained_workspace": str(self.retained_workspace) if self.retained_workspace is not None else None,
        }
        if include_resolution:
            document["resolution"] = resolution_to_dict(self.package_resolution) if self.package_resolution else None
        preserved_paths = (self.retained_workspace,) if self.retained_workspace is not None else ()
        return sanitize_report_document(document, preserved_paths=preserved_paths)

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2, sort_keys=True) + "\n"

    def render_text(self, *, include_resolution: bool = True) -> str:
        lines = [
            f"QA run report v{REPORT_SCHEMA_VERSION}: {self.package_identity} [{self.version} {self.portboard}] {self.status.value.upper()}"
        ]
        if include_resolution:
            if self.package_resolution is None:
                lines.append("  resolution: not available")
            else:
                lines.extend(resolution_text(self.package_resolution, indent="  "))
        lines.append(f"  typings: {self.stub_source.value} {self.provisioning_status}")
        if self.stub_command:
            lines.append(f"    command: {' '.join(sanitize_report_command(self.stub_command))}")
        for result in self.results:
            lines.append(
                f"  {result.checker}: {result.status.value.upper()} "
                f"({result.error_count} errors, {result.warning_count} warnings, {result.duration_seconds:.3f}s)"
            )
            if result.command:
                lines.append(f"    command: {' '.join(sanitize_report_command(result.command))}")
            if result.message:
                lines.append(f"    {result.message.strip()}")
            if result.status in {CheckerStatus.FAIL, CheckerStatus.ERROR}:
                lines.extend(f"    diagnostic: {_diagnostic_text(diagnostic)}" for diagnostic in result.diagnostics)
        workspace = str(self.retained_workspace) if self.retained_workspace is not None else "no"
        lines.append(f"  workspace retained: {workspace}")
        preserved_paths = (self.retained_workspace,) if self.retained_workspace is not None else ()
        return sanitize_report_text("\n".join(lines), preserved_paths=preserved_paths)


def plan_qa_matrix(
    record: PackageRecord,
    *,
    versions: Iterable[str],
    available_portboards: Iterable[str],
    stub_source: StubSource,
    checkers: Iterable[str],
    stub_path: Path | None = None,
    no_stub_cache: bool = False,
    unknown_policy: UnknownPortPolicy = UnknownPortPolicy.USE_REQUESTED,
) -> QAMatrixPlan:
    """Build a deterministic version/port matrix from package classification."""
    versions = tuple(sorted(set(versions)))
    requested_portboards = tuple(sorted(set(available_portboards)))
    checkers = tuple(dict.fromkeys(checker.strip().casefold() for checker in checkers if checker.strip()))
    if not versions or not requested_portboards or not checkers:
        raise ValueError("versions, available portboards, and checkers must not be empty")

    classification = record.classification
    if classification is None or classification.classification is PortClassification.UNKNOWN:
        if unknown_policy is UnknownPortPolicy.SKIP:
            reason = classification.reason if classification is not None else ReasonCode.NO_PORT_EVIDENCE
            return QAMatrixPlan((), RecordDisposition.SKIP, reason)
        selected_portboards = requested_portboards
    elif classification.classification is PortClassification.PORTABLE:
        selected_portboards = requested_portboards
    else:
        selected_portboards = tuple(
            portboard
            for portboard in requested_portboards
            if _matches_classification(portboard, classification.ports, classification.boards)
        )
        if not selected_portboards:
            return QAMatrixPlan((), RecordDisposition.SKIP, ReasonCode.NO_COMPATIBLE_PORT)

    cases = tuple(
        QACase(StubSelection(version, portboard, stub_source, stub_path, no_stub_cache), checkers)
        for version, portboard in product(versions, selected_portboards)
    )
    return QAMatrixPlan(cases, RecordDisposition.CHECK)


class UvStubProvisioner:
    """Provision selected stubs into a fresh workspace typings directory."""

    def __init__(self, project_root: Path) -> None:
        self.project_root = project_root.resolve()

    def provision(self, selection: StubSelection, target: Path) -> StubProvisionResult:
        if target.exists():
            shutil.rmtree(target)
        if selection.source is StubSource.PATH:
            assert selection.path is not None
            source = selection.path.resolve()
            if not source.is_dir():
                raise FileNotFoundError(f"Stub path does not exist: {source}")
            shutil.copytree(source, target)
            return StubProvisionResult(("copy", str(source), str(target)))

        command = self._install_command(selection, target)
        target.parent.mkdir(parents=True, exist_ok=True)
        try:
            subprocess.run(command, cwd=self.project_root, check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as error:
            raise RuntimeError(error.stderr or error.stdout or str(error)) from error
        self._copy_mpy_shed(target)
        return StubProvisionResult(tuple(command))

    def _install_command(self, selection: StubSelection, target: Path) -> list[str]:
        version = selection.version.lower().lstrip("v")
        if selection.source is StubSource.PYPI:
            packages = [f"micropython-{selection.portboard}-stubs=={version}.*"]
            options: list[str] = []
        elif selection.source is StubSource.PYPI_PRE:
            packages = [f"micropython-{selection.portboard}-stubs=={version}.*"]
            options = ["--pre"]
        elif selection.source is StubSource.LOCAL:
            if selection.version == "-":
                package_name = f"micropython-{selection.portboard}-stubs"
            else:
                package_name = f"micropython-{clean_version(selection.version, flat=True)}-{selection.portboard}-stubs"
            stdlib = self.project_root / "publish" / "micropython-stdlib-stubs"
            package = self.project_root / "publish" / package_name
            if not stdlib.is_dir() or not package.is_dir():
                raise FileNotFoundError(f"Local stub package is unavailable: {package}")
            packages = [str(stdlib), str(package)]
            options = ["--no-deps", "--pre"]
        else:
            raise ValueError(f"Unsupported stub source: {selection.source.value}")

        command = ["uv"]
        if selection.no_cache:
            command.append("--no-cache")
        command.extend(["pip", "install", *options, *packages, "--target", str(target)])
        return command

    def _copy_mpy_shed(self, target: Path) -> None:
        source = self.project_root / "reference" / "_mpy_shed"
        if source.is_dir():
            shutil.copytree(source, target / "_mpy_shed", dirs_exist_ok=True)


class ExistingCheckerBackend:
    """Adapter for the quality suite's existing normalized checker functions."""

    def run(self, workspace: Path, *, checker: str, version: str, portboard: str) -> CheckerExecution:
        report = invoke_typechecker(workspace, version, linter=checker)
        diagnostics_value = report.get("generalDiagnostics")
        summary_value = report.get("summary")
        if not isinstance(diagnostics_value, list) or not isinstance(summary_value, dict):
            raise RuntimeError(f"{checker} returned an invalid diagnostic report")
        diagnostics = [dict(item) for item in diagnostics_value if isinstance(item, dict)]
        diagnostics = filter_issues(diagnostics, version, portboard=portboard, linter=checker)
        return CheckerExecution(
            command=_checker_command(checker, workspace),
            diagnostics=tuple(_relative_diagnostic(item, workspace) for item in diagnostics),
            summary=dict(summary_value),
        )


class QARunner:
    def __init__(
        self,
        *,
        workspace_root: Path,
        config_root: Path,
        stub_provisioner: StubProvisioner,
        checker_backend: CheckerBackend,
    ) -> None:
        self.workspace_root = workspace_root
        self.config_root = config_root
        self.stub_provisioner = stub_provisioner
        self.checker_backend = checker_backend

    def run(
        self,
        resolution: ResolutionResult,
        case: QACase,
        *,
        retention: WorkspaceRetention = WorkspaceRetention.NEVER,
    ) -> QARunReport:
        started = time.perf_counter()
        record = resolution.record
        if record.disposition is not RecordDisposition.CHECK or record.resolution is None:
            results = tuple(
                QACheckerResult(
                    checker=checker,
                    command=(),
                    status=CheckerStatus.SKIP,
                    diagnostics=(),
                    error_count=0,
                    warning_count=0,
                    files_analyzed=0,
                    duration_seconds=0.0,
                    message=record.reason.value if record.reason else "package is not checkable",
                )
                for checker in case.checkers
            )
            return self._report(record, case, (), results, time.perf_counter() - started, None)

        self.workspace_root.mkdir(parents=True, exist_ok=True)
        workspace = Path(tempfile.mkdtemp(prefix="ecosystem-qa-", dir=self.workspace_root))
        stub_command: tuple[str, ...] = ()
        results: list[QACheckerResult] = []
        try:
            (workspace / "README.md").write_text(_workspace_readme(record), encoding="utf-8")
            self._prepare_workspace(workspace, resolution)
            stub_command = self.stub_provisioner.provision(case.stubs, workspace / "typings").command
            for checker in case.checkers:
                results.append(self._run_checker(workspace, checker, case.stubs))
        except Exception as error:
            completed = {result.checker for result in results}
            for checker in case.checkers:
                if checker in completed:
                    continue
                results.append(
                    QACheckerResult(
                        checker=checker,
                        command=(),
                        status=CheckerStatus.ERROR,
                        diagnostics=(),
                        error_count=0,
                        warning_count=0,
                        files_analyzed=0,
                        duration_seconds=0.0,
                        message=str(error),
                    )
                )

        failed = any(result.status in {CheckerStatus.FAIL, CheckerStatus.ERROR} for result in results)
        retain = retention is WorkspaceRetention.ALWAYS or (retention is WorkspaceRetention.ON_FAILURE and failed)
        retained_workspace = workspace.resolve() if retain else None
        if not retain:
            shutil.rmtree(workspace, ignore_errors=True)
        return self._report(
            record,
            case,
            stub_command,
            tuple(results),
            time.perf_counter() - started,
            retained_workspace,
        )

    def _prepare_workspace(self, workspace: Path, resolution: ResolutionResult) -> None:
        source_root = workspace / "source"
        source_root.mkdir()
        python_payloads = [payload for payload in resolution.payloads if payload.file.kind is FileKind.PYTHON]
        if not python_payloads:
            raise ValueError("resolved package has no Python payload")
        for payload in python_payloads:
            target = _safe_workspace_target(source_root, payload.file.target)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(payload.data)

        for config in self.config_root.iterdir():
            if config.is_file() and config.name.casefold() != "readme.md":
                shutil.copy2(config, workspace / config.name)
        config_path = workspace / "pyproject.toml"
        if not config_path.is_file():
            raise FileNotFoundError(f"Checker configuration is missing: {config_path}")
        config_text = config_path.read_text(encoding="utf-8")
        config_text = config_text.replace('include = ["."]', 'include = ["source"]')
        config_text = config_text.replace('files = "*.py"', 'files = ["source/**/*.py"]')
        config_text = config_text.replace('project-includes = ["**/*.py"]', 'project-includes = ["source/**/*.py"]')
        config_path.write_text(config_text, encoding="utf-8")

    def _run_checker(self, workspace: Path, checker: str, stubs: StubSelection) -> QACheckerResult:
        started = time.perf_counter()
        execution = self.checker_backend.run(
            workspace,
            checker=checker,
            version=stubs.version,
            portboard=stubs.portboard,
        )
        diagnostics = tuple(_relative_diagnostic(item, workspace) for item in execution.diagnostics)
        error_count = sum(item.get("severity") == "error" for item in diagnostics)
        warning_count = sum(item.get("severity") == "warning" for item in diagnostics)
        files_analyzed = _integer_summary(execution.summary, "filesAnalyzed")
        return QACheckerResult(
            checker=checker,
            command=execution.command,
            status=CheckerStatus.FAIL if error_count else CheckerStatus.PASS,
            diagnostics=diagnostics,
            error_count=error_count,
            warning_count=warning_count,
            files_analyzed=files_analyzed,
            duration_seconds=time.perf_counter() - started,
        )

    def _report(
        self,
        record: PackageRecord,
        case: QACase,
        stub_command: tuple[str, ...],
        results: tuple[QACheckerResult, ...],
        duration: float,
        retained_workspace: Path | None,
    ) -> QARunReport:
        resolution = record.resolution
        provenance = tuple(
            {
                "catalog": item.catalog.value,
                "entry_url": item.entry_url,
                "entry_key": item.entry_key,
                "observed_at": item.observed_at,
                "metadata": dict(item.metadata),
            }
            for item in record.candidate.provenance
        )
        return QARunReport(
            package_identity=record.candidate.identity.key,
            provenance=provenance,
            requested_reference=resolution.requested_reference if resolution else None,
            resolved_revision=resolution.resolved_revision if resolution else None,
            version=case.stubs.version,
            portboard=case.stubs.portboard,
            stub_source=case.stubs.source,
            stub_command=stub_command,
            results=results,
            duration_seconds=duration,
            retained_workspace=retained_workspace,
            package_version=resolution.package_version if resolution else None,
            package_resolution=resolution,
        )


def _matches_classification(portboard: str, ports: tuple[str, ...], boards: tuple[str, ...]) -> bool:
    port, separator, board = portboard.casefold().partition("-")
    return portboard.casefold() in ports or port in ports or (separator and (board in boards or portboard.casefold() in boards))


def _workspace_readme(record: PackageRecord) -> str:
    resolution = record.resolution
    generated_at = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    source_reference = resolution.canonical_reference if resolution is not None else record.candidate.install_reference
    resolved_revision = resolution.resolved_revision if resolution is not None else None
    lines = [
        "# Ecosystem QA workspace",
        "",
        f"- Generated (UTC): `{generated_at}`",
        f"- Package: `{record.candidate.identity.key}`",
        f"- Source reference: `{source_reference}`",
    ]
    repository_url = _repository_url(record) or "not determined"
    lines.append(f"- Source repository: {repository_url}")
    lines.extend(
        (
            f"- Resolved revision: `{resolved_revision or '-'}`",
            "",
            "## Index provenance",
            "",
        )
    )
    for item in record.candidate.provenance:
        observed = f" (observed `{item.observed_at}`)" if item.observed_at else ""
        lines.append(f"- `{item.catalog.value}`: {item.entry_url}{observed}")
    return sanitize_report_text("\n".join(lines)) + "\n"


def _repository_url(record: PackageRecord) -> str | None:
    identity = record.candidate.identity
    if identity.kind is not IdentityKind.REPOSITORY:
        return None
    provider, separator, location = identity.value.partition(":")
    root = _REPOSITORY_WEB_ROOTS.get(provider)
    parts = location.split("/")
    if not separator or root is None or len(parts) < 2:
        return None
    return f"{root}/{parts[0]}/{parts[1]}"


def _safe_workspace_target(root: Path, target: str) -> Path:
    parts = PurePosixPath(target).parts
    destination = root.joinpath(*parts)
    try:
        destination.resolve().relative_to(root.resolve())
    except ValueError as error:
        raise ValueError(f"Package target escapes QA workspace: {target}") from error
    return destination


def _checker_command(checker: str, workspace: Path) -> tuple[str, ...]:
    commands = {
        "pyright": (sys.executable, "-m", "pyright", "--project", str(workspace), "--outputjson"),
        "mypy": (sys.executable, "-m", "mypy", "--warn-unused-ignores", "--no-error-summary", "."),
        "ruff": (sys.executable, "-m", "ruff", "check", "--output-format=json", "."),
        "pyrefly": (sys.executable, "-m", "pyrefly", "check", "--output-format=json"),
        "ty": (sys.executable, "-m", "ty", "check"),
        "zuban": ("zuban", "check", "."),
    }
    try:
        return commands[checker]
    except KeyError as error:
        raise NotImplementedError(f"Unknown checker {checker}") from error


def _relative_diagnostic(diagnostic: dict[str, object], workspace: Path) -> dict[str, object]:
    normalized = dict(diagnostic)
    file_value = normalized.get("file")
    if isinstance(file_value, str):
        try:
            normalized["file"] = Path(file_value).resolve().relative_to(workspace.resolve()).as_posix()
        except ValueError:
            normalized["file"] = file_value
    return normalized


def _diagnostic_text(diagnostic: Mapping[str, object]) -> str:
    file_name = " ".join(str(diagnostic.get("file") or "<unknown>").split())
    location = file_name
    range_value = diagnostic.get("range")
    if isinstance(range_value, Mapping):
        start = range_value.get("start")
        if isinstance(start, Mapping):
            line = start.get("line")
            character = start.get("character")
            if isinstance(line, int) and not isinstance(line, bool) and line >= 0:
                location += f":{line + 1}"
                if isinstance(character, int) and not isinstance(character, bool) and character >= 0:
                    location += f":{character + 1}"
    severity = " ".join(str(diagnostic.get("severity") or "unknown").split())
    message = " ".join(str(diagnostic.get("message") or "(no message)").split())
    return f"{location}: {severity}: {message}"


def _integer_summary(summary: Mapping[str, object], key: str) -> int:
    value = summary.get(key, 0)
    return value if isinstance(value, int) else 0
