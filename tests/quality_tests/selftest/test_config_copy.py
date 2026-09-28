from pathlib import Path
from types import SimpleNamespace

import conftest
import typecheck


class _TestCache:
    def __init__(self, root: Path):
        self.root = root

    def makedir(self, name: str) -> Path:
        path = self.root / "d" / name
        path.mkdir(parents=True, exist_ok=True)
        return path

    def mkdir(self, name: str) -> Path:
        return self.makedir(name)


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


def test_refresh_mpy_shed_leaves_matching_install_untouched(tmp_path, monkeypatch):
    source = tmp_path / "reference" / "_mpy_shed"
    source.mkdir(parents=True)
    (source / "time_mp.pyi").write_text("class _TicksMs: ...\n", encoding="utf-8")
    destination = tmp_path / "typings" / "_mpy_shed"

    conftest._refresh_mpy_shed(source, destination)

    def fail_if_called(*args, **kwargs):
        raise AssertionError("matching cache was rewritten")

    monkeypatch.setattr(conftest.shutil, "rmtree", fail_if_called)
    monkeypatch.setattr(conftest.shutil, "copytree", fail_if_called)
    conftest._refresh_mpy_shed(source, destination)


def test_type_stub_target_reuses_matching_local_sources(tmp_path, monkeypatch):
    root = tmp_path / "project"
    stdlib_source = root / "publish" / "micropython-stdlib-stubs"
    stubs_source = root / "publish" / "micropython-v1_29_0-windows-stubs"
    stdlib_source.mkdir(parents=True)
    stubs_source.mkdir(parents=True)
    (stdlib_source / "builtins.pyi").write_text("class object: ...\n", encoding="utf-8")
    source_stub = stubs_source / "micropython.pyi"
    source_stub.write_text("class const: ...\n", encoding="utf-8")
    config = SimpleNamespace(
        cache=_TestCache(root / ".pytest_cache"),
        inipath=root / "pyproject.toml",
        getoption=lambda *args, **kwargs: False,
    )
    request = SimpleNamespace(config=config)
    installs = []

    def install_stubs(portboard, version, stub_source, pytestconfig, target, *, no_cache=False):
        installs.append((portboard, version, stub_source, no_cache))
        (target / "micropython.pyi").write_text("class const: ...\n", encoding="utf-8")
        return True

    monkeypatch.setenv("PYTEST_XDIST_TESTRUNUID", "run-1")
    monkeypatch.setattr(conftest, "install_stubs", install_stubs)

    first = conftest.type_stub_cache_path_fx.__wrapped__("windows", "v1.29.0", "local", config, request)
    second = conftest.type_stub_cache_path_fx.__wrapped__("windows", "v1.29.0", "local", config, request)

    assert first == second
    assert installs == [("windows", "v1.29.0", "local", False)]

    monkeypatch.setenv("PYTEST_XDIST_TESTRUNUID", "run-2")
    third = conftest.type_stub_cache_path_fx.__wrapped__("windows", "v1.29.0", "local", config, request)

    assert third == first
    assert installs == [("windows", "v1.29.0", "local", False)]

    source_stub.write_text("class const: ...\nclass schedule: ...\n", encoding="utf-8")
    conftest._cached_directory_fingerprint.cache_clear()
    fourth = conftest.type_stub_cache_path_fx.__wrapped__("windows", "v1.29.0", "local", config, request)

    assert fourth == first
    assert installs == [
        ("windows", "v1.29.0", "local", False),
        ("windows", "v1.29.0", "local", False),
    ]


def test_install_stubs_honors_no_cache(tmp_path, monkeypatch):
    root = tmp_path / "project"
    (root / "publish" / "micropython-stdlib-stubs").mkdir(parents=True)
    (root / "publish" / "micropython-v1_29_0-windows-stubs").mkdir(parents=True)
    config = SimpleNamespace(cache=_TestCache(root / ".pytest_cache"), inipath=root / "pyproject.toml")
    calls = []

    def run(command, **kwargs):
        calls.append((command, kwargs))

    monkeypatch.setattr(conftest.subprocess, "run", run)

    assert conftest.install_stubs("windows", "v1.29.0", "local", config, root / "target", no_cache=True)
    command, kwargs = calls[0]
    assert command[:3] == ["uv", "--no-cache", "pip"]
    assert "env" not in kwargs
    assert kwargs["check"] is True
