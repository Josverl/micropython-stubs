import json
import logging
import os
import subprocess
import sys
from contextlib import contextmanager
from pathlib import Path

from cachetools import TTLCache, cached

# Pyright JSON format

HEADER = """
{
    "version": "",
    "time": "",
    "generalDiagnostics": [],
    "summary": {
        "filesAnalyzed": 0,
        "errorCount": 0,
        "warningCount": 0,
        "informationCount": 0,
        "timeInSec": 0
    }
}
"""
DIAGNOSTIC = """
{
    "file": "",
    "severity": "",
    "message": "",
    "rule": "",
    "range": {
        "start": {
            "line": 0,
            "character": 0
        },
        "end": {
            "line": 999,
            "character": 99
        }
    }
}
"""

# ty (via its gitlab code quality output) uses gitlab's severity levels
SEVERITY_MAP = {
    "info": "information",
    "minor": "warning",
    "major": "error",
    "critical": "error",
    "blocker": "error",
}

log = logging.getLogger()


@cached(cache=TTLCache(maxsize=128, ttl=60 * 20))
def ty_version():
    "Get the ty version"
    try:
        result = subprocess.run(
            [sys.executable, "-m", "ty", "version"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except Exception as e:
        log.warning(f"Could not get ty version: {e}")
        return "unknown"


def check_with_ty(snip_path: Path):
    """
    Run ty on the specified path and return the type checking results.

    Args:
        snip_path (Path): The path to the code snippet to be checked.

    Returns:
        json: The type checking results in pyright format.

    """
    raw_results = run_ty(snip_path)
    results = ty_to_pyright(raw_results, snip_path)
    return results


@contextmanager
def chdir_mgr(path):
    """
    Context manager that changes the current working directory to the specified path,
    and then restores the original working directory when the context is exited.
    """
    oldpwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(oldpwd)


def run_ty(path: Path) -> list:
    """
    Run ty on the specified path.

    Args:
        path (Path): The path to run ty on.

    Returns:
        list: The result of running ty, in gitlab code quality format.
    """
    cmd = [
        sys.executable,
        "-m",
        "ty",
        "check",
        "--output-format=gitlab",
    ]

    try:
        with chdir_mgr(path):
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
            )

            # ty returns exit code 1 if there are errors, which is expected
            if result.returncode not in (0, 1):
                raise RuntimeError(f"ty failed with returncode {result.returncode}: {result.stderr}")

            if result.stdout.strip():
                try:
                    return json.loads(result.stdout)
                except json.JSONDecodeError as e:
                    raise RuntimeError(f"Could not parse ty JSON output: {e}") from e
            return []
    except Exception:
        log.exception("Error running ty")
        raise


def ty_to_pyright(ty_output: list, base_path: Path):
    """
    Convert ty's gitlab code quality output to Pyright format.

    Args:
        ty_output (list): List of issues from ty in gitlab code quality JSON format.
        base_path (Path): Base path for resolving relative file paths.

    Returns:
        dict: Pyright code quality report in JSON format.
    """
    pyright_report = json.loads(HEADER)
    pyright_report["version"] = ty_version()
    pyright_report["generalDiagnostics"] = []

    files_analyzed = set()

    for issue in ty_output:
        i = json.loads(DIAGNOSTIC)

        location = issue.get("location", {})
        # Get the file path and make it absolute
        file_path = Path(location.get("path", ""))
        if not file_path.is_absolute():
            file_path = base_path / file_path
        i["file"] = str(file_path)
        files_analyzed.add(str(file_path))

        # Map severity
        i["severity"] = SEVERITY_MAP.get(issue.get("severity", "major"), "error")

        # Get the message and rule
        i["message"] = issue.get("description", "")
        i["rule"] = issue.get("check_name", "")

        # Get the location - ty uses 1-based lines and columns, pyright uses 0-based
        positions = location.get("positions", {})
        begin = positions.get("begin", {})
        end = positions.get("end", begin)
        line_no = max(0, begin.get("line", 1) - 1)
        col_no = max(0, begin.get("column", 1) - 1)
        end_line_no = max(line_no, end.get("line", begin.get("line", 1)) - 1)
        end_col_no = max(col_no, end.get("column", begin.get("column", 1)) - 1)

        i["range"]["start"]["line"] = line_no
        i["range"]["start"]["character"] = col_no
        i["range"]["end"]["line"] = end_line_no
        i["range"]["end"]["character"] = end_col_no

        pyright_report["generalDiagnostics"].append(i)

    # Update summary counts
    for sev in ["error", "warning", "information"]:
        count = len([d for d in pyright_report["generalDiagnostics"] if d["severity"] == sev])
        pyright_report["summary"][f"{sev}Count"] = count

    pyright_report["summary"]["filesAnalyzed"] = len(files_analyzed)

    return pyright_report
