from pathlib import Path

import conftest
import typecheck


def _make_test_tree(root: Path) -> None:
    config_path = root / "_configs"
    config_path.mkdir(parents=True)
    (config_path / "pyproject.toml").write_text("[tool.test]\n", encoding="utf-8")
    (config_path / "readme.md").write_text("ignored\n", encoding="utf-8")
    (config_path / ".venv").mkdir()
    (config_path / ".venv" / "pyvenv.cfg").write_text("ignored\n", encoding="utf-8")


def test_snip_path_ignores_config_directories(tmp_path, monkeypatch, pytestconfig):
    root = tmp_path / "quality_tests"
    _make_test_tree(root)
    feature_path = root / "feat_example"
    feature_path.mkdir()
    (feature_path / "main.py").write_text("pass\n", encoding="utf-8")
    workspace = tmp_path / "workspace"
    workspace.mkdir()
    monkeypatch.setattr(conftest, "__file__", str(root / "conftest.py"))

    result = conftest.snip_path_fx.__wrapped__("example", workspace, pytestconfig)

    assert result == workspace
    assert (workspace / "main.py").is_file()
    assert (workspace / "pyproject.toml").is_file()
    assert not (workspace / ".venv").exists()
    assert not (workspace / "readme.md").exists()


def test_bulk_config_copy_ignores_config_directories(tmp_path, monkeypatch):
    root = tmp_path / "quality_tests"
    _make_test_tree(root)
    feature_path = root / "feat_example"
    feature_path.mkdir()
    monkeypatch.setattr(typecheck, "__file__", str(root / "typecheck.py"))

    typecheck.copy_config_files()

    assert (feature_path / "pyproject.toml").is_file()
    assert not (feature_path / ".venv").exists()
    assert not (feature_path / "readme.md").exists()


def test_refresh_mpy_shed_replaces_stale_install(tmp_path):
    source = tmp_path / "reference" / "_mpy_shed"
    source.mkdir(parents=True)
    (source / "time_mp.pyi").write_text("class _TicksMs: ...\n", encoding="utf-8")
    destination = tmp_path / "typings" / "_mpy_shed"
    destination.mkdir(parents=True)
    (destination / "time_mp.pyi").write_text("# stale\n", encoding="utf-8")
    (destination / "removed.pyi").write_text("# obsolete\n", encoding="utf-8")

    conftest._refresh_mpy_shed(source, destination)

    assert (destination / "time_mp.pyi").read_text(encoding="utf-8") == "class _TicksMs: ...\n"
    assert not (destination / "removed.pyi").exists()
