"""Render ecosystem QA JSON documents as Markdown overview and checker reports."""

from __future__ import annotations

import hashlib
import html
import re
from collections import Counter
from collections.abc import Mapping, Sequence
from dataclasses import dataclass

from packaging.version import InvalidVersion, Version

_STATUS_COLORS = {
    "PASS": "#1a7f37",
    "FAIL": "#cf222e",
    "SKIP": "#6e7781",
    "ERROR": "#cf222e",
}


@dataclass(frozen=True)
class EcosystemMarkdownReports:
    overview: str
    checker_details: dict[str, str]
    detail_filenames: dict[str, str]


@dataclass(frozen=True)
class _CheckerRun:
    key: str
    package: str
    version: str
    portboard: str
    checker: str
    status: str
    command: tuple[str, ...]
    diagnostics: tuple[Mapping[str, object], ...]
    error_count: int
    warning_count: int
    files_analyzed: int
    message: str

    @property
    def anchor(self) -> str:
        digest = hashlib.sha1(f"{self.key}\0{self.checker}".encode(), usedforsecurity=False).hexdigest()[:12]
        checker_slug = _slug(self.checker)
        return f"ecosystem-detail-{checker_slug}-{digest}"

    @property
    def has_detail(self) -> bool:
        return bool(self.diagnostics or self.message or self.status in {"FAIL", "ERROR"})


@dataclass(frozen=True)
class _ReportRow:
    key: str
    package: str
    version: str
    portboard: str
    outcome: str
    run_number: int | None
    checkers: Mapping[str, _CheckerRun]


def render_markdown_reports(
    document: Mapping[str, object],
    *,
    overview_filename: str = "ecosystem.md",
) -> EcosystemMarkdownReports:
    """Render one ecosystem report or aggregate document without filesystem access."""
    rows, requested_checkers = _collect_rows(document)
    checkers = sorted(requested_checkers | {checker for row in rows for checker in row.checkers}, key=str.casefold)
    detail_filenames = _detail_filenames(checkers, overview_filename)
    overview = _render_overview(document, rows, checkers, detail_filenames)
    details = {checker: _render_checker_detail(checker, rows, overview_filename) for checker in checkers}
    return EcosystemMarkdownReports(overview, details, detail_filenames)


def _collect_rows(document: Mapping[str, object]) -> tuple[list[_ReportRow], set[str]]:
    rows: list[_ReportRow] = []
    requested_checkers: set[str] = set()
    report_documents = _report_documents(document)
    aggregate = len(report_documents) > 1 or document.get("report_type") == "ecosystem_qa_aggregate"

    for run_number, report_document in report_documents:
        matrix = _mapping(report_document.get("qa_matrix"))
        requested_checkers.update(_strings(matrix.get("checkers")))
        for package_index, package_result in enumerate(_mappings(report_document.get("results"))):
            package = str(package_result.get("package_identity") or package_result.get("package_reference") or "unknown package")
            outcome = str(package_result.get("outcome") or "unknown")
            qa_reports = _mappings(package_result.get("reports"))
            if not qa_reports:
                rows.append(
                    _ReportRow(
                        key=f"{run_number}:{package_index}:none",
                        package=package,
                        version="",
                        portboard="",
                        outcome=outcome,
                        run_number=run_number if aggregate else None,
                        checkers={},
                    )
                )
                continue

            for report_index, qa_report in enumerate(qa_reports):
                version = str(qa_report.get("version") or "")
                portboard = str(qa_report.get("portboard") or "")
                row_key = f"{run_number}:{package_index}:{report_index}"
                checker_runs: dict[str, _CheckerRun] = {}
                for checker_result in _mappings(qa_report.get("results")):
                    checker = str(checker_result.get("checker") or "").strip()
                    if not checker:
                        continue
                    requested_checkers.add(checker)
                    checker_runs[checker] = _CheckerRun(
                        key=row_key,
                        package=package,
                        version=version,
                        portboard=portboard,
                        checker=checker,
                        status=str(checker_result.get("status") or "error").upper(),
                        command=_strings(checker_result.get("command")),
                        diagnostics=_mappings(checker_result.get("diagnostics")),
                        error_count=_integer(checker_result.get("error_count")),
                        warning_count=_integer(checker_result.get("warning_count")),
                        files_analyzed=_integer(checker_result.get("files_analyzed")),
                        message=str(checker_result.get("message") or ""),
                    )
                rows.append(
                    _ReportRow(
                        key=row_key,
                        package=package,
                        version=version,
                        portboard=portboard,
                        outcome=outcome,
                        run_number=run_number if aggregate else None,
                        checkers=checker_runs,
                    )
                )
    return rows, requested_checkers


