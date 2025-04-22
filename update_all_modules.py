"""
Creates a all_modules.json file containing a list of all modules across all micropython boards and ports
this is build by running this script from the root of the micropython-stubs repository
- it parses the  modules.json files of all the published packages in the repository
  Therefore the package builds should be run before this script is run


Viewer : https://flatgithub.com/Josverl/micropython-stubs/?filename=all_modules.json
"""

import contextlib
import hashlib
import json
from pathlib import Path

from packaging.version import Version

try:
    import tomllib  # type: ignore
except ModuleNotFoundError:
    import tomli as tomllib  # type: ignore

ADD_STDLIB = False


def partialhash(file: Path):
    with open(file, "rb") as f:
        # read by line and hash
        md5 = hashlib.blake2b(digest_size=4)
        # skip the module docstring and initial comments
        l = 0
        for line in f:
            # skip tripple quoated docstring
            if line.startswith(b'"""'):
                l += 1
                for line in f:
                    l += 1
                    if line.startswith(b'"""'):
                        break
            # skip comment
            if line.startswith(b"#"):  # and l < 10:
                l += 1
                continue
            md5.update(line)
    return md5.hexdigest()


def add_package(pkg_path: Path, all_modules, port="", board="", pkg_version=""):
    with open(pkg_path, "rb") as f:
        # port , board  and pkg_version are optional and are only used for stdlib modules
        # to keep these consistend with the port and board they are included in
        pyproject = tomllib.load(f)
        try:
            # new style pyproject.toml
            pkg_name = pyproject["project"]["name"]
            pkg_version = pkg_version or pyproject["project"]["version"]
            dependencies = pyproject["project"]["dependencies"]
        except KeyError:
            pkg_name = pyproject["tool"]["poetry"]["name"]
            pkg_version = pkg_version or pyproject["tool"]["poetry"]["version"]
            dependencies = pyproject["tool"]["poetry"]["dependencies"]
        mpy_version = Version(pkg_version).base_version
        modules = pyproject["tool"]["poetry"]["packages"]
        familiy = ""

        with contextlib.suppress(KeyError, IndexError):
            familiy = pkg_name.split("-")[0]
            port = port or pkg_name.split("-")[1]
            board = board or pkg_name.split("-")[2]

        if board == "stubs":
            board = "GENERIC"
        for mod in modules:
            # get module name
            mod_name = mod["include"].split(".")[0]
            if mod_name.startswith("stdlib/"):
                mod_name = mod_name.split("/")[1]
            row = {
                "family": familiy,
                "version": mpy_version,
                "mod_name": mod_name,
                "port": port,
                "board": board,
                "package": pkg_name,
                "pkg_version": pkg_version,
                "hash": partialhash(pkg_path.parent / mod["include"]),
            }
            all_modules.append(row)
        if ADD_STDLIB:
            # add stdlib modules if they are included in the pyproject.toml
            for dep in dependencies:
                if dep.startswith("micropython-"):
                    dep_pkg_path = pkg_path.parent.parent / dep / "pyproject.toml"
                    # add stdlib modules for this port & board
                    add_package(dep_pkg_path, all_modules, port, board, pkg_version)


def main(output_file="all_modules.json", input_dir="publish"):
    all_modules = []
    for pkg_path in Path(input_dir).rglob("pyproject.toml"):
        if "stdlib" in str(pkg_path):
            continue
        # if not "1_18" in str(pkg_path) and not "1_17" in str(pkg_path):
        #     continue
        try:
            add_package(pkg_path, all_modules)
        except KeyError as e:
            print(f"KeyError {e} in {pkg_path}")
            continue
    with open("all_modules.json", "w") as f:
        json.dump(all_modules, f, indent=4)


if __name__ == "__main__":
    main()
