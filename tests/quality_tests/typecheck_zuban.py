import json
import logging
import os
import re
import shutil
import subprocess
from pathlib import Path

from cachetools import TTLCache, cached

from typecheck_mypy import DIAGNOSTIC, HEADER

log = logging.getLogger()

_DIAGNOSTIC_RE = re.compile(
    r"^(?P<file>.+?):(?P<line>\d+)"
    r"(?::(?P<column>\d+))?"
    r"(?::(?P<end_line>\d+))?"
    r"(?::(?P<end_column>\d+))?"
    r": (?P<severity>error|warning|note): (?P<message>.*?)(?:  \[(?P<rule>[^]]+)\])?$"
)


@cached(cache=TTLCache(maxsize=1, ttl=60 * 20))
def zuban_version() -> str:
    """Return the installed Zuban version."""
    executable = shutil.which("zuban")
    if executable is None:
        return "unknown"
    try:
        result = subprocess.run([executable, "--version"], capture_output=True, text=True, check=True)
    except (OSError, subprocess.CalledProcessError) as exc:
        log.warning("Could not get Zuban version: %s", exc)
        return "unknown"
    return result.stdout.strip()


def check_with_zuban(snip_path: Path) -> dict:
    """Run Zuban and return diagnostics in the shared Pyright-shaped format."""
    output = run_zuban(snip_path)
    return zuban_to_pyright(output, snip_path)


def run_zuban(path: Path) -> str:
    """Run Zuban in its default mode using the snippet's copied configuration."""
    executable = shutil.which("zuban")
    if executable is None:
        raise RuntimeError("Zuban executable was not found")

    command = [
        executable,
        "check",
        ".",
        "--show-column-numbers",
        "--show-error-end",
        "--show-error-codes",
        "--no-pretty",
        "--no-error-summary",
    ]
    env = {**os.environ, "NO_COLOR": "1"}
    result = subprocess.run(command, capture_output=True, text=True, cwd=path, env=env)
    if result.returncode not in (0, 1):
        raise RuntimeError(f"Zuban failed with returncode {result.returncode}: {result.stderr or result.stdout}")
    return result.stdout


def zuban_to_pyright(output: str, base_path: Path) -> dict:
    """Convert Zuban's mypy-compatible text diagnostics to Pyright format."""
    report = json.loads(HEADER)
    report["version"] = zuban_version()
    diagnostics = []
    files_analyzed = set()

    for line in output.splitlines():
        match = _DIAGNOSTIC_RE.match(line.strip())
        if match is None:
            continue

        diagnostic = json.loads(DIAGNOSTIC)
        file_path = Path(match["file"])
        if not file_path.is_absolute():
            file_path = base_path / file_path
        file_path = file_path.resolve()
        files_analyzed.add(str(file_path))

        start_line = max(0, int(match["line"]) - 1)
        start_column = max(0, int(match["column"] or 1) - 1)
        end_line = max(start_line, int(match["end_line"] or match["line"]) - 1)
        end_column = max(start_column, int(match["end_column"] or match["column"] or 1) - 1)

        diagnostic["file"] = str(file_path)
        diagnostic["severity"] = "information" if match["severity"] == "note" else match["severity"]
        diagnostic["message"] = match["message"]
        diagnostic["rule"] = match["rule"] or ""
        diagnostic["range"]["start"] = {"line": start_line, "character": start_column}
        diagnostic["range"]["end"] = {"line": end_line, "character": end_column}
        diagnostics.append(diagnostic)

    report["generalDiagnostics"] = diagnostics
    for severity in ("error", "warning", "information"):
        report["summary"][f"{severity}Count"] = sum(item["severity"] == severity for item in diagnostics)
    report["summary"]["filesAnalyzed"] = len(files_analyzed)
    return report
