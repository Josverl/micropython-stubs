import json
import logging
import os
import shutil
from contextlib import contextmanager
from pathlib import Path
from typing import Dict, List

from cachetools import TTLCache, cached
from mypy import api as mypy_api
from mypy_gitlab_code_quality import generate_report as gitlab_report

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
    "major": "error",
    "warning": "warning",
    "info": "information",
    "unknown": "information",
}

log = logging.getLogger()


@cached(cache=TTLCache(maxsize=128, ttl=60 * 20))
def mypy_version():
    "quick way to get the mypy version"
    return mypy_api.run(["--version"])[0].strip()


def check_with_mypy(snip_path, patch: bool):
    """
    Run mypy on the specified path and return the type checking results.

    Args:
        snip_path (str): The path to the code snippet to be checked.

    Returns:
        json: The type checking results in pyright format.

    """
    raw_results = run_mypy(snip_path, patch)
    results = raw_results.split("\n")
    gl_report = gitlab_report(map(str.rstrip, results))
    results = gitlab_to_pyright(gl_report)
    return results


def mypy_patch(check_path):
    """
    Remove the files that mypy is allergic to from the typings folder in the  path.

    Args:
        check_path (Path): The path to the snippets folder.

    Raises:
        Exception: If the check_path does not exist.

    """
    if not check_path.exists():
        raise Exception(f"Path {check_path} not found")

    for f in ("typings/sys.pyi",):
        file = check_path / f

        if file.exists():
            if file.is_file():
                #  print(f"Removing {f}")
                file.unlink()

            elif file.is_dir():
                shutil.rmtree(file)


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


def run_mypy(path: Path, patch: bool = False) -> str:
    """
    Run mypy on the specified path.

    Args:
        path (Path): The path to run mypy on.

    Returns:
        str: The result of running mypy.
    """
    if patch:
        mypy_patch(path)
    # Note that --warn-unused-ignores does not seem to work as expected in stdlib
    cmd = [
        "--warn-unused-ignores",
        "--no-error-summary",
        "--no-color",
        "--show-absolute-path",
        ".",
    ]
    # print(f"Running mypy in {path}\nmypy {' '.join(cmd)}")
    try:
        with chdir_mgr(path):
            # ref https://mypy.readthedocs.io/en/latest/extending_mypy.html#integrating-mypy-into-another-python-application
            result = mypy_api.run(cmd)
            errors = result[1]
            if errors:
                message = errors.split("\n")[0].replace(":", "-")
                err_report = f"{path}:0: error: {message}  [import]"
                return err_report

            return result[0]
    except Exception as e:
        print(e)


# convert from gitlab to pyright format


def gitlab_to_pyright(report):
    """
    Convert GitLab code quality report to Pyright format.

    Args:
        report (list): List of issues from GitLab code quality report.

    Returns:
        dict: Pyright code quality report in JSON format.
    """
    pyright_report = json.loads(HEADER)
    pyright_report["version"] = mypy_version()
    pyright_report["generalDiagnostics"] = []

    for issue in report:
        i = json.loads(DIAGNOSTIC)
        i["file"] = issue["location"]["path"]
        i["severity"] = SEVERITY_MAP[issue["severity"]]
        i["message"] = issue["description"]
        i["rule"] = issue["check_name"]
        # pyright uses 0-based lines - gitlab uses 1-based lines
        line_no = int(issue["location"]["lines"]["begin"]) - 1
        i["range"]["start"]["line"] = line_no
        i["range"]["end"]["line"] = line_no
        pyright_report["generalDiagnostics"].append(i)

    for sev in ["error", "warning", "information"]:
        count = len([d for d in pyright_report["generalDiagnostics"] if d["severity"] == sev])
        pyright_report["summary"][f"{sev}Count"] = count
    return pyright_report
