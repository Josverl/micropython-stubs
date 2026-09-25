import json
from pathlib import Path
from types import SimpleNamespace

import pytest
from markdown_report import add_report_metadata, render_markdown, write_markdown_report

pytest_plugins = ["pytester"]


def make_report(
    *,
    checker="pyright",
    test_name="test_typecheck",
    names=("version", "portboard", "feature"),
    values=("v1.29.0", "unix", "stdlib"),
    outcome="passed",
    when="call",
    wasxfail=None,
    diagnostic="",
    nodeid=None,
):
    nodeid = nodeid or f"tests/test_example.py::{test_name}[local-{'-'.join(values)}-{checker}]"
    test_id = json.dumps([f"tests/test_example.py::{test_name}", list(names), list(values)])
    properties = [
        ("markdown_report_checker", checker),
        ("markdown_report_test_id", test_id),
        ("markdown_report_test_name", test_name),
        ("markdown_report_nodeid", nodeid),
        ("markdown_report_row_names", json.dumps(names)),
        ("markdown_report_row_values", json.dumps(values)),
    ]
    if diagnostic:
        properties.append(("markdown_report_diagnostic", diagnostic))
    return SimpleNamespace(
        user_properties=properties,
        outcome=outcome,
        when=when,
        wasxfail=wasxfail,
        passed=outcome == "passed",
        failed=outcome == "failed",
        skipped=outcome == "skipped",
    )


def test_add_report_metadata_omits_source_and_checker():
    item = SimpleNamespace(
        nodeid="tests/test_example.py::test_typecheck[local-v1.29.0-unix-stdlib-pyrefly]",
        callspec=SimpleNamespace(
            params={
                "stub_source": "local",
                "version": "v1.29.0",
                "portboard": "unix",
                "feature": "stdlib",
                "linter": "pyrefly",
            }
        ),
        funcargs={},
    )
    report = SimpleNamespace(user_properties=[])
    add_report_metadata(item, SimpleNamespace(excinfo=None), report)

    properties = dict(report.user_properties)
    assert properties["markdown_report_checker"] == "pyrefly"
    assert properties["markdown_report_nodeid"] == item.nodeid
    assert json.loads(properties["markdown_report_row_names"]) == ["version", "portboard", "feature"]
    assert json.loads(properties["markdown_report_row_values"]) == ["v1.29.0", "unix", "stdlib"]
    assert "local" not in properties["markdown_report_test_id"]


@pytest.mark.parametrize(
    ("outcome", "wasxfail", "expected"),
    [
        ("passed", None, "PASS"),
        ("failed", None, "FAIL"),
        ("skipped", None, "SKIP"),
        ("skipped", "expected", "XFAIL"),
        ("passed", "expected", "XPASS"),
        ("failed", "expected", "XPASS"),
    ],
)
def test_render_markdown_classifies_and_colors_statuses(outcome, wasxfail, expected):
    markdown = render_markdown([make_report(outcome=outcome, wasxfail=wasxfail, diagnostic="checker detail")])

    assert f">{expected}</span>" in markdown
    assert 'style="color:' in markdown


def test_render_markdown_discovers_checkers_and_links_failure_details():
    reports = [
        make_report(checker="pyright"),
        make_report(checker="future-checker", outcome="failed", diagnostic="unknown member: Pin"),
        make_report(checker="ty", outcome="skipped", wasxfail="experimental", diagnostic="bad assignment"),
    ]

    markdown = render_markdown(reports)

    assert "| Test | future-checker | pyright | ty |" in markdown
    assert "## 1.29.0" in markdown
    assert "| unix stdlib |" in markdown
    assert markdown.count('<a href="typecheck_report_') == 2
    assert 'href="typecheck_report_future_checker.md#typecheck-detail-future-checker-' in markdown
    assert 'href="typecheck_report_ty.md#typecheck-detail-ty-' in markdown
    assert "unknown member: Pin" not in markdown
    assert "bad assignment" not in markdown
    assert "Traceback" not in markdown


def test_render_markdown_uses_failure_precedence_and_missing_cells():
    reports = [
        make_report(checker="pyright", outcome="passed"),
        make_report(checker="pyright", outcome="failed", when="teardown"),
        make_report(checker="mypy", values=("v1.29.0", "unix", "asyncio")),
    ]

    markdown = render_markdown(reports)

    stdlib_line = next(line for line in markdown.splitlines() if line.startswith("| unix stdlib |"))
    assert ">FAIL</span>" in stdlib_line
    assert "| - |" in stdlib_line


def test_render_markdown_disambiguates_rows_and_escapes_content():
    reports = [
        make_report(test_name="test_first", values=("v1.29.0", "unix", "a|b")),
        make_report(test_name="test_second", values=("v1.29.0", "unix", "a|b")),
    ]

    markdown = render_markdown(reports)

    assert "unix a\\|b (test_first)" in markdown
    assert "unix a\\|b (test_second)" in markdown


