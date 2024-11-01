"""
Update the micropython-stlib-stubs 
- based on typeshed 
- merged with (some) micropython documentation.`

"""

import re
import shutil
import subprocess
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Union

import rich_click as click
from loguru import logger as log
from stubber.codemod.enrich import enrich_folder
from stubber.utils import do_post_processing
from stubber.utils.config import CONFIG

STDLIB_MODULES_TO_KEEP = [
    "_typeshed",
    "asyncio",
    "collections",
    "sys",
    "os",
    "__future__",
    "_ast",
    "_codecs",
    "_collections_abc",
    "_decimal",
    "abc",
    "builtins",
    "io",
    "re",
    # "socket",
    "sys",
    "types",
    "typing_extensions",
    "typing",
    "ssl",
    "enum",
    # "functools",
    # "queue",
    # "selectors",
    "sre_compile",
    "sre_constants",
    "sre_parse",
]

# try to limit the "overspeak" of python modules to the bare minimum
STDLIB_MODULES_TO_REMOVE = [
    "os/path.pyi",
    "sys/_monitoring.pyi",
    "asyncio/subprocess.pyi",
    "asyncio/base_subprocess.pyi",
    "asyncio/taskgroups.pyi",
    "asyncio/taskgroups.pyi",
    "asyncio/windows_events.pyi",
    "asyncio/windows_utils.pyi",
]


TYPE_IGNORES = [
    # cannot be based on itself
    ("os", ["path = _path"]),
    # reportAttributeAccessIssue
    ("asyncio/taskgroups", [": Context", "from contextvars import Context"]),
    ("asyncio/base_events", [": Context", "from contextvars import Context"]),
    ("asyncio/base_futures", [": Context", "from contextvars import Context"]),
    ("asyncio/events", [": Context", "from contextvars import Context"]),
    ("asyncio/runners", [": Context", "from contextvars import Context"]),
    # reportInvalidTypeArguments
    ("_typeshed", ["Field[Any]"]),
    # reportArgumentType Literal not assignable to [type]
    (
        "builtins",
        [
            ": int = -1",
            ": int = 0",
            " | None = None",
            ": bool = True",
            ": bool = False",
            ': str | None = "',
            ': str = "',
            '| bytearray = b"',
            ': bytes = b"',
        ],
    ),
    (
        "collections",
        [
            "deque[_T]",  #  Expected no type arguments for class
            "OrderedDict[",  #  Expected no type arguments for class "OrderedDict"
            "class deque(stdlib_deque):",
            "class OrderedDict(stdlib_OrderedDict):",
            ": _T, /",  ## TypeVar appears only once in generic function signature
            "[_KT, _VT]",  # TypeVar appears only once in generic function signature
            ": _T,",  # TypeVar appears only once in generic function signature
            ": _KT,",  # TypeVar appears only once in generic function signature
            ": _VT,",  # TypeVar appears only once in generic function signature
            "-> _T:",  # TypeVar appears only once in generic function signature
            "-> _KT:",  # TypeVar appears only once in generic function signature
            "-> _VT:",  # TypeVar appears only once in generic function signature
            "Iterator[_T]",
            "Iterator[_KT]",
        ],
    ),
    ("io", ["from io import *"]),
]

COMMENT_OUT_LINES = [
    ("asyncio", ["from .subprocess import *"]),
]


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


# match "var: type",
re_var_typ = re.compile(r"^([\w\_]+)\s*:\s*\w+")
# match var= value
re_var_val = re.compile(r"^([\w\_]+)\s*=\s*\w+")


def find_toplevel_vars(module: Path) -> set:
    """Find the top level variables defined in a module."""
    keep = set()
    if not module.exists():
        return keep
    with open(module, "r", encoding="utf-8") as f:
        for line in f.readlines():
            if match := re_var_typ.match(line):
                keep.add(match.group(1))
            elif match := re_var_val.match(line):
                keep.add(match.group(1))
    return keep


def update_module_vars(module: Path, keep: set):
    """
    Update the module top level  variables to only keep the ones
    in the `keep` set or starting with _ .
    """
    with open(module, "r", encoding="utf-8") as f:
        lines = f.readlines()
    with open(module, "w", encoding="utf-8") as f:
        for line in lines:
            if match := re_var_typ.match(line):
                if match.group(1) in keep or match.group(1).startswith("_"):
                    f.write(line)
                else:
                    f.write(f"# {line}")
            elif match := re_var_val.match(line):
                if match.group(1) in keep or match.group(1).startswith("_"):
                    f.write(line)
                else:
                    f.write(f"# {line}")
            else:
                f.write(line)


def add_type_ignore(folder: Path):
    """Add type ignores to some of the lines in the _typeshed stubs."""
    n = 0
    for mod, lines in TYPE_IGNORES:
        file_path = folder / mod / "__init__.pyi"
        if not file_path.exists():
            file_path = folder / f"{mod}.pyi"
            if not file_path.exists():
                continue
        with open(file_path, "r") as f:
            content = f.readlines()
        with open(file_path, "w") as f:
            for line in content:
                _line = line.rstrip("\n")
                for ignore in lines:
                    if ignore in _line and not _line.endswith("# type: ignore"):
                        f.write(f"{_line}  # type: ignore\n")
                        n += 1
                        break
                else:
                    f.write(line)
    log.info(f"Added {n} type ignores to {folder}")


