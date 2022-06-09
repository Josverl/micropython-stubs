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
import logging
from pathlib import Path
from typing import List, Tuple

import jsons
from stubber.utils.versions import clean_version

from json_database import  JsonDatabase
from pysondb import PysonDB

from stubpacker import StubPackage

LOG = logging.getLogger(__name__)
LOG.setLevel("INFO")


# Defaults to the root of the project
root_path: Path = Path(".")


# db_path = root_path / "data" / "package_data.jsondb"
# db = JsonDatabase("packages", db_path.as_posix())

db_path = root_path / "data" / "package_data_v3.jsondb"
db = PysonDB(db_path.as_posix())


# ######################################
# esp32-generic-stubs
# ######################################
# todo : pass this as parameters
version = "v1.18"
type = "board"
port = "esp32"
board = "GENERIC"

ver_flat = clean_version(version, flat=True)



for mpy_version in ["1.17", "1.18"]:
    for port in ["esp32"]:
        board = "GENERIC"

        # keys
        stub_package_name = f"micropython-{port}-{board}-stubs".lower().replace("-generic-stubs", "-stubs")
       
        # find in the database
        known_pkgs = db.get_by_query(query=lambda x: x['mpy_version'] == mpy_version and x['name'] == stub_package_name)

        print( f"{stub_package_name} {mpy_version}- {len(known_pkgs)}")
        [LOG.info(f"{x['name']} - {x['mpy_version']} - {x['pkg_version']}") for x in known_pkgs]




if 1:
    # for board stubs: remove -GENERIC from the name to simplify package naming convention
    stub_package_name = f"micropython-{port}-{board}-stubs".lower().replace("-generic-stubs", "-stubs")
    package_path = root_path / "publish" / stub_package_name

    stubs: List[Tuple[str, Path]] = [
        ("Firmware stubs", Path("./stubs") / f"micropython-{ver_flat}-{port}"),
        ("Frozen stubs", Path("./stubs") / f"micropython-{ver_flat}-frozen" / port / board),
        ("Core Stubs", Path("./stubs") / "cpython_core-pycopy"),
    ]

    package = StubPackage(package_path, stub_package_name, version, stubs=stubs)
    print(package.pkg_version)
    print(package.mpy_version)

    db.add(package.to_json())
    db.commit()
    package.update_package_files()
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
    package = StubPackage(package_path, stub_package_name, version, description="Micropython Core stubs", stubs=stubs)
    package.update_package_files()

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

if 0:
    stub_package_name = f"micropython-doc-stubs"
    package_path = root_path / "publish" / stub_package_name

    stubs: List[Tuple[str, Path]] = [
        ("Doc Stubs", Path("./stubs") / f"micropython-{ver_flat}-docstubs"),
    ]

    package = StubPackage(package_path, stub_package_name, version, description="Micropython Doc Stubs",stubs=stubs)
    package.update_package_files()

    package.bump()
    package.build()
    package.publish()
    package.clean()



