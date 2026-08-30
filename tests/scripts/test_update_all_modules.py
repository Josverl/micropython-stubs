from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType


def _load_script_module() -> ModuleType:
    repo_root = Path(__file__).resolve().parents[2]
    script_path = repo_root / "scripts" / "update_all_modules.py"
    spec = importlib.util.spec_from_file_location("update_all_modules", script_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_add_package_reads_hatch_modules(tmp_path: Path):
    mod = _load_script_module()
    package = tmp_path / "micropython-v1_29_0-rp2-stubs"
    (package / "uasyncio").mkdir(parents=True)
    (package / "machine.pyi").write_text("class Pin: ...\n", encoding="utf-8")
    (package / "uasyncio" / "__init__.pyi").write_text("class Event: ...\n", encoding="utf-8")
    (package / "README.md").write_text("Not a module\n", encoding="utf-8")
    pyproject = package / "pyproject.toml"
    pyproject.write_text(
        """
[project]
name = "micropython-rp2-stubs"
version = "1.29.0.post1"
dependencies = []

[tool.hatch.build.targets.wheel]
include = ["*.pyi", "**/*.pyi", "README.md"]
""".strip(),
        encoding="utf-8",
    )

    rows = []
    mod.add_package(pyproject, rows)

    assert [row["mod_name"] for row in rows] == ["machine", "uasyncio/__init__"]
    assert {row["version"] for row in rows} == {"1.29.0"}
    assert {row["package"] for row in rows} == {"micropython-rp2-stubs"}


def test_package_modules_reads_legacy_poetry_list(tmp_path: Path):
    mod = _load_script_module()
    pyproject = {
        "tool": {
            "poetry": {
                "packages": [
                    {"include": "machine.pyi"},
                    {"include": "uasyncio/__init__.pyi"},
                ]
            }
        }
    }

    modules = mod.package_modules(pyproject, tmp_path / "pyproject.toml")

    assert modules == [
        {"include": "machine.pyi"},
        {"include": "uasyncio/__init__.pyi"},
    ]