def comment_out_lines(folder: Path):
    n = 0
    for mod, lines in COMMENT_OUT_LINES:
        file_path = folder / mod / "__init__.pyi"
        if not file_path.exists():
            file_path = folder / f"{mod}.pyi"
            if not file_path.exists():
                continue
        with open(file_path, "r") as f:
            content = f.readlines()
        with open(file_path, "w") as f:
            for line in content:
                _line = line.rstrip("\n")
                for ignore in lines:
                    if ignore in _line and not _line.startswith("#"):
                        f.write(f"# {line}")
                        n += 1
                        break
                else:
                    f.write(line)

    log.info(f"Commented out {n} lines in {folder}")


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
        f.write("# This file contains the commit hash of typeshed used to generate the stubs\n")
        f.write(f"# https://github.com/python/typeshed/tree/{typeshed_commit_hash.decode('utf-8')}\n")
        f.write(f"{typeshed_commit_hash.decode('utf-8')}\n")

    log.info("Clean up extraneous folders from stdlib")
    for fldr in pkg_stdlib_path.glob("*"):
        if fldr.is_dir() and fldr.stem not in STDLIB_MODULES_TO_KEEP:
            shutil.rmtree(fldr)
            time.sleep(0.1)

    log.info("Clean up extraneous stubs from stdlib")
    for stub in pkg_stdlib_path.glob("*.pyi"):
        if stub.stem not in STDLIB_MODULES_TO_KEEP:
            # print(f"Removing {stub.stem}")
            stub.unlink()

    for name in STDLIB_MODULES_TO_REMOVE:
        if (pkg_stdlib_path / name).exists():
            (pkg_stdlib_path / name).unlink()


def merge_docstubs_into_stdlib(
    *,
    dist_stdlib_path: Path,
    docstubs_path: Path,
    boardstub_path: Optional[Path] = None,
    dry_run=False,
):
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
        Boost("sys", "sys.pyi", "sys/__init__.pyi"),
        Boost("ssl", "ssl.pyi", "ssl.pyi"),
        # TODO: add ssl.SSLContext.load_cert_chain
        Boost("io", "io.pyi", "io.pyi"),
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
            if boost.docstub:
                # read the toplevel vars from the docstub and firmware stubs
                keep = find_toplevel_vars(docstubs_path / boost.docstub)
                keep.update(find_toplevel_vars(boardstub_path / boost.docstub))
                if "io" in boost.stub_name:
                    keep.add("open")  # open is not in the io docstub
                update_module_vars(module_path, keep)

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
        found_all = False
        for i, line in enumerate(lines):
            if line.startswith("__all__ = "):
                lines[i] = f"__all__ = {repr(boost.all)}\n"
                found_all = True
        if not found_all:
            lines.append(f"__all__ = {repr(boost.all)}\n")
        with open(module_path, "w") as f:
            f.writelines(lines)
    except Exception as e:
        log.error(f"Failed to update __all__ in {module_path}: {e}")


@click.command()
@click.option("--clone", "-c", help="Clone the typeshed repo.", default=False, show_default=True)
@click.option(
    "--typeshed",
    "-t",
    is_flag=True,
    help="Update stdlib from the typeshed repo.",
    default=True,
    show_default=True,
)
@click.option(
    "--merge",
    "-m",
    is_flag=True,
    help="Merge the docstubs into the stdlib.",
    default=True,
    show_default=True,
)
@click.option("--build", "-b", is_flag=True, help="Build the wheel file.", default=True, show_default=True)
def update(clone: bool = False, typeshed: bool = False, merge: bool = True, build: bool = True):
    """
    Update the stdlib and create a wheel file.
    """
    # TODO: Read from CONFIG
    rootpath = Path(__file__).parent.parent.parent
    log.info(f"using rootpath: {rootpath}")
    dist_stdlib_path = rootpath / "publish/micropython-stdlib-stubs"
    docstubs_path = rootpath / "stubs/micropython-v1_23_0-docstubs"
    boardstub_path = rootpath / "stubs/micropython-v1_23_0-esp32-ESP32_GENERIC"
    typeshed_path = rootpath / "repos/typeshed"

    # check that the paths exist
    assert rootpath.exists(), f"rootpath {rootpath} does not exist"
    assert dist_stdlib_path.exists(), f"dist_stdlib_path {dist_stdlib_path} does not exist"
    assert docstubs_path.exists(), f"docstubs_path {docstubs_path} does not exist"
    assert boardstub_path.exists(), f"boardstub_path {boardstub_path} does not exist"
    assert typeshed_path.exists(), f"typeshed_path {typeshed_path} does not exist"

    if clone:
        # TODO
        # clone typeshed if needed and switch to the correct hash
        print("in the repos folder run:")
        print("git clone https://github.com/python/typeshed.git")
        log.warning("Not implemented yet")

    if typeshed:
        update_stdlib_from_typeshed(dist_stdlib_path, typeshed_path)

    if merge:
        merge_docstubs_into_stdlib(
            dist_stdlib_path=dist_stdlib_path,
            docstubs_path=docstubs_path,
            boardstub_path=boardstub_path,
        )

    # tidy up the stubs
    do_post_processing([dist_stdlib_path], stubgen=False, black=True, autoflake=True)

    # remove typerchecker noise from typeshed ,
    # so that the actual issues caused by micropython stubs are more visible
    add_type_ignore(dist_stdlib_path / "stdlib")

    # comment out some lines that cause issues
    comment_out_lines(dist_stdlib_path / "stdlib")

    if build:
        subprocess.check_call(["poetry", "build"], cwd=dist_stdlib_path)


if __name__ == "__main__":
    # find_toplevel_vars(Path(r"C:\develop\MyPython\micropython-stubs\publish\micropython-v1_22_0-esp32-stubs\sys.pyi"))
    update()
