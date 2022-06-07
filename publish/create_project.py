import shutil
import subprocess
from pathlib import Path
from typing import List, Tuple

import tomli
import tomli_w
from packaging.version import parse

template_path = Path("C:\\develop\\MyPython\\micropython-stubs\\publish\\template")


def create_pyproject(
    package_path: Path,
    name: str,
    version: str = "0.0.1",
    folders=List[str],
    description: str = "MicroPython stubs",
):
    """
    create or update/overwrite a `pyproject.toml` file by combining a template file
    with the given parameters.
    and updating it with the pyi files included
    """
    # package_path = Path("C:\\develop\\MyPython\\micropython-stubs\\publish\\micropython-esp32-generic-stubs")

    # TODO: do not overwrite existing pyproject.toml but read and apply changes to it
    pre_existing = (package_path / "pyproject.toml").exists()
    if pre_existing:
        with open(package_path / "pyproject.toml", "rb") as f:
            pyproject = tomli.load(f)
            # clear out the packages section
            pyproject["tool"]["poetry"]["packages"] = []
    else:
        # read the template pyproject.toml file
        with open(template_path / "pyproject.toml", "rb") as f:
            pyproject = tomli.load(f)
            # do not overwrite the version of a pre-existing file
            pyproject["tool"]["poetry"]["version"] = version

    # update the name , version and description of the package
    pyproject["tool"]["poetry"]["name"] = name
    pyproject["tool"]["poetry"]["description"] = description

    # add the modules to the package
    for folder_name in folders:
        folder = package_path / folder_name
        # find packages using __init__ files
        for p in folder.rglob("**/__init__.py"):
            # add the module to the package
            # fixme : only accounts for one level of packages
            pyproject["tool"]["poetry"]["packages"] += [{"from": folder.name, "include": p.parent.name}]
        # now find other stub files directly in the folder
        for p in folder.glob("*.pyi"):
            pyproject["tool"]["poetry"]["packages"] += [{"from": folder.name, "include": p.name}]

    try:
        # check if the result is a valid toml file
        tomli.loads(tomli_w.dumps(pyproject))
    except tomli.TOMLDecodeError as e:
        print("Could not create a valid TOML file")
        raise (e)

    with open(package_path / "pyproject.toml", "wb") as output:
        tomli_w.dump(pyproject, output)


def create_stub_package(
    package_path: Path,
    package_name: str,
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
        f.write(f"# {package_name}\n\n")
        f.write(f"Included stubs:\n")
        for name, folder in stubs:
            f.write(f"* {name} from {folder.as_posix()}\n")

    # - create/update pyproject.toml
    # todo: pass stubs
    create_pyproject(
        package_path,
        package_name,
        semver.public,
        [p.name for description, p in stubs],
        description=description,
    )

    # TODO: check the validity of the assembled package using mypy ?

    subprocess.run(["poetry", "check"], cwd=package_path)
