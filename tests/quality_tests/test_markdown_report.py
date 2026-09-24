import json
from types import SimpleNamespace

import pytest
from markdown_report import add_report_metadata, render_markdown

pytest_plugins = ["pytester"]


def make_report(
    *,
    checker="pyright",
    test_name="test_typecheck",
    values=("v1.29.0", "unix", "stdlib"),
    outcome="passed",
    when="call",
    wasxfail=None,
    diagnostic="",
):
    test_id = json.dumps([f"tests/test_example.py::{test_name}", ["version", "portboard", "feature"], list(values)])
    properties = [
        ("markdown_report_checker", checker),
        ("markdown_report_test_id", test_id),
        ("markdown_report_test_name", test_name),
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
    assert "| v1.29.0 unix stdlib |" in markdown
    assert markdown.count('<a href="#typecheck-detail-') == 2
    assert "### future-checker" in markdown
    assert "### ty" in markdown
    assert "unknown member: Pin" in markdown
    assert "bad assignment" in markdown
    assert "Traceback" not in markdown


def test_render_markdown_uses_failure_precedence_and_missing_cells():
    reports = [
        make_report(checker="pyright", outcome="passed"),
        make_report(checker="pyright", outcome="failed", when="teardown"),
        make_report(checker="mypy", values=("v1.29.0", "unix", "asyncio")),
    ]

    markdown = render_markdown(reports)

    stdlib_line = next(line for line in markdown.splitlines() if line.startswith("| v1.29.0 unix stdlib |"))
    assert ">FAIL</span>" in stdlib_line
    assert "| - |" in stdlib_line


def test_render_markdown_disambiguates_rows_and_escapes_content():
    reports = [
        make_report(test_name="test_first", values=("v1.29.0", "unix", "a|b")),
        make_report(test_name="test_second", values=("v1.29.0", "unix", "a|b")),
    ]

    markdown = render_markdown(reports)

    assert "v1.29.0 unix a\\|b (test_first)" in markdown
    assert "v1.29.0 unix a\\|b (test_second)" in markdown


def test_render_markdown_uses_a_longer_fence_for_checker_output():
    markdown = render_markdown([make_report(outcome="failed", diagnostic="message with ``` inside")])

    assert "````text\nmessage with ``` inside\n````" in markdown


def test_report_option_aggregates_xdist_results_and_is_opt_in(pytester):
    quality_tests = __file__.rsplit("/", 1)[0]
    pytester.makeconftest(
        f"""
import sys
sys.path.insert(0, {quality_tests!r})
exec(compile(open({quality_tests + "/conftest.py"!r}).read(), {quality_tests + "/conftest.py"!r}, "exec"))
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
    assert "| Test | expected-checker | new-checker |" in markdown
    assert "| v1.29.0 unix asyncio |" in markdown
    assert '<a href="#typecheck-detail-expected-checker-' in markdown
    assert "checker diagnostic without traceback" in markdown
    assert "Traceback (most recent call last)" not in markdown

    report_path.write_text("sentinel", encoding="utf-8")
    result = pytester.runpytest_subprocess("-n", "2", "-q")
    result.assert_outcomes(passed=1, xfailed=1)
    assert report_path.read_text(encoding="utf-8") == "sentinel"
