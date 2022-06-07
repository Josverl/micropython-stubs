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

# todo : pass this as parameters
ver = "v1_18"
port = "esp32"
board = "generic"


# Defaults to the root of the project
root_path: Path = Path(".")


# ######################################
# esp32-generic-stubs
# ######################################
if 0:
    stub_package_name = f"micropython-{port}-{board}-stubs"
    package_path = root_path / "publish" / stub_package_name

    stubs: List[Tuple[str, Path]] = [
        ("Firmware stubs", Path("./stubs") / f"micropython-{ver}-{port}"),
        #    ("Core Stubs", Path("./stubs") / "cpython_core-pycopy"),
    ]

    create_stub_package(package_path, stub_package_name, stubs)


# ######################################
# micropython-core-stubs
# ######################################
stub_package_name = f"micropython-core-stubs"
package_path = root_path / "publish" / stub_package_name

stubs: List[Tuple[str, Path]] = [
    ("Core Stubs", Path("./stubs") / "cpython_core-pycopy"),
]

create_stub_package(package_path, stub_package_name, stubs, description="Micropython Core stubs")


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
