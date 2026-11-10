from ..reporting import sanitize_report_text


def test_windows_path_redaction_preserves_diagnostic_suffix():
    diagnostic = r"diagnostic: C:\work\driver.py: undefined name"

    assert sanitize_report_text(diagnostic) == "diagnostic: <path>: undefined name"
