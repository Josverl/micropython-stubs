""" 
prepare a set of stub files for publishing to PyPi


"""
import tomli_w
from pathlib import Path
import shutil
import subprocess

from create_project import create_project


# todo : pass this as parameters
ver = "v1_18"
port = "esp32"
board = "generic"

stub_package_name = f"micropython-{port}-{board}-stubs"


# assume running in the root of the project
package_path = Path("./publish") / stub_package_name

# todo: convert V1_18 to semver and use the patch level as version for the stubs package

semver = "1.18.1"

stubs = [("Firmware stubs", Path("./stubs") / f"micropython-{ver}-{port}"), ("Core Stubs", Path("./stubs") / "cpython_core-pycopy")]


# create the package folder
package_path.mkdir(parents=True, exist_ok=True)

# Copy in the subs to the package
for name, folder in stubs:
    print(f"Copying {name}")
    shutil.copytree(folder, package_path / folder.name, symlinks=True, dirs_exist_ok=True)

# add a readme with the names of the stubs
# todo: prettify this
with open(package_path / "README.md", "w") as f:
    f.write(f"# {stub_package_name}\n\n")
    f.write(f"Included stubs:\n")
    for name, folder in stubs:
        f.write(f"* {name} from {folder.as_posix()}\n")

# - create/update pyproject.toml

create_project(package_path, stub_package_name, semver, f"MicroPython stubs for {ver} {port}")


# TODO: check the validity of the assembled package using mypy ?

subprocess.run(["poetry", "check"], cwd=package_path)

# bump the version of the package
subprocess.run(["poetry", "version", "prerelease", "-s"], cwd=package_path)
# subprocess.run(["poetry", "version", "patch", "-s"], cwd=package_path)

# create package
subprocess.run(["poetry", "build", "-vvv"], cwd=package_path)

#Publish to test 
subprocess.run(["poetry", "publish", "-r", "test-pypi"], cwd=package_path)

# Publish

