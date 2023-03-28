"""
Creates a all_modules.json file containing a list of all modules across all micropython boards and ports
this is build by running this script from the root of the micropython-stubs repository
- it parses the  modules.json files of all the published packages in the repository
  Therefore the package builds should be run before this script is run
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from packaging.version import Version

try:
    import tomllib  # type: ignore
except ModuleNotFoundError:
    import tomli as tomllib  # type: ignore

ADD_STDLIB = False


def main(output_file="all_modules.json", input_dir="publish"):
    all_modules = []
    for pkg_path in Path(input_dir).rglob("pyproject.toml"):
        if "stdlib" in str(pkg_path):
            continue
        # if not "1_18" in str(pkg_path) and not "1_17" in str(pkg_path):
        #     continue
        try:
            add_package(pkg_path,all_modules)
        except KeyError as e:
            continue
    with open("all_modules.json", "w") as f:
        json.dump(all_modules, f, indent=4)

def add_package(pkg_path:Path, all_modules, port="", board="", pkg_version=""):
    with open(pkg_path, 'rb') as f:
        # port , board  and pkg_version are optional and are only used for stdlib modules
        # to keep these consistend with the port and board they are included in
        pyproject = tomllib.load(f)
        pkg_name = pyproject["tool"]["poetry"]["name"]
        pkg_version = pkg_version or pyproject["tool"]["poetry"]["version"]
        mpy_version = Version(pkg_version).base_version
        modules = pyproject["tool"]["poetry"]["packages"]
        familiy =""
        try:
            familiy = pyproject["tool"]["poetry"]["name"].split("-")[0]
            port = port or pyproject["tool"]["poetry"]["name"].split("-")[1]
            board = board or pyproject["tool"]["poetry"]["name"].split("-")[2] 
        except (KeyError, IndexError):
            pass
        if board == "stubs":
            board = "GENERIC"
        for mod in modules:
                    # get module name
            mod_name  = mod["include"].split(".")[0]
            if mod_name.startswith("stdlib/"):
                mod_name = mod_name.split("/")[1]
            row = {
                            "family": familiy,
                            "version": mpy_version,
                            "mod_name": mod_name,
                            "port": port,
                            "board": board,
                            "package":  pkg_name, 
                            "pkg_version": pkg_version,
                    }
            all_modules.append(row)
        if ADD_STDLIB:
            # add stdlib modules if they are included in the pyproject.toml
            dependencies = pyproject["tool"]["poetry"]["dependencies"]
            for dep in dependencies:
                if dep.startswith("micropython-"):
                    dep_pkg_path = pkg_path.parent.parent/ dep / "pyproject.toml"
                    # add stdlib modules for this port & board
                    add_package(dep_pkg_path,all_modules, port , board, pkg_version)

if __name__ == "__main__":
    main()