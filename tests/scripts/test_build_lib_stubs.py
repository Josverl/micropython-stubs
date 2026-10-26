from __future__ import annotations

import importlib.util
import ast
import json
import subprocess
import sys
import tomllib
import zipfile
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("build_lib_stubs", ROOT / "experiment/build_lib_stubs.py")
assert spec is not None and spec.loader is not None
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


def test_manifest_resolves_transitive_dependency(tmp_path: Path):
    cwd = Path.cwd()
    mpy = ROOT / "repos/micropython"
    lib = ROOT / "repos/micropython-lib"
    if not lib.is_dir() or not mpy.is_dir():
        pytest.skip("Local source checkouts are required")
    manifest = tmp_path / "manifest.py"
    manifest.write_text('require("usb-device-cdc")\n')
    dependency = builder.collect_sources(manifest, mpy, lib, tmp_path / "dependency")
    assert {r["target"] for r in dependency} == {"usb/device/__init__.py", "usb/device/core.py", "usb/device/cdc.py"}
    assert Path.cwd() == cwd


@pytest.mark.parametrize("result", [True, False])
def test_missing_generated_output_is_failure(tmp_path: Path, monkeypatch: pytest.MonkeyPatch, result: bool):
    (tmp_path / "sample.py").write_text("def example(): pass\n")
    monkeypatch.setattr(builder, "generate_pyi_files", lambda _: result)
    with pytest.raises(RuntimeError, match="Missing generated|failed to generate"):
        builder.generate_stubs(tmp_path)


def test_origin_docstrings(tmp_path: Path):
    lib = tmp_path / "lib"
    folder = tmp_path / "stubs"
    (folder / "usb/device").mkdir(parents=True)
    (folder / "aiorepl.pyi").write_text("def task(): ...\n")
    (folder / "usb/device/__init__.pyi").write_text('"""Existing documentation."""\nfrom .core import get as get\n')
    (folder / "usb/__init__.pyi").write_text("")
    records = [
        {"target": "aiorepl.py", "source": str(lib / "micropython/aiorepl/aiorepl.py")},
        {"target": "usb/device/__init__.py", "source": str(lib / "micropython/usb/usb-device/usb/device/__init__.py")},
    ]
    builder.add_origin_docstrings(folder, lib, records)
    assert ast.get_docstring(ast.parse((folder / "aiorepl.pyi").read_text())) == (
        "Module: 'aiorepl' from micropython-lib\n\nlocation: micropython/aiorepl/aiorepl.py"
    )
    device = ast.parse((folder / "usb/device/__init__.pyi").read_text())
    assert ast.get_docstring(device) == (
        "Module: 'usb.device' from micropython-lib\n\n"
        "location: micropython/usb/usb-device/usb/device/__init__.py\n\nExisting documentation."
    )
    assert isinstance(device.body[1], ast.ImportFrom)
    assert ast.get_docstring(ast.parse((folder / "usb/__init__.pyi").read_text())) == (
        "Module: 'usb' from micropython-lib\n\nlocation: micropython/usb/usb-device/usb/"
    )


def test_built_wheel():
    package = ROOT / "publish/micropython-lib-stubs"
    if not (package / "dist").is_dir():
        pytest.skip("Run experiment/build_lib_stubs.py first")
    expected = {p.relative_to(package).as_posix() for p in package.rglob("*.pyi")}
    (wheel,) = (package / "dist").glob("*.whl")
    assert not list((package / "dist").glob("*.tar.gz"))
    with zipfile.ZipFile(wheel) as archive:
        names = set(archive.namelist())
        assert builder.MARKER not in names
        assert {p for p in names if p.endswith(".pyi")} == expected
        assert not any(p.endswith(".py") for p in names)
        metadata = archive.read(next(p for p in names if p.endswith(".dist-info/METADATA"))).decode()
        expected_version = tomllib.loads((package / "pyproject.toml").read_text())["project"]["version"]
        assert f"Version: {expected_version}\n" in metadata


def test_installed_wheel_with_board_stubs(tmp_path: Path):
    package = ROOT / "publish/micropython-lib-stubs"
    if not (package / "dist").is_dir():
        pytest.skip("Run experiment/build_lib_stubs.py first")
    (wheel,) = (package / "dist").glob("*.whl")
    target = tmp_path / "typings"
    board = ROOT / "publish/micropython-v1_29_0-rp2-stubs"
    subprocess.run(["uv", "pip", "install", "--target", str(target), str(board)], check=True)
    subprocess.run(["uv", "pip", "install", "--no-deps", "--target", str(target), str(wheel)], check=True)
    (tmp_path / "pyrightconfig.json").write_text(
        json.dumps(
            {
                "include": ["smoke.py"],
                "stubPath": "typings",
                "typeCheckingMode": "standard",
                "pythonVersion": "3.9",
                "reportMissingModuleSource": "none",
            }
        )
    )
    (tmp_path / "smoke.py").write_text(
        "import aiorepl\nimport logging\nimport usb.device\n"
        "from usb.device.cdc import CDCInterface\nfrom usb.device.core import Interface\n"
        'repl = aiorepl.task()\nlogger = logging.getLogger("experiment")\n'
        'logger.info("Ready")\ndevice = usb.device.get()\ncdc = CDCInterface()\n'
        "cdc.init(baudrate=115200)\ninterface: Interface = cdc\n"
    )
    subprocess.run([sys.executable, "-m", "pyright", "--project", str(tmp_path / "pyrightconfig.json")], check=True)
