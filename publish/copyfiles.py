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
import subprocess
from pathlib import Path
from typing import List, Tuple

import tomli_w
from packaging.version import parse

from create_project import create_stub_package
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
board = "generic"

ver_flat = clean_version(version, flat=True)

if 1:
    stub_package_name = f"micropython-{port}-{board}-board-stubs"
    package_path = root_path / "publish" / stub_package_name

    stubs: List[Tuple[str, Path]] = [
        ("Firmware stubs", Path("./stubs") / f"micropython-{ver_flat}-{port}"),
        ("Core Stubs", Path("./stubs") / "cpython_core-pycopy"),
    ]

    create_stub_package(package_path, stub_package_name, stubs, version= version)


# ######################################
# micropython-core-stubs
# ######################################
# todo : pass this as parameters
version = "v0.1"
type = "core"

ver_flat = clean_version(version, flat=True)
if 0:
    stub_package_name = f"micropython-{type}-stubs"
    package_path = root_path / "publish" / stub_package_name

    stubs: List[Tuple[str, Path]] = [
        ("Core Stubs", Path("./stubs") / "cpython_core-pycopy"),
    ]

    create_stub_package(package_path, stub_package_name, stubs, version = version, description="Micropython Core stubs")


# ######################################
# micropython-doc-stubs
# ######################################
version = "v1.18"
type = "doc"

if 0:
    stub_package_name = f"micropython-{type}-stubs"
    package_path = root_path / "publish" / stub_package_name

    stubs: List[Tuple[str, Path]] = [
        ("Doc Stubs", Path("./stubs") / "cpython_core-pycopy"),
    ]

    create_stub_package(package_path, stub_package_name, stubs, version = "0.1.0",description="Micropython Core stubs")



subprocess.run(["poetry", "check", "-vvv"], cwd=package_path)
# bump the version of the package
# TODO: Use Post release
subprocess.run(["poetry", "version", "prerelease", "-s"], cwd=package_path)
# subprocess.run(["poetry", "version", "patch", "-s"], cwd=package_path)

# create package
subprocess.run(["poetry", "build", "-vvv"], cwd=package_path)

# Publish to test
subprocess.run(["poetry", "publish", "-r", "test-pypi"], cwd=package_path)

# Publish


# # https://packaging.pypa.io/en/latest/_modules/packaging/version.html
# # [<epoch.!]<version>[.post<build>]

# semver = parse("v1_18".replace("_", "."))
# semver = parse("v1_18.post1".replace("_", "."))
# semver = parse("v1_18.rev1".replace("_", "."))
# semver.base_version
# semver.release
# semver.public
