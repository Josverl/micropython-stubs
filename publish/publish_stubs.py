"""
prepare a set of stub files for publishing to PyPi

required folder structure:

+--stubs
|  +--<any stub folders in repo>
|  +--micropython-v1_18-esp32
|
+--publish
|  +--package_data.jsondb
|  +--template
|     +--pyproject.toml
|
|  +--<folder for each package>
|     +--<package name> double nested to match the folder structure
|  +--<family>-version-<port>-<board>-<type>-stubs
|  +--micropython-v1_18-esp32-generic-fw-stubs
|


!!Note: anything excluded in .gitignore is not packaged by poetry
"""

from pathlib import Path
from typing import Dict, List, Tuple

import jsons
from stubber.utils.versions import clean_version

from pysondb import PysonDB

from stubpacker import StubPackage
from packaging.version import parse

from loguru import logger as log
import sys

# replace std handler with a custom one capped on INFO level
log.remove()
log.add(sys.stderr, level="INFO", backtrace=True, diagnose=True)


root_path: Path = Path(".")


# db_path = root_path / "data" / "package_data.jsondb"
# db = JsonDatabase("packages", db_path.as_posix())

db_path = root_path / "publish" / "package_data.jsondb"
db = PysonDB(db_path.as_posix())


is_dryrun = True

log.info("preparing stubs ")
if is_dryrun:
    log.warning("dry run, no stubs will be published")
#
COMBINED = 1
DOC_STUBS = 2
CORE_STUBS = 2


def package_name(port, board, pkg=COMBINED, family="micropython") -> str:
    "generate a package name"
    if pkg == COMBINED:
        # # {family}-{port}-{board}-stubs
        return f"{family}-{port}-{board}-stubs".lower().replace("-generic-stubs", "-stubs")
    raise NotImplementedError(port, board, pkg)


def package_path(port, board, version, pkg=COMBINED, family="micropython") -> Path:
    "generate a package name"
    if pkg == COMBINED:
        # {family}-{version}-{port}-{board}-stubs
        return (
            root_path
            / "publish"
            / f"{family}-{clean_version(mpy_version, flat=True)}-{port}-{board}-stubs".lower().replace("-generic-stubs", "-stubs")
        )
    raise NotImplementedError(port, board, pkg)


for mpy_version in ["1.17", "1.18"]:  # "1.14", "1.15", "1.16",
    for port in ["esp32", "esp8266", "rp2", "stm32"]:
        # TODO: Stubber: firmware Stubber MUST report "stm32" for a pyboard
        board = "GENERIC"
        # package name for firmware package
        pkg_name = package_name(port, board)

        log.info("=" * 40)

        # find in the database
        recs = db.get_by_query(query=lambda x: x["mpy_version"] == mpy_version and x["name"] == pkg_name)
        # dict to list
        recs = [{"id": key, "data": recs[key]} for key in recs]
        # sort
        packages = sorted(recs, key=lambda x: parse(x["data"]["pkg_version"]))

        # [log.info(f"{x['name']} - {x['mpy_version']} - {x['pkg_version']}") for x in packages]
        if len(packages) > 0:
            pkg_from_db = packages[-1]["data"]
            log.info(f"Found {pkg_name} {mpy_version} {pkg_from_db['pkg_version']}")
        else:
            pkg_from_db = None

        # create the stub package on disk
        pkg_path = package_path(port, board, mpy_version)
        if pkg_from_db:

            package = StubPackage(pkg_path, pkg_name, json_data=pkg_from_db)
        else:
            ver_flat = clean_version(mpy_version, flat=True)

            stubs: List[Tuple[str, Path]] = [
                ("Firmware stubs", Path("./stubs") / f"micropython-{ver_flat}-{port}"),
                ("Frozen stubs", Path("./stubs") / f"micropython-{ver_flat}-frozen" / port / board),
                ("Core Stubs", Path("./stubs") / "cpython_core-pycopy"),
            ]
            package = StubPackage(pkg_path, pkg_name, mpy_version, stubs=stubs)

        # check if the sources exist
        OK = True
        for (name, path) in package.stub_sources:
            if not path.exists():
                log.warning(f"{pkg_path}: source {name} does not exist: {path}")
                OK = False
        if not OK:
            log.info(f"{pkg_path}: skipping as source stubs are missing")
            package._publish = False
            continue

        package.update_package_files()
        package.update_included_stubs()
        package.check()

        # If there are changes to the package, then publish it
        if package.is_changed():
            log.info(f"Found changes to package : {package.package_name} {package.pkg_version}")
            package.bump()
            package.hash = package.create_hash()
            log.debug(f"New hash: {package.package_name} {package.pkg_version} {package.hash}")
            if not is_dryrun:
                package.build()
                package.publish()
                db.add(package.to_json())
                db.commit()
        else:
            log.info(f"No changes to package : {package.package_name} {package.pkg_version}")

        package.clean()


# ######################################
# micropython-core-stubs
# ######################################
# todo: Publish: Integrate core stubs in publishing loop
version = "v0.1"
type = "core"


if 0:
    pkg_name = f"micropython-{type}-stubs"
    pkg_path = root_path / "publish" / pkg_name

    stubs: List[Tuple[str, Path]] = [
        ("Core Stubs", Path("./stubs") / "cpython_core-pycopy"),
    ]
    package = StubPackage(pkg_path, pkg_name, version, description="Micropython Core stubs", stubs=stubs)
    package.update_package_files()

    package.bump()
    package.build()
    package.publish()
    package.clean()


# ######################################
# micropython-doc-stubs
# ######################################
# todo : Publish: Integrate doc stubs in publishing loop
version = "v1.18"
type = "doc"
ver_flat = clean_version(version, flat=True)

if 0:
    pkg_name = f"micropython-doc-stubs"
    pkg_path = root_path / "publish" / pkg_name

    stubs: List[Tuple[str, Path]] = [
        ("Doc Stubs", Path("./stubs") / f"micropython-{ver_flat}-docstubs"),
    ]

    package = StubPackage(pkg_path, pkg_name, version, description="Micropython Doc Stubs", stubs=stubs)
    package.update_package_files()

    package.bump()
    package.build()
    package.publish()
    package.clean()
