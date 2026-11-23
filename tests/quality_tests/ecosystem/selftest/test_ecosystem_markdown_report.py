import pytest

from ..markdown_report import render_markdown_reports


def _document(*, pyright_status: str = "pass", pyright_command: list[str] | None = None) -> dict[str, object]:
    return {
        "schema_version": 2,
        "mode": "batch",
        "exit_code": 1,
        "duration_seconds": 1.25,
        "counts": {
            "pass": 1,
            "type_check_failure": 1,
            "unsupported": 0,
            "unavailable": 1,
            "skipped": 0,
            "error": 0,
        },
        "qa_matrix": {"checkers": ["pyright", "mypy"]},
        "results": [
            {
                "package_identity": "repository:github:example/driver",
                "outcome": "type_check_failure",
                "reports": [
                    {
                        "version": "v1.29.0",
                        "portboard": "rp2-rpi_pico",
                        "results": [
                            {
                                "checker": "pyright",
                                "status": pyright_status,
                                "command": pyright_command or ["pyright", "--outputjson"],
                                "diagnostics": [],
                                "error_count": 0,
                                "warning_count": 0,
                                "files_analyzed": 2,
                                "message": "",
                            },
                            {
                                "checker": "mypy",
                                "status": "fail",
                                "command": ["mypy", "source"],
                                "diagnostics": [
                                    {
                                        "file": "source/driver.py",
                                        "severity": "error",
                                        "rule": "assignment",
                                        "message": "Incompatible assignment",
                                        "range": {"start": {"line": 4, "character": 2}},
                                    }
                                ],
                                "error_count": 1,
                                "warning_count": 0,
                                "files_analyzed": 2,
                                "message": "",
                            },
                        ],
                    }
                ],
            },
            {
                "package_identity": "index:missing-package",
                "outcome": "unavailable",
                "reports": [],
            },
        ],
    }


def test_render_markdown_reports_creates_overview_and_every_checker_detail() -> None:
    reports = render_markdown_reports(_document())

    assert "# Ecosystem type checker report" in reports.overview
    assert "| Package results | 3 |" in reports.overview
    assert "## 1.29.0" in reports.overview
    assert "## not checked / no version" in reports.overview
    assert "| Package | Target | Outcome | mypy | pyright |" in reports.overview
    assert 'href="ecosystem_mypy.md#ecosystem-detail-mypy-' in reports.overview
    assert set(reports.checker_details) == {"mypy", "pyright"}

    mypy = reports.checker_details["mypy"]
    assert "# mypy ecosystem diagnostics" in mypy
    assert "| Failed | 1 |" in mypy
    assert '"source/driver.py"(5,3): error [assignment]: Incompatible assignment' in mypy
    assert "[Back to ecosystem type checker report](ecosystem.md)" in mypy

    pyright = reports.checker_details["pyright"]
    assert "| Passed | 1 |" in pyright
    assert "No diagnostics were reported." in pyright


def test_rendered_module_command_omits_python_executable_prefix() -> None:
    reports = render_markdown_reports(_document(pyright_status="fail", pyright_command=["<path>", "-m", "pyright", "--outputjson"]))

    pyright = reports.checker_details["pyright"]
    assert "**Command:** `pyright --outputjson`" in pyright
    assert "&lt;path&gt; -m pyright" not in pyright


@pytest.mark.parametrize(
    ("occurrence_count", "expected_rendered_count", "is_shared"),
    [(20, 20, False), (21, 1, True)],
)
def test_checker_report_hoists_diagnostics_above_threshold(occurrence_count: int, expected_rendered_count: int, is_shared: bool) -> None:
    diagnostic = {
        "file": "source/shared.py",
        "severity": "error",
        "rule": "assignment",
        "message": "Incompatible assignment",
        "range": {"start": {"line": 4, "character": 2}},
    }
    document = _document()
    document["results"] = [
        {
            "package_identity": f"index:package-{index}",
            "outcome": "type_check_failure",
            "reports": [
                {
                    "version": "v1.29.0",
                    "portboard": "rp2-rpi_pico",
                    "results": [
                        {
                            "checker": "mypy",
                            "status": "fail",
                            "command": ["mypy", "source"],
                            "diagnostics": [diagnostic],
                            "error_count": 1,
                            "warning_count": 0,
                            "files_analyzed": 1,
                            "message": "",
                        }
                    ],
                }
            ],
        }
        for index in range(occurrence_count)
    ]

    markdown = render_markdown_reports(document).checker_details["mypy"]
    rendered_diagnostic = '"source/shared.py"(5,3): error [assignment]: Incompatible assignment'

    assert markdown.count(rendered_diagnostic) == expected_rendered_count
    assert ("## Shared diagnostics" in markdown) is is_shared
    assert (f"Reported by {occurrence_count} runs" in markdown) is is_shared
