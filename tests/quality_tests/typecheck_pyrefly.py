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

SEVERITY_MAP = {
    "error": "error",
    "warn": "warning",
    "info": "information",
}

log = logging.getLogger()


@cached(cache=TTLCache(maxsize=128, ttl=60 * 20))
def pyrefly_version():
    "Get the pyrefly version"
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pyrefly", "--version"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except Exception as e:
        log.warning(f"Could not get pyrefly version: {e}")
        return "unknown"


def check_with_pyrefly(snip_path: Path):
    """
    Run pyrefly on the specified path and return the type checking results.

    Args:
        snip_path (Path): The path to the code snippet to be checked.

    Returns:
        json: The type checking results in pyright format.

    """
    raw_results = run_pyrefly(snip_path)
    results = pyrefly_to_pyright(raw_results, snip_path)
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


def run_pyrefly(path: Path) -> list:
    """
    Run pyrefly on the specified path.

    Args:
        path (Path): The path to run pyrefly on.

    Returns:
        list: The result of running pyrefly in JSON format.
    """
    # Do not pass a file/folder argument: this keeps pyrefly in "project-checking mode"
    # so that the project_includes/project_excludes from pyproject.toml (e.g. excluding
    # the typings folder) are honored.
    cmd = [
        sys.executable,
        "-m",
        "pyrefly",
        "check",
        "--output-format=json",
    ]

    try:
        with chdir_mgr(path):
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
            )

            # pyrefly returns exit code 1 if there are errors, which is expected
            if result.returncode not in (0, 1):
                log.error(f"Pyrefly failed with returncode {result.returncode}: {result.stderr}")
                return []

            if result.stdout.strip():
                try:
                    return json.loads(result.stdout).get("errors", [])
                except json.JSONDecodeError as e:
                    log.error(f"Could not parse pyrefly JSON output: {e}")
                    return []
            return []
    except Exception as e:
        log.error(f"Error running pyrefly: {e}")
        return []


def pyrefly_to_pyright(pyrefly_output: list, base_path: Path):
    """
    Convert pyrefly output to Pyright format.

    Args:
        pyrefly_output (list): List of issues from pyrefly in JSON format.
        base_path (Path): Base path for resolving relative file paths.

    Returns:
        dict: Pyright code quality report in JSON format.
    """
    pyright_report = json.loads(HEADER)
    pyright_report["version"] = pyrefly_version()
    pyright_report["generalDiagnostics"] = []

    files_analyzed = set()

    for issue in pyrefly_output:
        i = json.loads(DIAGNOSTIC)

        # Get the file path and make it absolute
        file_path = Path(issue.get("path", ""))
        if not file_path.is_absolute():
            file_path = base_path / file_path
        i["file"] = str(file_path)
        files_analyzed.add(str(file_path))

        # Map severity
        i["severity"] = SEVERITY_MAP.get(issue.get("severity", "error"), "error")

        # Get the message and rule
        i["message"] = issue.get("description", "")
        i["rule"] = issue.get("name", "")

        # Get the location - pyrefly uses 1-based lines and columns, pyright uses 0-based
        line_no = max(0, issue.get("line", 1) - 1)
        col_no = max(0, issue.get("column", 1) - 1)
        end_line_no = max(line_no, issue.get("stop_line", issue.get("line", 1)) - 1)
        end_col_no = max(col_no, issue.get("stop_column", issue.get("column", 1)) - 1)

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
