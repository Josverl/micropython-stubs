from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType


def _load_build_module() -> ModuleType:
    repo_root = Path(__file__).resolve().parents[2]
    script_path = repo_root / "publish" / "micropython-stdlib-stubs" / "build.py"
    spec = importlib.util.spec_from_file_location("build_stdlib", script_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_update_module_vars_keeps_known_micropython_builtins(tmp_path: Path):
    mod = _load_build_module()
    builtins_stub = tmp_path / "builtins.pyi"
    builtins_stub.write_text(
        "NotImplemented: _NotImplementedType\nIOError = OSError\nEnvironmentError = OSError\n",
        encoding="utf-8",
    )

    mod.update_module_vars(builtins_stub, set())

    assert builtins_stub.read_text(encoding="utf-8").splitlines() == [
        "NotImplemented: _NotImplementedType",
        "IOError = OSError",
        "# EnvironmentError = OSError",
    ]
