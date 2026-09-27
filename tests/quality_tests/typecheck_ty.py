import json
import logging
import os
import hashlib
import shutil
import subprocess
import sys
import tempfile
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


# Directories inside `typings/` that are not MicroPython module stubs.
_NON_MODULE_DIRS = {"stdlib", "stubs", "__pycache__"}

# Marker file written once a merged typeshed has been built completely.
_TYPESHED_MARKER = ".mpy-typeshed-complete"


def build_ty_typeshed(typings: Path, destination: Path) -> Path:
    """
    Build a custom typeshed root for ty from an installed `typings/` folder.

    Unlike pyright (`stubPath`) and mypy (`MYPYPATH`), ty always resolves standard library
    modules from its typeshed search path, so MicroPython stubs placed on `extra-paths` can
    never shadow them. The only way to make ty see `time.ticks_ms`, `gc.mem_free`, ... is to
    hand it a custom typeshed that already contains the MicroPython flavour of those modules.

    The destination must live outside every other search path, otherwise ty panics
    (see https://github.com/astral-sh/ty/issues/523).
    """
    if (destination / _TYPESHED_MARKER).exists():
        return destination

    destination.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(dir=destination.parent, prefix="build-"))
    stdlib = staging / "stdlib"
    shutil.copytree(typings / "stdlib", stdlib)
    if (typings / "stubs").is_dir():
        shutil.copytree(typings / "stubs", staging / "stubs")

    # Overlay the MicroPython module stubs on top of the reduced typeshed.
    module_names = set()
    for item in typings.iterdir():
        if item.is_dir():
            if item.name in _NON_MODULE_DIRS or item.name.endswith(".dist-info"):
                continue
            shutil.copytree(item, stdlib / item.name, dirs_exist_ok=True)
            module_names.add(item.name)
        elif item.suffix == ".pyi":
            shutil.copy2(item, stdlib / item.name)
            module_names.add(item.stem)

    versions = stdlib / "VERSIONS"
    known = {line.split(":", 1)[0].strip() for line in versions.read_text(encoding="utf-8").splitlines()}
    extra = sorted(name for name in module_names if name not in known)
    if extra:
        with versions.open("a", encoding="utf-8") as f:
            f.write("\n" + "\n".join(f"{name}: 3.0-" for name in extra) + "\n")

    (staging / _TYPESHED_MARKER).touch()
    try:
        staging.rename(destination)
    except OSError:
        # Another xdist worker won the race; its copy is equivalent.
        shutil.rmtree(staging, ignore_errors=True)
    return destination


def _fingerprint(typings: Path) -> str:
    "Stable key for the contents of a `typings/` folder."
    h = hashlib.sha256()
    for file in sorted(p for p in typings.rglob("*") if p.is_file()):
        h.update(file.relative_to(typings).as_posix().encode())
        h.update(str(file.stat().st_size).encode())
    return h.hexdigest()[:16]


def ty_typeshed_for(path: Path) -> Path | None:
    """
    Return the custom typeshed to use for the snippet workspace `path`, building it on demand.

    The typeshed is cached outside of any snippet workspace - both to avoid rebuilding it for
    every folder, and because ty panics when the typeshed overlaps another search path.
    """
    typings = path / "typings"
    if not (typings / "stdlib").is_dir():
        return None
    destination = Path(tempfile.gettempdir()) / "mpy-ty-typeshed" / _fingerprint(typings)
    try:
        return build_ty_typeshed(typings, destination)
    except Exception:
        log.exception("Could not build a custom typeshed for ty")
        return None


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
    typeshed = ty_typeshed_for(path)
    if typeshed:
        cmd += ["--typeshed", str(typeshed)]

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
