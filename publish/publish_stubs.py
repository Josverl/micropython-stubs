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
|     +--README.md
|     +--LICENSE.md
|  +--<folder for each package>
|     +--<package name> double nested to match the folder structure
|  +--<family>-version-<port>-<board>-<type>-stubs
|  +--micropython-v1_18-esp32-stubs
|  +--micropython-v1_18-stm32-stubs
|  +--micropython-v1_19_1-stm32-stubs
|  +-- ...
|


!!Note: anything excluded in .gitignore is not packaged by poetry
"""

from pathlib import Path
from typing import Dict, List, Tuple, Union

from stubber.utils.versions import clean_version

from pysondb import PysonDB

from stubpacker import StubPackage
from packaging.version import parse

from loguru import logger as log
import sys
import click

# replace std log handler with a custom one capped on INFO level
log.remove()
log.add(sys.stderr, level="INFO", backtrace=True, diagnose=True)

ALL_TYPES = ["combo", "doc", "core"]
COMBINED = ALL_TYPES[0]
DOC_STUBS = ALL_TYPES[1]
CORE_STUBS = ALL_TYPES[2]


def package_name(
    port: str = "", board: str = "", pkg=COMBINED, family="micropython"
) -> str:
    "generate a package name"
    if pkg == COMBINED:
        # # {family}-{port}-{board}-stubs
        return f"{family}-{port}-{board}-stubs".lower().replace(
            "-generic-stubs", "-stubs"
        )
    elif pkg == DOC_STUBS:
        return f"{family}-doc-stubs".lower()

    raise NotImplementedError(port, board, pkg)


# def package_path(port, board, mpy_version, pub_path: Path, pkg=COMBINED, family="micropython") -> Path:
#     "generate a package name"
#     return pub_path / package_name( port, board, pkg, family)


def get_package(
    db: PysonDB, pub_path: Path, mpy_version: str, pkg_name: str
) -> Union[StubPackage, None]:
    "get package from db or create a new one"
    # find in the database
    recs = db.get_by_query(
        query=lambda x: x["mpy_version"] == mpy_version and x["name"] == pkg_name
    )
    # dict to list
    recs = [{"id": key, "data": recs[key]} for key in recs]
    # sort
    packages = sorted(recs, key=lambda x: parse(x["data"]["pkg_version"]))

    [
        log.debug(
            f"{x['data']['name']} - {x['data']['mpy_version']} - {x['data']['pkg_version']}"
        )
        for x in packages
    ]
    if len(packages) > 0:
        pkg_from_db = packages[-1]["data"]
        log.info(f"Found latest {pkg_name} == {pkg_from_db['pkg_version']}")
        return pkg_from_db
    else:
        return None


def create_package(
    pkg_path: Path,
    pkg_name: str,
    mpy_version: str,
    port: str = "",
    board: str = "",
    family: str = "micropython",
    pkg_type=COMBINED,
) -> StubPackage:
    "create and initialize a package with the correct sources"
    package = None
    if pkg_type == COMBINED:
        assert port != ""
        assert board != ""
        ver_flat = clean_version(mpy_version, flat=True)

        stubs: List[Tuple[str, Path]] = [
            ("Firmware stubs", Path("./stubs") / f"{family}-{ver_flat}-{port}"),
            (
                "Frozen stubs",
                Path("./stubs") / f"{family}-{ver_flat}-frozen" / port / board,
            ),
            ("Core Stubs", Path("./stubs") / "cpython_core-pycopy"),
        ]
        package = StubPackage(pkg_path, pkg_name, mpy_version, stubs=stubs)
    elif pkg_type == DOC_STUBS:
        # TODO add doc stubs
        ver_flat = clean_version(mpy_version, flat=True)

        stubs: List[Tuple[str, Path]] = [
            ("Doc stubs", Path("./stubs") / f"{family}-{ver_flat}-docstubs"),
        ]
        package = StubPackage(pkg_path, pkg_name, mpy_version, stubs=stubs)

    elif pkg_type == CORE_STUBS:
        # TODO add core stubs
        raise NotImplementedError(type)
    else:
        raise NotImplementedError(type)

    return package


# ######################################
# micropython-doc-stubs
# ######################################
# todo : Publish: Integrate doc stubs in publishing loop


def publish_doc_stubs(
    versions: List[str],
    pub_path: Path,
    db: PysonDB,
    family="micropython",
    production=False,  # PyPI or Test-PyPi
    dryrun=False,  # don't publish , dont save to the database
    force=False,  # publish even if no changes
    clean: bool = False,  # clean up afterards
):

    for mpy_version in versions:
        pkg_type = DOC_STUBS
        ver_flat = clean_version(mpy_version, flat=True)
        # package name for firmware package
        # pkg_name = f"micropython-doc-stubs"
        pkg_name = package_name(family=family, pkg=pkg_type)
        pkg_path = pub_path / pkg_name
        log.info("=" * 40)

        package = get_package(db, pub_path, mpy_version, pkg_name=pkg_name)
        if not package:
            log.warning(f"No package found for {pkg_name}")
            package = create_package(
                pub_path, pkg_name, mpy_version, pkg_type=DOC_STUBS
            )
            continue
        stubs: List[Tuple[str, Path]] = [
            ("Doc Stubs", Path("./stubs") / f"micropython-{ver_flat}-doc-stubs"),
        ]

        package = StubPackage(
            pkg_path,
            pkg_name,
            mpy_version,
            description="Micropython Doc Stubs",
            stubs=stubs,
        )

        # /////////////////////////
        # dit kan hergebruikt worden

        package.update_package_files()
        package.update_included_stubs()
        package.check()

        # If there are changes to the package, then publish it
        if not (package.is_changed() or force):
            log.info(
                f"No changes to package : {package.package_name} {package.pkg_version}"
            )
        else:
            if not force:
                log.info(
                    f"Found changes to package : {package.package_name} {package.pkg_version} {package.hash} != {package.create_hash()}"
                )
            ## TODO: get last published version.postXXX from PyPI and update version if different
            package.bump()
            package.hash = package.create_hash()
            log.debug(
                f"New hash: {package.package_name} {package.pkg_version} {package.hash}"
            )
            if dryrun:
                log.warning("Updated package is NOT published.")
            else:
                package.build()
                package.publish(production=production)
                db.add(package.to_json())
                db.commit()

        if clean:
            package.clean()


def publish_board_stubs(
    versions: List[str],
    ports: List[str],
    boards: List[str],
    db: PysonDB,
    pub_path: Path,
    pkg_type=COMBINED,
    family: str = "micropython",
    production=False,  # PyPI or Test-PyPi
    dryrun=False,  # don't publish , dont save to the database
    force=False,  # publish even if no changes
    clean: bool = False,  # clean up afterards
):
    for mpy_version in versions:
        for port in ports:

            # Firmware Stubber MUST report "stm32" for a pyboard
            for board in boards:
                # package name for firmware package
                pkg_name = package_name(port, board)
                log.info("=" * 40)

                package = get_package(db, pub_path, mpy_version, pkg_name)
                if not package:
                    log.warning(f"No package found for {pkg_name}")
                    package = create_package(
                        pub_path,
                        pkg_name,
                        mpy_version,
                        port,
                        board,
                        family,
                        pkg_type=pkg_type,
                    )
                    continue

                # check if the sources exist
                OK = True
                for (name, path) in package.stub_sources:
                    if not path.exists():
                        log.warning(f"{pkg_name}: source {name} does not exist: {path}")
                        OK = False
                if not OK:
                    log.warning(f"{pkg_name}: skipping as source stubs are missing")

                    package._publish = False
                    continue

                # /////////////////////////
                # dit kan hergebruikt worden

                package.update_package_files()
                package.update_included_stubs()
                package.check()

                # If there are changes to the package, then publish it
                if not (package.is_changed() or force):
                    log.info(
                        f"No changes to package : {package.package_name} {package.pkg_version}"
                    )
                else:
                    if not force:
                        log.info(
                            f"Found changes to package : {package.package_name} {package.pkg_version} {package.hash} != {package.create_hash()}"
                        )
                    ## TODO: get last published version.postXXX from PyPI and update version if different
                    package.bump()
                    package.hash = package.create_hash()
                    log.debug(
                        f"New hash: {package.package_name} {package.pkg_version} {package.hash}"
                    )
                    if dryrun:
                        log.warning("Updated package is NOT published.")
                    else:
                        package.build()
                        package.publish(production=production)
                        db.add(package.to_json())
                        db.commit()

                if clean:
                    package.clean()


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# ######################################
# CLI
# ######################################

LAST_VERSION = "1.19.1"
ALL_VERSIONS = ["1.17", "1.18", "1.19", "1.19.1"]  # "1.14", "1.15", "1.16","1.17",
ALL_PORTS = ["stm32", "esp32", "esp8266", "rp2"]
ALL_BOARDS = ["GENERIC"]


@click.command()
@click.option("--family", default="micropython", type=str, show_default=True)
@click.option(
    "--version",
    "--Version",
    "-V",
    "versions",
    multiple=True,
    default=[LAST_VERSION],
    # type=click.Choice(ALL_VERSIONS),
    show_default=True,
    help="multiple: ",
)
@click.option(
    "--port",
    "-p",
    "ports",
    multiple=True,
    default=ALL_PORTS,
    type=click.Choice(ALL_PORTS),
    show_default=True,
    help="multiple: ",
)
@click.option(
    "--board",
    "-b",
    "boards",
    multiple=True,
    default=ALL_BOARDS,
    type=click.Choice(ALL_BOARDS),
    show_default=True,
    help="multiple: ",
)
@click.option(
    "--pypi/--test-pypi",
    is_flag=True,
    default=False,
    prompt="Publish to PYPI (y) or Test-PYPI (n)",
    help="publish to PYPI or Test-PYPI",
)
@click.option(
    "--dry-run",
    "dryrun",
    is_flag=True,
    default=False,
    help="go though the motions but do not publish",
)
@click.option(
    "--force",
    is_flag=True,
    default=False,
    help="create new post release even if no changes detected",
)
@click.option(
    "--clean",
    is_flag=True,
    default=False,
    help="clean folders after processing and publishing",
)
@click.option(
    "--type",
    "-t",
    "stub_type",
    default=ALL_TYPES[0],
    type=click.Choice(ALL_TYPES),
    help="stub type to publish",
)
@click.option("-v", "--verbose", count=True)
#
def cli_publish(
    family, versions, ports, boards, pypi, dryrun, force, verbose, clean, stub_type: str
):
    """Commandline interface to publish stubs."""
    # force overrules dryrun
    if force:
        dryrun = False
    # lists please
    versions = list(versions)
    ports = list(ports)
    boards = list(boards)

    production = pypi

    root_path: Path = Path(".")
    db_path = (
        root_path / "publish" / f"package_data{'' if production else '_test'}.jsondb"
    )
    db = PysonDB(db_path.as_posix())
    if stub_type == "combo":
        publish_board_stubs(
            versions=versions,
            ports=ports,
            boards=boards,
            db=db,
            pub_path=root_path / "publish",
            family=family,
            production=production,
            dryrun=dryrun,
            clean=clean,
        )
    elif stub_type == "doc":
        publish_doc_stubs(
            versions=versions,
            db=db,
            pub_path=root_path / "publish",
            family=family,
            production=production,
            dryrun=dryrun,
            clean=clean,
        )
        pass
    # elif stub_type == "core":
    #     pass
    else:
        log.warning("unknown stub type :", stub_type)
        raise ValueError


# ######################################
# main
# ######################################

if __name__ == "__main__":

    cli_publish()


# ######################################
# micropython-core-stubs
# ######################################


# # todo: Publish: Integrate core stubs in publishing loop
# if 0:
#     version = "v0.1"
#     type = "core"

#     pkg_name = f"micropython-{type}-stubs"
#     pkg_path = root_path / "publish" / pkg_name

#     stubs: List[Tuple[str, Path]] = [
#         ("Core Stubs", Path("./stubs") / "cpython_core-pycopy"),
#     ]
#     package = StubPackage(pkg_path, pkg_name, version, description="Micropython Core stubs", stubs=stubs)
#     package.update_package_files()

#     package.bump()
#     package.build()
#     package.publish()
#     package.clean()
