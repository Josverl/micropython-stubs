"""Build the optional Markdown summary for checker-parametrized tests."""

from __future__ import annotations

import hashlib
import html
import json
import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

_PROPERTY_PREFIX = "markdown_report_"
_STATUS_PRECEDENCE = {"PASS": 1, "SKIP": 2, "XFAIL": 3, "XPASS": 4, "FAIL": 5}
_STATUS_COLORS = {
    "PASS": "#1a7f37",
    "FAIL": "#cf222e",
    "SKIP": "#6e7781",
    "XFAIL": "#9a6700",
    "XPASS": "#8250df",
}
_PREFERRED_ROW_PARAMS = ("version", "portboard", "feature")


@dataclass
class ReportCell:
    status: str
    diagnostic: str = ""


@dataclass
class ReportRow:
    test_id: str
    test_name: str
    values: tuple[str, ...]
    cells: dict[str, ReportCell]


def add_report_metadata(item: Any, call: Any, report: Any) -> None:
    """Attach xdist-serializable checker metadata to a pytest report."""
    callspec = getattr(item, "callspec", None)
    params = getattr(callspec, "params", {})
    if "linter" not in params:
        return

    excluded = {"stub_source", "linter", *_PREFERRED_ROW_PARAMS}
    row_names = [name for name in _PREFERRED_ROW_PARAMS if name in params]
    row_names.extend(name for name in params if name not in excluded)
    row_values = [str(params[name]) for name in row_names]
    base_nodeid = item.nodeid.split("[", 1)[0]
    test_name = base_nodeid.rsplit("::", 1)[-1]

    properties = {
        "checker": str(params["linter"]),
        "test_id": json.dumps([base_nodeid, row_names, row_values]),
        "test_name": test_name,
        "row_values": json.dumps(row_values),
    }

    if call.excinfo is not None:
        diagnostic_parts = [str(call.excinfo.value).strip()]
        caplog = getattr(item, "funcargs", {}).get("caplog")
        if caplog is not None:
            log_messages = [record.message for record in caplog.records if record.levelno >= logging.WARNING]
            if log_messages:
                diagnostic_parts.append("\n".join(log_messages))
        properties["diagnostic"] = "\n\n".join(part for part in diagnostic_parts if part)

    for name, value in properties.items():
        report.user_properties.append((f"{_PROPERTY_PREFIX}{name}", value))


def render_markdown(reports: Iterable[Any]) -> str:
    """Render checker reports as a Markdown table and linked diagnostics."""
    rows = _aggregate_reports(reports)
    if not rows:
        return "# Type checker test report\n\nNo checker-parametrized tests were run.\n"

    checkers = sorted({checker for row in rows.values() for checker in row.cells}, key=str.casefold)
    sorted_rows = sorted(rows.values(), key=lambda row: (tuple(value.casefold() for value in row.values), row.test_id))
    labels = _display_labels(sorted_rows)

    lines = [
        "# Type checker test report",
        "",
        "| Test | " + " | ".join(_escape_markdown(checker) for checker in checkers) + " |",
        "| --- | " + " | ".join("---" for _ in checkers) + " |",
    ]

    details: list[tuple[str, ReportRow, str, ReportCell]] = []
    for row in sorted_rows:
        cells = []
        for checker in checkers:
            cell = row.cells.get(checker)
            if cell is None:
                cells.append("-")
                continue
            anchor = _detail_anchor(row.test_id, checker)
            cells.append(_status_html(cell.status, anchor if cell.status in {"FAIL", "XFAIL"} else None))
            if cell.status in {"FAIL", "XFAIL"}:
                details.append((checker, row, anchor, cell))
        lines.append(f"| {_escape_markdown(labels[row.test_id])} | " + " | ".join(cells) + " |")

    if details:
        lines.extend(["", "## Failures and expected failures"])
        for checker in checkers:
            checker_details = [detail for detail in details if detail[0] == checker]
            if not checker_details:
                continue
            lines.extend(["", f"### {_escape_markdown(checker)}"])
            for _, row, anchor, cell in checker_details:
                lines.extend(
                    [
                        "",
                        f'<a id="{anchor}"></a>',
                        f"#### {_escape_markdown(labels[row.test_id])} - {cell.status}",
                        "",
                        _fenced_text(
                            cell.diagnostic or "No checker diagnostic was captured; the test failed before checker output was available."
                        ),
                    ]
                )

    return "\n".join(lines) + "\n"


