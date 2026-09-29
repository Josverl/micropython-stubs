from ..markdown_report import render_markdown_reports


def _document() -> dict[str, object]:
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
                                "status": "pass",
                                "command": ["pyright", "--outputjson"],
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
