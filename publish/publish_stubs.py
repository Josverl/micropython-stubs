""" 
prepare a set of stub files for publishing to PyPi

required folder structure: 

+--stubs
|  +--<any stub folders in repo>
|  +--micropython-v1_18-esp32
|
+--publish
|  +--template
|     +--pyproject.toml
|
|  +--<folder for each package>
|     +--<package name> double nested to match the folder structure
|  +--<family>-version-<port>-<board>-<type>-stubs
|  +--micropython-v1_18-esp32-generic-fw-stubs

!!Note: anything excluded in .gitignore is not packaged by poetry 
"""
from pathlib import Path
from typing import List, Tuple


from stubpacker import StubPackage
from stubber.utils.versions import clean_version


# Defaults to the root of the project
root_path: Path = Path(".")


# ######################################
# esp32-generic-stubs
# ######################################
# todo : pass this as parameters
version = "v1.18"
type = "board"
port = "esp32"
board = "GENERIC"

ver_flat = clean_version(version, flat=True)

if 1:
    stub_package_name = f"micropython-{port}-{board}-stubs"
    package_path = root_path / "publish" / stub_package_name

    stubs: List[Tuple[str, Path]] = [
        ("Firmware stubs", Path("./stubs") / f"micropython-{ver_flat}-{port}"),
        ("Frozen stubs", Path("./stubs") / f"micropython-{ver_flat}-frozen" / port / board),
        ("Core Stubs", Path("./stubs") / "cpython_core-pycopy"),
    ]

    package = StubPackage(package_path, stub_package_name, version)
    package.update_stub_package(stubs)
    package.bump()
    package.build()
    package.publish()
    package.clean()


# ######################################
# micropython-core-stubs
# ######################################
# todo : pass this as parameters
version = "v0.1"
type = "core"


if 0:
    stub_package_name = f"micropython-{type}-stubs"
    package_path = root_path / "publish" / stub_package_name

    stubs: List[Tuple[str, Path]] = [
        ("Core Stubs", Path("./stubs") / "cpython_core-pycopy"),
    ]
    package = StubPackage(package_path, stub_package_name, version, description="Micropython Core stubs")
    package.update_stub_package(stubs)

    package.bump()
    package.build()
    package.publish()
    package.clean()


# ######################################
# micropython-doc-stubs
# ######################################
version = "v1.18"
type = "doc"
ver_flat = clean_version(version, flat=True)

if 1:
    stub_package_name = f"micropython-{type}-stubs"
    package_path = root_path / "publish" / stub_package_name

    stubs: List[Tuple[str, Path]] = [
        ("Doc Stubs", Path("./stubs") / f"micropython-{ver_flat}-docstubs"),
    ]

    package = StubPackage(package_path, stub_package_name, version, description="Micropython Doc Stubs")
    package.update_stub_package(stubs)

    package.bump()
    package.build()
    package.publish()
    package.clean()