def write_markdown_report(terminalreporter: Any, output_path: Path) -> None:
    """Write reports collected by pytest's controller-side terminal reporter."""
    reports = []
    seen = set()
    for status_reports in terminalreporter.stats.values():
        for report in status_reports:
            identity = id(report)
            if identity not in seen:
                seen.add(identity)
                reports.append(report)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_markdown(reports), encoding="utf-8")


def _aggregate_reports(reports: Iterable[Any]) -> dict[str, ReportRow]:
    rows: dict[str, ReportRow] = {}
    for report in reports:
        properties = dict(getattr(report, "user_properties", []))
        checker = properties.get(f"{_PROPERTY_PREFIX}checker")
        test_id = properties.get(f"{_PROPERTY_PREFIX}test_id")
        if not checker or not test_id:
            continue

        status = _report_status(report)
        if status is None:
            continue

        row = rows.setdefault(
            test_id,
            ReportRow(
                test_id=test_id,
                test_name=properties[f"{_PROPERTY_PREFIX}test_name"],
                values=tuple(json.loads(properties[f"{_PROPERTY_PREFIX}row_values"])),
                cells={},
            ),
        )
        diagnostic = properties.get(f"{_PROPERTY_PREFIX}diagnostic", "")
        current = row.cells.get(checker)
        if current is None or _STATUS_PRECEDENCE[status] > _STATUS_PRECEDENCE[current.status]:
            row.cells[checker] = ReportCell(status=status, diagnostic=diagnostic)
        elif status == current.status and diagnostic and not current.diagnostic:
            current.diagnostic = diagnostic
    return rows


def _report_status(report: Any) -> str | None:
    wasxfail = getattr(report, "wasxfail", None)
    if report.when == "call":
        if wasxfail:
            return "XFAIL" if report.skipped else "XPASS"
        if report.failed:
            return "FAIL"
        if report.skipped:
            return "SKIP"
        if report.passed:
            return "PASS"
    elif report.failed:
        return "FAIL"
    elif report.skipped:
        return "SKIP"
    return None


def _display_labels(rows: list[ReportRow]) -> dict[str, str]:
    base_labels = {row.test_id: " ".join(row.values) or row.test_name for row in rows}
    label_counts: dict[str, int] = {}
    for label in base_labels.values():
        label_counts[label] = label_counts.get(label, 0) + 1
    return {
        row.test_id: f"{base_labels[row.test_id]} ({row.test_name})"
        if label_counts[base_labels[row.test_id]] > 1
        else base_labels[row.test_id]
        for row in rows
    }


def _status_html(status: str, anchor: str | None) -> str:
    span = f'<span style="color: {_STATUS_COLORS[status]}; font-weight: 600">{status}</span>'
    return f'<a href="#{anchor}">{span}</a>' if anchor else span


def _detail_anchor(test_id: str, checker: str) -> str:
    digest = hashlib.sha1(f"{test_id}\0{checker}".encode(), usedforsecurity=False).hexdigest()[:12]
    checker_slug = re.sub(r"[^a-z0-9]+", "-", checker.casefold()).strip("-") or "checker"
    return f"typecheck-detail-{checker_slug}-{digest}"


def _escape_markdown(value: str) -> str:
    return html.escape(value, quote=False).replace("|", "\\|").replace("\n", "<br>")


def _fenced_text(value: str) -> str:
    longest_run = max((len(match.group(0)) for match in re.finditer(r"`+", value)), default=0)
    fence = "`" * max(3, longest_run + 1)
    return f"{fence}text\n{value.rstrip()}\n{fence}"
