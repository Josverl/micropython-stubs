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
import tomli_w
from pathlib import Path
import shutil
import subprocess

from create_project import create_project
from typing import List, Tuple
from packaging.version import parse

# todo : pass this as parameters
ver = "v1_18"
port = "esp32"
board = "generic"


def create_stub_package(
    package_path: Path,
    name: str,
    stubs: List[Tuple[str, Path]],
    version: str = "0.0.1",
    description: str = "MicroPython stubs",
):
    """ """
    # package_path = Path("C:\\develop\\MyPython\\micropython-stubs\\publish\\micropython-esp32-generic-stubs")

    # todo: convert V1_18 to semver and use the patch level as version for the stubs package
    semver = parse(version.replace("_", "."))

    # create the package folder
    package_path.mkdir(parents=True, exist_ok=True)

    # Copy in the subs to the package
    for name, folder in stubs:
        print(f"Copying {name} from {folder}")
        shutil.copytree(folder, package_path / folder.name, symlinks=True, dirs_exist_ok=True)

    # add a readme with the names of the stubs
    # todo: prettify this
    with open(package_path / "README.md", "w") as f:
        f.write(f"# {stub_package_name}\n\n")
        f.write(f"Included stubs:\n")
        for name, folder in stubs:
            f.write(f"* {name} from {folder.as_posix()}\n")

    # - create/update pyproject.toml
    # todo: pass stubs
    create_project(
        package_path,
        stub_package_name,
        semver.public,
        [p.name for description, p in stubs],
        description=description,
    )

    # TODO: check the validity of the assembled package using mypy ?

    subprocess.run(["poetry", "check"], cwd=package_path)


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
