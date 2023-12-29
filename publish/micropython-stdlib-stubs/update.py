"""
Update the micropython-stlib-stubs 
- based on typeshed 
- merged with (some) micropython documentation.`

"""

import shutil
import subprocess
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Union

from loguru import logger as log
from stubber.codemod.enrich import enrich_folder
from stubber.utils import do_post_processing
from stubber.utils.config import CONFIG

modules_to_keep = [
    "_typeshed",
    "asyncio",
    "collections",
    "sys",
    "os",
    # "json",
    "__future__",
    "_ast",
    "_codecs",
    "_collections_abc",
    "_decimal",
    "abc",
    "builtins",
    "io",
    "re",
    "socket",
    "sys",
    "types",
    "typing_extensions",
    "typing",
    "ssl",
    # TODO: TESTING NEEDED WHICH ONES ARE NEEDED
    # "codecs",
    # "contextlib",
    # "contextvars",
    # "dataclasses", # not in MicroPython
    # "decimal",
    "enum",
    # "fractions",
    "functools",
    # "numbers",
    "queue",
    "selectors",
    "sre_compile",
    "sre_constants",
    "sre_parse",
]


def update_stdlib_from_typeshed(dist_stdlib_path: Path, typeshed_path: Path):
    """
    Update the standard library from the typeshed folder.

    Args:
        dist_stdlib_path (Path): The path to the destination stdlib folder.
        typeshed_path (Path): The path to the typeshed folder.
    """
    pkg_stdlib_path = dist_stdlib_path / "stdlib"
    log.info("Clean up the stdlib folder")
    shutil.rmtree(pkg_stdlib_path, ignore_errors=True)
    time.sleep(1)

    log.info("Copy the typeshed folder to the stdlib")
    shutil.copytree(typeshed_path / "stdlib", pkg_stdlib_path, dirs_exist_ok=True)

    # get the commit hash of typeshed and save it to a file
    log.info("Save typeshed commit hash to file")
    typeshed_commit_hash = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=typeshed_path)
    with open(dist_stdlib_path / "typeshed_commit.txt", "w") as f:
        f.write(f"https://github.com/python/typeshed/tree/{typeshed_commit_hash.decode('utf-8')}")

    log.info("Clean up extraneous folders from stdlib")
    for fldr in pkg_stdlib_path.glob("*"):
        if fldr.is_dir() and fldr.stem not in modules_to_keep:
            shutil.rmtree(fldr)
            time.sleep(0.1)

    log.info("Clean up extraneous stubs from stdlib")
    for stub in pkg_stdlib_path.glob("*.pyi"):
        if stub.stem not in modules_to_keep:
            # print(f"Removing {stub.stem}")
            stub.unlink()

    # try to limit the "overspeak" of python modules to the bare minimum
    sub_modules_to_remove = [
        "os/path.pyi",
        "sys/_monitoring.pyi",
        "asyncio/subprocess.pyi",
        "asyncio/base_subprocess.pyi",
        "asyncio/taskgroups.pyi",
        "asyncio/taskgroups.pyi",
        "asyncio/windows_events.pyi",
        "asyncio/windows_utils.pyi",
    ]
    for name in sub_modules_to_remove:
        if (pkg_stdlib_path / name).exists():
            (pkg_stdlib_path / name).unlink()


@dataclass
class Boost:
    """
    Boost class for enriching stub files.

    Attributes:
        stub_name (str): The name of the stub file in stdlib.
        docstub (str): The name of the docstub file in docstubs, or empty if no enrichment is needed.
        file (Union[Path, str]): The name of the file in stdlib, or empty if it is the same as stub_name.
        all (List[str]): The __all__ list to use for the module, or empty if no update is needed.
    """

    stub_name: str
    docstub: str = ""
    file: Union[Path, str] = ""
    all: List[str] = field(default_factory=list)

    def __post_init__(self):
        self.file = Path("stdlib") / (self.file or self.stub_name + ".pyi")


def merge_docstubs_into_stdlib(*, dist_stdlib_path: Path, docstubs_path: Path, dry_run=True):
    """
    Merge docstubs into the stdlib.

    Args:
        dist_stdlib_path (Path): The path to the destination stdlib folder.
        docstubs_path (Path): The path to the docstubs folder.
        dry_run (bool, optional): Whether to perform a dry run or not. Defaults to True.
    """
    write_back = not dry_run
    show_diff = dry_run

    boosts = [
        Boost(
            "collections",
            "collections.pyi",
            "collections/__init__.pyi",
            all=["OrderedDict", "defaultdict", "deque", "namedtuple"],
        ),
        Boost(
            "sys",
            "sys.pyi",
            "sys/__init__.pyi",
            # all=["OrderedDict", "defaultdict", "deque", "namedtuple"],
        ),
        Boost(
            "ssl",
            "ssl.pyi",
            "ssl.pyi",
            # TODO: add ssl.SSLContext.load_cert_chain
        ),
    ]

    for boost in boosts:
        module_path = dist_stdlib_path / boost.file
        if module_path.exists():
            log.info(f"Enriching {module_path}")
            result = enrich_folder(
                module_path,
                docstubs_path,
                show_diff=show_diff,
                write_back=write_back,
                package_name=boost.stub_name,
            )
            if boost.all:
                update_public_interface(boost, module_path)

            if result:
                log.info(f"Enriched {module_path}")


def update_public_interface(boost: Boost, module_path: Path):
    """
    Update the public interface (__all__) of a module.
    Uses very basic parsing - just replace the __all__ line with the new one.

    Args:
        boost (Boost): The Boost object containing the module information.
        module_path (Path): The path to the module file.
    """
    # TODO: fragile, replace by libcst codemod
    try:
        with open(module_path, "r") as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            if line.startswith("__all__ = "):
                lines[i] = f"__all__ = {repr(boost.all)}\n"
        with open(module_path, "w") as f:
            f.writelines(lines)
    except Exception as e:
        log.error(f"Failed to update __all__ in {module_path}: {e}")


def update():
    """
    Update the stdlib and create a wheel file.
    """
    # TODO: Read from CONFIG
    rootpath = Path(__file__).parent.parent.parent
    dist_stdlib_path = rootpath / "publish/micropython-stdlib-stubs"
    docstubs_path = rootpath / "stubs/micropython-v1_21_0-docstubs"
    typeshed_path = rootpath / "repos/typeshed"
    update_stdlib_from_typeshed(dist_stdlib_path, typeshed_path)

    merge_docstubs_into_stdlib(dist_stdlib_path=dist_stdlib_path, docstubs_path=docstubs_path, dry_run=False)

    # tidy up the stubs
    do_post_processing([dist_stdlib_path], stubgen=False, black=True, autoflake=True)

    subprocess.check_call(["poetry", "build"], cwd=dist_stdlib_path)


if __name__ == "__main__":
    update()
    print("done")
