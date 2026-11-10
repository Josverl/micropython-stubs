"""Validated cumulative reports for repeated ecosystem QA invocations."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
import json
from pathlib import Path

from .reporting import REPORT_SCHEMA_VERSION

AGGREGATE_SCHEMA_VERSION = 1
AGGREGATE_REPORT_TYPE = "ecosystem_qa_aggregate"
OUTCOME_NAMES = ("pass", "type_check_failure", "unsupported", "unavailable", "skipped", "error")


@dataclass(frozen=True)
class AggregateReport:
    runs: tuple[dict[str, object], ...] = ()

    @classmethod
    def from_path(cls, path: Path) -> AggregateReport:
        try:
            document = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            raise ValueError(f"Aggregate report file {path} must contain valid JSON: {error.msg}") from error
        if not isinstance(document, dict):
            raise ValueError(f"Aggregate report file {path} must contain a JSON object")
        if document.get("report_type") == AGGREGATE_REPORT_TYPE:
            return cls.from_dict(document)
        if document.get("schema_version") == REPORT_SCHEMA_VERSION:
            return cls((_validated_run(document, context=f"Report file {path}"),))
        raise ValueError(f"Aggregate report file {path} must contain a compatible ecosystem QA report or aggregate")

    @classmethod
    def from_dict(cls, document: dict[str, object]) -> AggregateReport:
        if document.get("schema_version") != AGGREGATE_SCHEMA_VERSION:
            raise ValueError(f"Aggregate report requires schema_version {AGGREGATE_SCHEMA_VERSION}")
        if document.get("report_type") != AGGREGATE_REPORT_TYPE:
            raise ValueError(f"Aggregate report requires report_type {AGGREGATE_REPORT_TYPE!r}")
        if document.get("run_schema_version") != REPORT_SCHEMA_VERSION:
            raise ValueError(f"Aggregate report requires run_schema_version {REPORT_SCHEMA_VERSION}")
        runs_value = document.get("runs")
        if not isinstance(runs_value, list) or not runs_value:
            raise ValueError("Aggregate report runs must be a non-empty list")
        runs = tuple(_validated_run(run, context=f"Aggregate run {index}") for index, run in enumerate(runs_value, start=1))
        aggregate = cls(runs)
        expected = aggregate.to_dict()
        for key in ("run_count", "counts", "exit_code"):
            if document.get(key) != expected[key]:
                raise ValueError(f"Aggregate report {key} does not match its runs")
        return aggregate

    @property
    def counts(self) -> dict[str, int]:
        return {name: sum(_run_counts(run)[name] for run in self.runs) for name in OUTCOME_NAMES}

    @property
    def exit_code(self) -> int:
        return max((_integer(run.get("exit_code"), "run exit_code") for run in self.runs), default=0)

    def append(self, run: dict[str, object]) -> AggregateReport:
        return AggregateReport((*self.runs, _validated_run(run, context="New report")))

    def to_dict(self) -> dict[str, object]:
        return {
            "schema_version": AGGREGATE_SCHEMA_VERSION,
            "report_type": AGGREGATE_REPORT_TYPE,
            "run_schema_version": REPORT_SCHEMA_VERSION,
            "run_count": len(self.runs),
            "counts": self.counts,
            "exit_code": self.exit_code,
            "runs": [deepcopy(run) for run in self.runs],
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2, sort_keys=True) + "\n"


def _validated_run(value: object, *, context: str) -> dict[str, object]:
    if not isinstance(value, dict):
        raise ValueError(f"{context} must be a JSON object")
    if value.get("schema_version") != REPORT_SCHEMA_VERSION:
        raise ValueError(f"{context} requires schema_version {REPORT_SCHEMA_VERSION}")
    if value.get("mode") not in {"focused", "batch"}:
        raise ValueError(f"{context} has an invalid mode")
    results = value.get("results")
    if not isinstance(results, list):
        raise ValueError(f"{context} results must be a list")
    expected_counts = dict.fromkeys(OUTCOME_NAMES, 0)
    for index, result in enumerate(results, start=1):
        if not isinstance(result, dict) or result.get("outcome") not in expected_counts:
            raise ValueError(f"{context} result {index} has an invalid outcome")
        outcome = result["outcome"]
        assert isinstance(outcome, str)
        expected_counts[outcome] += 1
    counts = _run_counts(value)
    if counts != expected_counts:
        raise ValueError(f"{context} counts do not match its results")
    exit_code = _integer(value.get("exit_code"), f"{context} exit_code")
    if exit_code not in {0, 1, 2}:
        raise ValueError(f"{context} exit_code must be 0, 1, or 2")
    catalog_diagnostics = value.get("catalog_diagnostics")
    if not isinstance(catalog_diagnostics, list):
        raise ValueError(f"{context} catalog_diagnostics must be a list")
    outcomes = {result["outcome"] for result in results if isinstance(result, dict)}
    has_catalog_errors = any(isinstance(item, dict) and item.get("disposition") == "error" for item in catalog_diagnostics)
    if not outcomes or has_catalog_errors or outcomes & {"unsupported", "unavailable", "error"}:
        expected_exit = 2
    elif "type_check_failure" in outcomes:
        expected_exit = 1
    else:
        expected_exit = 0
    if exit_code != expected_exit:
        raise ValueError(f"{context} exit_code does not match its results")
    return deepcopy(value)


def _run_counts(run: dict[str, object]) -> dict[str, int]:
    value = run.get("counts")
    if not isinstance(value, dict) or set(value) != set(OUTCOME_NAMES):
        raise ValueError("Run counts must contain every ecosystem outcome")
    return {name: _nonnegative_integer(value[name], f"run count {name}") for name in OUTCOME_NAMES}


def _integer(value: object, name: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool):
        raise ValueError(f"{name} must be an integer")
    return value


def _nonnegative_integer(value: object, name: str) -> int:
    result = _integer(value, name)
    if result < 0:
        raise ValueError(f"{name} must not be negative")
    return result
