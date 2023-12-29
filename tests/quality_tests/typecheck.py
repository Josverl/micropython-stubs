import json
import logging
import platform
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Dict, List

import fasteners
import pytest
from mypy_gitlab_code_quality import generate_report as gitlab_report
from packaging.version import Version

from typecheck_mypy import check_with_mypy

log = logging.getLogger()


def copy_config_files():
    # copy the config files from the __config folder to all check_* and feat_* folders 
    # so that the typecheck can be run from the command line
    my_path = Path(__file__).parent.absolute()
    config_path = my_path / "_configs"
    for folder in list(my_path.glob("check_*")) + list(my_path.glob("feat_*")):
        for file in config_path.glob("*.*"):
            if file.name == "readme.md":
                continue
            try: 
                shutil.copy(file, folder)
            except Exception as e:
                print(f"Could not copy {file} to {folder} : {e}")
                pass


def port_and_board(portboard):
    if "-" in portboard:
        port, board = portboard.split("-", 1)
    else:
        port, board = portboard, ""
    return port, board

def stub_ignore(line, version, port, board, linter, is_source=True) -> bool:
    """
    Check if a typecheck error should be ignored based on the version of micropython , the port and the board
    the same syntax can be used in the source file or in the test case condition :

    format of the source line (is_source=True)
        import espnow # stubs-ignore: version<1.21.0 or not port.startswith('esp')

    or condition (is_source=False) line:
        version<1.21.0
        skip version<1.21.0 # skip prefix to helps human understanding / reading
        skip port.startswith('esp')
    """
    if is_source:
        comment = line.rsplit("#")[-1].strip()
        if not (comment.startswith("stubs-ignore") and ":" in comment):
            return False
        id, condition = comment.split(":")
        if id.strip() != "stubs-ignore":
            return False
        condition = condition.strip()
    else:
        condition = line.strip()
    if condition.lower().startswith("skip"):
        condition = condition[4:].strip()
    context = {}
    context["Version"] = Version
    context["version"] = Version(version) if not version in ("latest", "-") else Version("9999.99.99")
    context["port"] = port
    context["board"] = board
    context["linter"] = linter

    try:
        # transform : version>=1.20.1 to version>=Version('1.20.1') using a regular expression
        condition = re.sub(r"(\d+\.\d+\.\d+)", r"Version('\1')", condition.strip())
        result = eval(condition, context)
        # print(f'stubs-ignore: {condition} -> {"Skip" if result else "Process"}')
    except Exception as e:
        log.warning(f"Incorrect stubs-ignore condition: `{condition}`\ncaused: {e}")
        result = False

    return bool(result)


def filter_issues(issues: List[Dict], version: str,*, linter:str, portboard: str = ""):
    port, board = portboard.split("-") if "-" in portboard else (portboard, "")
    for issue in issues:
        try:
            filename = Path(issue["file"])
            with open(filename, "r") as f:
                lines = f.readlines()
            line = issue["range"]["start"]["line"]
            if len(lines) > line:
                theline: str = lines[line]
                # check if the line contains a stubs-ignore comment
                if stub_ignore(theline, version, port, board, linter=linter):
                    issue["severity"] = "information"
        except KeyError as e:
            log.warning(f"Could not process issue: {e} \n{json.dumps(issues, indent=4)}")
    return issues

def run_typechecker( snip_path:Path, version:str, portboard:str, pytestconfig:pytest.Config, *, linter:str,):
    """
    Run Pyright static type checker a path with validation code

    Args:
        snip_path (Path): The path to the project.
        version (str): The version of the stubs .
        portboard (str): The portboard of the project.
        pytestconfig: The pytest configuration object.

    Returns:
        tuple: A tuple containing the information message and the number of errors found.
    """

    typecheck_lock = fasteners.InterProcessLock(snip_path / "typecheck_lock.file")

    results = {}
    with typecheck_lock:
        if linter=="pyright":
            results = check_with_pyright(snip_path)
        elif linter=="mypy":
            results = check_with_mypy(snip_path)
        else:
            raise NotImplementedError(f"Unknown linter {linter}")
            results = []
    if not results or not "generalDiagnostics" in results:
        pytest.xfail(f"Could not run {linter} on {snip_path}")

    issues: List[Dict] = results["generalDiagnostics"]
    # for each of the issues - retrieve the line in the source file to inspect if has a trailing comment
    issues = filter_issues(issues, version, portboard=portboard, linter=linter)

    # log the errors  in the issues list so that pytest will capture the output
    for issue in issues:
        # log file:line:column?: message
        try:
            relative = Path(issue["file"]).relative_to(pytestconfig.rootpath).as_posix()
        except Exception:
            relative = issue["file"]
        # try to make a VSCode clickable link in the pytest output
        # Python style links: From "<path>", line <line>
        # <path>(<line>,<column>):<message>
        msg = f"\"{relative}\"({issue['range']['start']['line']+1},{issue['range']['start']['character']}): {issue['message']}"
        # caplog.messages.append(msg)
        if issue["severity"] == "error":
            log.error(msg)
        elif issue["severity"] == "warning":
            log.warning(msg)
        else:
            log.info(msg)

    info_msg = f"{linter} found {results['summary']['errorCount']} errors and {results['summary']['warningCount']} warnings in {results['summary']['filesAnalyzed']} files."
    errorcount = len([i for i in issues if i["severity"] == "error"])
    return info_msg,errorcount


#=====================================================================================

def check_with_pyright(snip_path):
    
    cmd = f"pyright --project {snip_path.as_posix()} --outputjson"
    use_shell = platform.system() != "Windows"
    results = {}
    try:
                # run pyright in the folder with the check_scripts to allow modules to import each other.
        result = subprocess.run(cmd, shell=use_shell, capture_output=True, cwd=snip_path.as_posix())
    except OSError as e:
        raise e
    if result.returncode >= 2:
        assert (
                    0
                ), f"Pyright failed with returncode {result.returncode}: {result.stdout}\n{result.stderr}"
    try:
        results = json.loads(result.stdout)
    except Exception:
        assert 0, "Could not load pyright's JSON output..."
    return results