def _render_overview(
    document: Mapping[str, object],
    rows: list[_ReportRow],
    checkers: list[str],
    detail_filenames: Mapping[str, str],
) -> str:
    report_documents = _report_documents(document)
    counts = _outcome_counts(document, report_documents)
    duration = sum(_number(item.get("duration_seconds")) for _, item in report_documents)
    mode = "aggregate" if document.get("report_type") == "ecosystem_qa_aggregate" else str(document.get("mode") or "unknown")
    checker_links = ", ".join(
        f"[{_escape_markdown(checker)}]({html.escape(detail_filenames[checker], quote=True)})" for checker in checkers
    )
    lines = [
        "# Ecosystem type checker report",
        "",
        "This report summarizes MicroPython ecosystem packages against the selected stub and type checker matrix.",
        "",
        "## Run summary",
        "",
        "| Metric | Value |",
        "| --- | --- |",
        f"| Mode | {_escape_markdown(mode)} |",
        f"| Runs | {len(report_documents)} |",
        f"| Package results | {sum(counts.values())} |",
        f"| Checker runs | {sum(len(row.checkers) for row in rows)} |",
        f"| Checkers | {_escape_markdown(', '.join(checkers) or 'none')} |",
        f"| Checker reports | {checker_links or 'none'} |",
        f"| Exit code | {_integer(document.get('exit_code'))} |",
        f"| Duration | {duration:.3f}s |",
        "",
        "## Package outcomes",
        "",
        "| Outcome | Count |",
        "| --- | ---: |",
    ]
    lines.extend(f"| {_escape_markdown(outcome)} | {count} |" for outcome, count in sorted(counts.items()))

    for version_label, group_rows in _version_groups(rows):
        lines.extend(
            [
                "",
                f"## {_escape_markdown(version_label)}",
                "",
                "| Package | Target | Outcome | " + " | ".join(_escape_markdown(checker) for checker in checkers) + " |",
                "| --- | --- | --- | " + " | ".join("---" for _ in checkers) + " |",
            ]
        )
        for row in group_rows:
            package = f"{row.package} (run {row.run_number})" if row.run_number is not None else row.package
            cells = [_checker_cell(row.checkers.get(checker), detail_filenames[checker]) for checker in checkers]
            lines.append(
                f"| {_escape_markdown(package)} | {_escape_markdown(row.portboard or '-')} | "
                f"{_escape_markdown(row.outcome)} | " + " | ".join(cells) + " |"
            )
    return "\n".join(lines) + "\n"