def test_render_markdown_groups_stdlib_then_versions_descending():
    reports = [
        make_report(test_name="test_v19", values=("v1.9.0", "unix", "stdlib")),
        make_report(test_name="test_stdlib", values=("-", "stdlib", "stdlib_only")),
        make_report(test_name="test_v110", values=("v1.10.0", "unix", "stdlib")),
        make_report(test_name="test_preview", values=("v1.11.0-preview", "unix", "stdlib")),
        make_report(test_name="test_named", values=("latest", "unix", "stdlib")),
        make_report(test_name="test_missing", names=("portboard", "feature"), values=("unix", "asyncio")),
    ]

    markdown = render_markdown(reports)

    headings = [line for line in markdown.splitlines() if line.startswith("## ")]
    assert headings == [
        "## stdlib / no version",
        "## 1.11.0-preview",
        "## 1.10.0",
        "## 1.9.0",
        "## latest",
    ]
    assert "| stdlib stdlib_only |" in markdown
    assert "| unix asyncio |" in markdown
    assert "| v1.10.0 unix stdlib |" not in markdown


def test_render_markdown_sorts_rows_within_version_and_repeats_checker_columns():
    reports = [
        make_report(checker="z-checker", test_name="test_b", values=("v1.29.0", "unix", "stdlib")),
        make_report(checker="a-checker", test_name="test_a", values=("v1.29.0", "esp32", "asyncio")),
        make_report(checker="a-checker", test_name="test_stdlib", values=("-", "stdlib", "stdlib_only")),
    ]

    markdown = render_markdown(reports)

    assert markdown.count("| Test | a-checker | z-checker |") == 2
    assert markdown.index("| esp32 asyncio |") < markdown.index("| unix stdlib |")


def test_checker_report_uses_a_longer_fence_for_checker_output(tmp_path):
    nodeid = "tests/quality_tests/test_snippets.py::test_typecheck[local-v1.29.0-webassembly-webassembly-pyright]"
    terminalreporter = SimpleNamespace(
        stats={"failed": [make_report(outcome="failed", diagnostic="message with ``` inside", nodeid=nodeid)]}
    )

    write_markdown_report(terminalreporter, tmp_path / "typecheck_report.md")
    markdown = (tmp_path / "typecheck_report_pyright.md").read_text(encoding="utf-8")

    assert nodeid in markdown
    assert "````text\nmessage with ``` inside\n````" in markdown


def test_report_option_aggregates_xdist_results_and_is_opt_in(pytester):
    quality_tests = Path(__file__).resolve().parent.parent
    conftest = quality_tests / "conftest.py"
    pytester.makeconftest(
        f"""
import sys
sys.path.insert(0, {str(quality_tests)!r})
exec(compile(open({str(conftest)!r}).read(), {str(conftest)!r}, "exec"))
"""
    )
    pytester.makepyfile(
        """
import pytest

@pytest.mark.parametrize("stub_source", ["local"])
@pytest.mark.parametrize("version", ["v1.29.0"])
@pytest.mark.parametrize("portboard", ["unix"])
@pytest.mark.parametrize("feature", ["asyncio"])
@pytest.mark.parametrize("linter", ["new-checker", pytest.param("expected-checker", marks=pytest.mark.xfail(reason="expected"))])
def test_typecheck(stub_source, version, portboard, feature, linter):
    if linter == "expected-checker":
        raise AssertionError("checker diagnostic without traceback")
"""
    )

    result = pytester.runpytest_subprocess("-n", "2", "--report", "-q")
    result.assert_outcomes(passed=1, xfailed=1)

    report_path = pytester.path / "typecheck_report.md"
    markdown = report_path.read_text(encoding="utf-8")
    checker_report_path = pytester.path / "typecheck_report_expected_checker.md"
    checker_markdown = checker_report_path.read_text(encoding="utf-8")
    assert "| Test | expected-checker | new-checker |" in markdown
    assert "## 1.29.0" in markdown
    assert "| unix asyncio |" in markdown
    assert '<a href="typecheck_report_expected_checker.md#typecheck-detail-expected-checker-' in markdown
    assert "checker diagnostic without traceback" not in markdown
    assert "checker diagnostic without traceback" in checker_markdown
    assert "[Back to type checker test report](typecheck_report.md)" in checker_markdown
    assert "Traceback (most recent call last)" not in checker_markdown
    assert not (pytester.path / "typecheck_report_new_checker.md").exists()

    report_path.write_text("sentinel", encoding="utf-8")
    result = pytester.runpytest_subprocess("-n", "2", "-q")
    result.assert_outcomes(passed=1, xfailed=1)
    assert report_path.read_text(encoding="utf-8") == "sentinel"
