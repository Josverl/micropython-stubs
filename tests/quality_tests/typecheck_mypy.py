import json
import logging
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Dict, List
from cachetools import cached, TTLCache
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


@cached(cache=TTLCache(maxsize=128, ttl=60*20))
def mypy_version():
    "quick way to get the mypy version"
    return mypy_api.run(["--version"])[0].strip()


def check_with_mypy(snip_path):
    """
    Run mypy on the specified path and return the type checking results.

    Args:
        snip_path (str): The path to the code snippet to be checked.

    Returns:
        json: The type checking results in pyright format.

    """
    raw_results = run_mypy(snip_path)
    results = raw_results.split("\n")
    results = gitlab_to_pyright(gitlab_report(map(str.rstrip, results)))    
    return results


def mypy_patch(check_path):
    if not check_path.exists():
        Exception(f"Path {check_path} not found")

    for f in ("typings/sys.pyi",):
        file = check_path / f

        if file.exists():
            print(f"Removing {f}")
            if file.is_file():
                file.unlink()

            elif file.is_dir():
                shutil.rmtree(file)


def run_mypy(path: Path):
    print(f"Running mypy in {path}")
    mypy_patch(path)
    cmd = [ sys.executable, "-m", "mypy", "--no-error-summary", "--no-color","--show-absolute-path", "."]
    try:
        output = subprocess.run(
            cmd,
            # check=True,
            cwd=path,
            capture_output=True,
            text=True,
            shell=False,
        )
        return output.stdout
    except subprocess.CalledProcessError as e:
        print(e)

# convert from gitlab to pyright format

def gitlab_to_pyright(report):
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
        i["range"]["start"]["line"] = int(issue["location"]["lines"]["begin"]) -1 
        pyright_report["generalDiagnostics"].append(i)

    for sev in ["error", "warning", "information"]:
        count = len([d for d in pyright_report["generalDiagnostics"] if d["severity"] == sev])
        pyright_report["summary"][f"{sev}Count"] = count
    return pyright_report