def _render_checker_detail(checker: str, rows: list[_ReportRow], overview_filename: str) -> str:
    checker_runs = [row.checkers[checker] for row in rows if checker in row.checkers]
    status_counts = Counter(run.status for run in checker_runs)
    lines = [
        f"# {_escape_markdown(checker)} ecosystem diagnostics",
        "",
        f"[Back to ecosystem type checker report]({_escape_markdown(overview_filename)})",
        "",
        "## Summary",
        "",
        "| Metric | Value |",
        "| --- | ---: |",
        f"| Runs | {len(checker_runs)} |",
        f"| Passed | {status_counts['PASS']} |",
        f"| Failed | {status_counts['FAIL']} |",
        f"| Errors | {status_counts['ERROR']} |",
        f"| Skipped | {status_counts['SKIP']} |",
        f"| Error diagnostics | {sum(run.error_count for run in checker_runs)} |",
        f"| Warning diagnostics | {sum(run.warning_count for run in checker_runs)} |",
        f"| Files analyzed | {sum(run.files_analyzed for run in checker_runs)} |",
        "",
        "## Runs",
        "",
    ]
    if checker_runs:
        lines.extend(
            [
                "| Package | Version | Target | Status | Errors | Warnings | Files |",
                "| --- | --- | --- | --- | ---: | ---: | ---: |",
            ]
        )
        for run in checker_runs:
            status = _status_html(run.status)
            if run.has_detail:
                status = f'<a href="#{run.anchor}">{status}</a>'
            lines.append(
                f"| {_escape_markdown(run.package)} | {_escape_markdown(run.version or '-')} | "
                f"{_escape_markdown(run.portboard or '-')} | {status} | {run.error_count} | "
                f"{run.warning_count} | {run.files_analyzed} |"
            )
    else:
        lines.append("No checker runs were captured.")

    detailed_runs = [run for run in checker_runs if run.has_detail]
    diagnostic_lines = {run.key: tuple(_diagnostic_text(item) for item in run.diagnostics) for run in detailed_runs}
    occurrence_counts = Counter(line for lines_for_run in diagnostic_lines.values() for line in set(lines_for_run))
    shared_diagnostics = {line: count for line, count in occurrence_counts.items() if count > 1}

    for run in detailed_runs:
        lines.extend(
            [
                "",
                f'<a id="{run.anchor}"></a>',
                f"## {_escape_markdown(run.package)} - {run.status}",
                "",
                f"**Run specification:** `{_escape_markdown(run.version or '-')} {_escape_markdown(run.portboard or '-')}`",
                "",
                f"**Summary:** {run.error_count} errors, {run.warning_count} warnings, {run.files_analyzed} files analyzed",
            ]
        )
        if run.command:
            lines.extend(["", f"**Command:** `{_escape_markdown(_display_command(run.command))}`"])
        if run.message:
            lines.extend(["", "**Execution message:**", "", _fenced_text(run.message)])
        unique_diagnostics = [line for line in diagnostic_lines[run.key] if line not in shared_diagnostics]
        if run.diagnostics:
            lines.extend(
                [
                    "",
                    "**Diagnostics:**",
                    "",
                    _fenced_text("\n".join(unique_diagnostics) or "No unique checker diagnostic was captured."),
                ]
            )
        shared_count = sum(line in shared_diagnostics for line in diagnostic_lines[run.key])
        if shared_count:
            noun = "diagnostic" if shared_count == 1 else "diagnostics"
            lines.extend(["", f"{shared_count} shared {noun} omitted; see [Shared diagnostics](#shared-diagnostics)."])

    if shared_diagnostics:
        shared_lines = [f"{line} (Reported by {count} runs)" for line, count in sorted(shared_diagnostics.items())]
        lines.extend(["", "## Shared diagnostics", "", _fenced_text("\n".join(shared_lines))])
    elif checker_runs and not detailed_runs:
        lines.extend(["", "No diagnostics were reported."])
    return "\n".join(lines) + "\n"


def _checker_cell(run: _CheckerRun | None, detail_filename: str) -> str:
    if run is None:
        return "-"
    status = _status_html(run.status)
    if not run.has_detail:
        return status
    return f'<a href="{html.escape(detail_filename, quote=True)}#{run.anchor}">{status}</a>'


def _status_html(status: str) -> str:
    color = _STATUS_COLORS.get(status, _STATUS_COLORS["ERROR"])
    return f'<span style="color: {color}; font-weight: 600">{html.escape(status)}</span>'


def _diagnostic_text(diagnostic: Mapping[str, object]) -> str:
    start = _mapping(_mapping(diagnostic.get("range")).get("start"))
    line = _integer(start.get("line")) + 1
    character = _integer(start.get("character")) + 1
    severity = str(diagnostic.get("severity") or "error")
    rule = str(diagnostic.get("rule") or "")
    rule_text = f" [{rule}]" if rule else ""
    return f'"{diagnostic.get("file") or "<unknown>"}"({line},{character}): {severity}{rule_text}: {diagnostic.get("message") or ""}'


