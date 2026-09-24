from pathlib import Path

import pytest

from typecheck_zuban import check_with_zuban, run_zuban, zuban_to_pyright


def test_zuban_to_pyright_parses_ranges_rules_and_severities(tmp_path):
    output = "\n".join(
        [
            'main.py:4:11:4:18: error: Argument has incompatible type "str"  [arg-type]',
            "main.py:5:1:5:13: warning: This may be wrong  [test-warning]",
            "main.py:6:1:6:5: note: Additional context",
            "typings/_mpy_shed/__init__.pyi:49:17:49:26: error: Invalid type annotation  [valid-type]",
            "Found 1 error in 1 file (checked 1 source file)",
        ]
    )

    report = zuban_to_pyright(output, tmp_path)

    assert report["summary"] == {
        "filesAnalyzed": 2,
        "errorCount": 2,
        "warningCount": 1,
        "informationCount": 1,
        "timeInSec": 0,
    }
    error = report["generalDiagnostics"][0]
    assert error["file"] == str((tmp_path / "main.py").resolve())
    assert error["rule"] == "arg-type"
    assert error["range"] == {
        "start": {"line": 3, "character": 10},
        "end": {"line": 3, "character": 17},
    }
    assert report["generalDiagnostics"][3]["file"] == str((tmp_path / "typings/_mpy_shed/__init__.pyi").resolve())


def test_check_with_zuban_reports_real_type_error(tmp_path):
    (tmp_path / "bad.py").write_text(
        'def takes_int(value: int) -> None:\n    pass\n\ntakes_int("wrong")\n',
        encoding="utf-8",
    )

    report = check_with_zuban(tmp_path)

    assert report["summary"]["errorCount"] == 1
    assert report["generalDiagnostics"][0]["rule"] == "arg-type"


def test_run_zuban_rejects_tool_failures(tmp_path, monkeypatch):
    monkeypatch.setattr("typecheck_zuban.shutil.which", lambda _: "zuban")
    monkeypatch.setattr(
        "typecheck_zuban.subprocess.run",
        lambda *args, **kwargs: type("Result", (), {"returncode": 2, "stdout": "", "stderr": "bad config"})(),
    )

    with pytest.raises(RuntimeError, match="returncode 2: bad config"):
        run_zuban(tmp_path)
