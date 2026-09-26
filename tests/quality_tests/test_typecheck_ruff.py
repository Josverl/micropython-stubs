import shutil
from pathlib import Path

from typecheck_ruff import run_ruff


def test_run_ruff_excludes_real_typings_directory(tmp_path: Path):
    config = Path(__file__).parent / "_configs" / "pyproject.toml"
    shutil.copy2(config, tmp_path / "pyproject.toml")
    (tmp_path / "check.py").write_text("if value == True:\n    pass\n", encoding="utf-8")
    typings = tmp_path / "typings"
    typings.mkdir()
    (typings / "installed_stub.pyi").write_text("if value == True:\n    pass\n", encoding="utf-8")

    results = run_ruff(tmp_path)

    assert len(results) == 1
    assert Path(results[0]["filename"]).name == "check.py"