def _version_groups(rows: Sequence[_ReportRow]) -> list[tuple[str, list[_ReportRow]]]:
    unversioned: list[_ReportRow] = []
    parsed: dict[Version, list[_ReportRow]] = {}
    labels: dict[Version, str] = {}
    unparsed: dict[str, list[_ReportRow]] = {}
    for row in rows:
        version = row.version.strip()
        if not version or version == "-":
            unversioned.append(row)
            continue
        try:
            parsed_version = Version(version)
        except InvalidVersion:
            unparsed.setdefault(version, []).append(row)
        else:
            parsed.setdefault(parsed_version, []).append(row)
            labels.setdefault(parsed_version, version.removeprefix("v"))

    groups: list[tuple[str, list[_ReportRow]]] = []
    if unversioned:
        groups.append(("not checked / no version", _sort_rows(unversioned)))
    groups.extend((labels[version], _sort_rows(parsed[version])) for version in sorted(parsed, reverse=True))
    groups.extend((version, _sort_rows(unparsed[version])) for version in sorted(unparsed, key=str.casefold))
    return groups


def _sort_rows(rows: Sequence[_ReportRow]) -> list[_ReportRow]:
    return sorted(rows, key=lambda row: (row.package.casefold(), row.portboard.casefold(), row.key))


def _report_documents(document: Mapping[str, object]) -> tuple[tuple[int, Mapping[str, object]], ...]:
    if document.get("report_type") == "ecosystem_qa_aggregate":
        return tuple(enumerate(_mappings(document.get("runs")), start=1))
    return ((1, document),)


def _outcome_counts(
    document: Mapping[str, object],
    report_documents: Sequence[tuple[int, Mapping[str, object]]],
) -> dict[str, int]:
    counts = _mapping(document.get("counts"))
    if counts:
        return {str(name): _integer(value) for name, value in counts.items()}
    combined: Counter[str] = Counter()
    for _, report_document in report_documents:
        combined.update({str(name): _integer(value) for name, value in _mapping(report_document.get("counts")).items()})
    return dict(combined)


def _detail_filenames(checkers: Sequence[str], overview_filename: str) -> dict[str, str]:
    stem, separator, suffix = overview_filename.rpartition(".")
    if not separator:
        stem, suffix = overview_filename, "md"
    filenames: dict[str, str] = {}
    used: set[str] = set()
    for checker in checkers:
        slug = _slug(checker)
        filename = f"{stem}_{slug}.{suffix}"
        if filename in used:
            digest = hashlib.sha1(checker.encode(), usedforsecurity=False).hexdigest()[:8]
            filename = f"{stem}_{slug}_{digest}.{suffix}"
        filenames[checker] = filename
        used.add(filename)
    return filenames


def _slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.casefold()).strip("_") or "checker"


def _mapping(value: object) -> Mapping[str, object]:
    return value if isinstance(value, Mapping) else {}


def _mappings(value: object) -> tuple[Mapping[str, object], ...]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes)):
        return ()
    return tuple(item for item in value if isinstance(item, Mapping))


def _strings(value: object) -> tuple[str, ...]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes)):
        return ()
    return tuple(str(item) for item in value)


def _display_command(command: Sequence[str]) -> str:
    if len(command) >= 3 and command[1] == "-m":
        command = command[2:]
    return " ".join(command)


def _integer(value: object) -> int:
    return value if isinstance(value, int) and not isinstance(value, bool) else 0


def _number(value: object) -> float:
    return float(value) if isinstance(value, (int, float)) and not isinstance(value, bool) else 0.0


def _escape_markdown(value: str) -> str:
    return html.escape(value, quote=False).replace("|", "\\|").replace("\n", "<br>")


def _fenced_text(value: str) -> str:
    longest_run = max((len(match.group(0)) for match in re.finditer(r"`+", value)), default=0)
    fence = "`" * max(3, longest_run + 1)
    return f"{fence}text\n{value.rstrip()}\n{fence}"
