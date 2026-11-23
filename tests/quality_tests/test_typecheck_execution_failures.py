from collections.abc import Callable
from pathlib import Path
from subprocess import CompletedProcess

import pytest
import typecheck_pyrefly
import typecheck_ruff


@pytest.mark.parametrize(
    ("subprocess_run", "run_checker"),
    [
        pytest.param("typecheck_ruff.subprocess.run", typecheck_ruff.run_ruff, id="ruff"),
        pytest.param("typecheck_pyrefly.subprocess.run", typecheck_pyrefly.run_pyrefly, id="pyrefly"),
    ],
)
@pytest.mark.parametrize(
    ("result", "message"),
    [
        pytest.param(CompletedProcess([], 1, "", "No module named checker"), "produced no JSON output", id="missing"),
        pytest.param(CompletedProcess([], 2, "", "checker crashed"), "failed with returncode 2", id="failed"),
        pytest.param(CompletedProcess([], 0, "not-json", ""), "Could not parse", id="invalid-json"),
    ],
)
def test_checker_adapter_propagates_execution_failure(
    subprocess_run: str,
    run_checker: Callable[[Path], list[object]],
    result: CompletedProcess[str],
    message: str,
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.setattr(subprocess_run, lambda *_args, **_kwargs: result)

    with pytest.raises(RuntimeError, match=message):
        run_checker(tmp_path)
