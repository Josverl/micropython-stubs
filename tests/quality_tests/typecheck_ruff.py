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
    "warning": "warning",
}

log = logging.getLogger()


@cached(cache=TTLCache(maxsize=128, ttl=60 * 20))
def ruff_version():
    "Get the ruff version"
    try:
        result = subprocess.run(
            [sys.executable, "-m", "ruff", "--version"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except Exception as e:
        log.warning(f"Could not get ruff version: {e}")
        return "unknown"


def check_with_ruff(snip_path: Path):
    """
    Run ruff on the specified path and return the type checking results.

    Args:
        snip_path (Path): The path to the code snippet to be checked.

    Returns:
        json: The type checking results in pyright format.

    """
    raw_results = run_ruff(snip_path)
    results = ruff_to_pyright(raw_results, snip_path)
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


def run_ruff(path: Path) -> list:
    """
    Run ruff on the specified path.

    Args:
        path (Path): The path to run ruff on.

    Returns:
        list: The result of running ruff in JSON format.
    """
    # Use ruff check with JSON output format
    cmd = [
        sys.executable,
        "-m",
        "ruff",
        "check",
        "--output-format=json",
        ".",
    ]
    
    try:
        with chdir_mgr(path):
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
            )
            
            # ruff returns exit code 1 if there are violations, which is expected
            if result.returncode not in (0, 1):
                log.error(f"Ruff failed with returncode {result.returncode}: {result.stderr}")
                return []
            
            if result.stdout.strip():
                try:
                    return json.loads(result.stdout)
                except json.JSONDecodeError as e:
                    log.error(f"Could not parse ruff JSON output: {e}")
                    return []
            return []
    except Exception as e:
        log.error(f"Error running ruff: {e}")
        return []


def ruff_to_pyright(ruff_output: list, base_path: Path):
    """
    Convert ruff output to Pyright format.

    Args:
        ruff_output (list): List of issues from ruff in JSON format.
        base_path (Path): Base path for resolving relative file paths.

    Returns:
        dict: Pyright code quality report in JSON format.
    """
    pyright_report = json.loads(HEADER)
    pyright_report["version"] = ruff_version()
    pyright_report["generalDiagnostics"] = []

    files_analyzed = set()
    
    for issue in ruff_output:
        i = json.loads(DIAGNOSTIC)
        
        # Get the file path and make it absolute
        file_path = Path(issue.get("filename", ""))
        if not file_path.is_absolute():
            file_path = base_path / file_path
        i["file"] = str(file_path)
        files_analyzed.add(str(file_path))
        
        # Map severity - ruff doesn't have severity in the same way, treat all as errors
        # unless it's a specific rule we want to treat as warning
        i["severity"] = "error"
        
        # Get the message and rule
        i["message"] = issue.get("message", "")
        code = issue.get("code", "")
        i["rule"] = code
        
        # Get the location
        location = issue.get("location", {})
        # ruff uses 1-based lines, pyright uses 0-based lines
        line_no = location.get("row", 1) - 1
        col_no = location.get("column", 0) - 1 if location.get("column", 0) > 0 else 0
        
        i["range"]["start"]["line"] = line_no
        i["range"]["start"]["character"] = col_no
        i["range"]["end"]["line"] = line_no
        i["range"]["end"]["character"] = col_no + 1
        
        pyright_report["generalDiagnostics"].append(i)

    # Update summary counts
    for sev in ["error", "warning", "information"]:
        count = len([d for d in pyright_report["generalDiagnostics"] if d["severity"] == sev])
        pyright_report["summary"][f"{sev}Count"] = count
    
    pyright_report["summary"]["filesAnalyzed"] = len(files_analyzed)
    
    return pyright_report
