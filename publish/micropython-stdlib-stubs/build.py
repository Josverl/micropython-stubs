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
from mpflash.versions import clean_version, get_stable_mp_version
from stubber.codemod.enrich import enrich_file, enrich_folder
from stubber.modcat import STDLIB_ONLY_MODULES
from stubber.utils import do_post_processing
from stubber.utils.config import readconfig

# these modules will be kept in the stdlib folder
STDLIB_MODULES_TO_KEEP = list(
    set(STDLIB_ONLY_MODULES)
    | set(
        [
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
            "array",
            "builtins",
            "io",
            "re",
            # "socket",
            "sys",
            "types",
            "typing_extensions",
            "typing",
            "tls",
            "ssl",
            "enum",
            # "functools",
            # "queue",
            # "selectors",
            "sre_compile",
            "sre_constants",
            "sre_parse",
        ]
    )
)


# try to limit the "overspeak" of python modules to the bare minimum
STDLIB_MODULES_TO_REMOVE = [
    "os/path.pyi",
    "sys/_monitoring.pyi",
    #
    "asyncio/subprocess.pyi",
    "asyncio/base_subprocess.pyi",
    "asyncio/taskgroups.pyi",
    "asyncio/taskgroups.pyi",
    "asyncio/windows_events.pyi",
    "asyncio/windows_utils.pyi",
    #
    "json/decoder.pyi",
    "json/encoder.pyi",
    "json/tool.pyi",
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

# comment out some lines to hide the existance of CPython apis that do not exists in MicroPython
COMMENT_OUT_LINES = [
    ("asyncio", ["from .subprocess import *"]),
    (
        "os",
        [
            "from . import path as _path",
            "def _exit(status: int) -> NoReturn: ...",
        ],
    ),
]

# change some lines to hide the existance of CPython apis that do not exists in MicroPython
# this is for things such as function or classdefs that extend beyond a single line
CHANGE_LINES = [
    ("ssl", [("def create_default_context", "def __mpy_has_no_create_default_context")]),
    (
        "sys",
        [
            ("def atexit(", "def __mpy_has_no_atexit("),
            (
                "implementation: _implementation",
                "implementation: _mp_implementation",
            ),  # TODO : simplify by merging attribute types.
        ],
    ),
]


@dataclass
class Boost:
    """
    Boost class for enriching stdlib-stubs with information from MicroPython-stubs.

    Attributes:
        stub_name (str): The name of the stub file in stdlib.
        docstub (str): The name of the docstub file in docstubs, or empty if no enrichment is needed.
        file (Union[Path, str]): The name of the file in stdlib, or empty if it is the same as stub_name.
        all (List[str]): The __all__ list to use for the module, or empty if no update is needed.
    """

    stub_name: str
    source: str = ""
    target: Union[Path, str] = ""
    all: List[str] = field(default_factory=list)

    def __post_init__(self):
        self.source = self.source or self.stub_name
        self.target = Path("stdlib") / (self.target or self.stub_name)


# match "var: type",
re_var_typ = re.compile(r"^([\w\_]+)\s*:\s*\w+")
# match var= value
re_var_val = re.compile(r"^([\w\_]+)\s*=\s*\w+")


def find_toplevel_vars(module: Path) -> set:
    """Find the top level variables defined in a module."""
    keep = set()
    if module.is_dir():
        module = module / "__init__.pyi"
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
    if module.is_dir():
        module = module / "__init__.pyi"
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
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.readlines()
        with open(file_path, "w", encoding="utf-8") as f:
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


def change_lines(folder: Path):
    """used to make changes to the names of functions in the stdlib stubs to hide the
    existance of CPython apis that do not exists in MicroPython.
    todo: replace functionality by libcst codemod for a more robust implementation
    """
    n = 0
    for mod, lines in CHANGE_LINES:
        file_path = folder / mod / "__init__.pyi"
        if not file_path.exists():
            file_path = folder / f"{mod}.pyi"
            if not file_path.exists():
                continue
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.readlines()
        with open(file_path, "w", encoding="utf-8") as f:
            for line in content:
                _line = line
                for old, new in lines:
                    if old in _line:
                        line = line.replace(old, new)
                        n += 1
                f.write(line)


def update_typing_pyi(
    dist_stdlib_path: Path,
):
    """
    patch updates into typing.pyi
    - allow IO.write(bytes) overload
    """
    tsk = enrich_file(
        dist_stdlib_path / "handcrafted/typing.pyi",
        dist_stdlib_path / "stdlib/typing.pyi",
        diff=True,
        write_back=True,
        copy_params=True,
        copy_docstr=True,
    )
    next(tsk)


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
    boardstub_path: Path,
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
            all=["OrderedDict", "defaultdict", "deque", "namedtuple"],
        ),
        Boost("os"),
        Boost("sys"),
        Boost("ssl"),
        Boost("io"),
        Boost("array"),
        # evaluating
        # Boost("tls"), # -- MicroPython only - does not exists in stdlib
        Boost("socket"),  # not available in all boards ...
        Boost("json"),
        Boost("struct"),
        Boost("builtins"),
    ]

    for boost in boosts:
        source_path = docstubs_path / boost.source
        target_path = dist_stdlib_path / boost.target
        if not source_path.exists():
            log.warning(f"Docstub {source_path} does not exist")
            continue
        if not target_path.exists():
            if target_path.with_suffix(".pyi").exists():
                target_path = target_path.with_suffix(".pyi")
            else:
                continue
        log.info(f"Enriching {target_path}")
        result = enrich_folder(
            source_path,  # source
            target_path,  # desr
            show_diff=show_diff,
            write_back=write_back,
            ext=".pyi",
            copy_params=True,
            copy_docstr=True,
        )
        if boost.all:
            update_public_interface(boost, target_path)
        if boost.source:
            # read the toplevel vars from the docstub and firmware stubs
            keep = find_toplevel_vars(docstubs_path / boost.source)
            keep.update(find_toplevel_vars(boardstub_path / boost.source))
            if "io" in boost.stub_name:
                keep.add("open")  # open is not in the io docstub
            update_module_vars(target_path, keep)

        if result:
            log.info(f"Enriched {target_path}")


def update_public_interface(boost: Boost, module_path: Path):
    """
    Update the public interface (__all__) of a module.
    Uses very basic parsing - just replace the __all__ line with the new one.

    Args:
        boost (Boost): The Boost object containing the module information.
        module_path (Path): The path to the module file.
    """
    # TODO: fragile, replace by libcst codemod
    if module_path.is_dir():
        module_path = module_path / "__init__.pyi"
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


def update_mpy_shed(rootpath: Path, dist_stdlib_path: Path):
    """
    Update the _mpy_shed from the reference stubs.
    """
    log.info("Update _mpy_shed from the reference stubs")
    shutil.rmtree(dist_stdlib_path / "_mpy_shed", ignore_errors=True)
    shutil.copytree(
        rootpath / "reference/_mpy_shed",
        dist_stdlib_path / "_mpy_shed",
        dirs_exist_ok=True,
    )


def update_asyncio_manual(dist_stdlib_path: Path):
    """
    Update the asyncio stubs from the manual updated copy.
    """
    log.info("Update asyncio stubs from handcrafted copy")
    src_asyncio = dist_stdlib_path / "handcrafted/asyncio"
    dst_asyncio = dist_stdlib_path / "stdlib/asyncio"
    shutil.rmtree(dst_asyncio, ignore_errors=True)
    shutil.copytree(src_asyncio, dst_asyncio, dirs_exist_ok=True)


@click.command()
@click.option("--clone", "-c", help="Clone the typeshed repo.", default=False, show_default=True)
@click.option(
    "--version",
    "-v",
    type=str,
    help="Specify Micropython version",
    default="1.24.1",
    show_default=True,
)
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
def update(
    version: Optional[str] = None,
    clone: bool = False,
    typeshed: bool = False,
    merge: bool = True,
    build: bool = True,
):
    """
    Update the micropython-stdlib-stubs package and create a wheel file.
    """
    # Read from CONFIG, from a parent's pyproject.toml
    CONFIG = readconfig(Path(__file__).parent.parent)

    log.info(CONFIG.config_path)
    # print(repr(CONFIG))
    if not version:
        version = get_stable_mp_version()

    flat_version = clean_version(version, flat=True, drop_v=False)
    log.info(f"Build micropython-stdlib-stubs for version: {version}")

    rootpath = CONFIG.config_path
    # if not rootpath.is_absolute() and CONFIG.config_path:
    #     rootpath = CONFIG.config_path / rootpath

    log.info(f"Using rootpath: {rootpath}")

    dist_stdlib_path = rootpath / "publish/micropython-stdlib-stubs"
    docstubs_path = rootpath / f"stubs/micropython-{flat_version}-docstubs"
    boardstub_path = rootpath / f"stubs/micropython-{flat_version}-esp32-ESP32_GENERIC"
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
        print("git clone https://github.com/python/typeshed.git\ncd typeshed\ngit checkout <commit-hash>")
        log.warning("Not implemented yet")

    if typeshed:
        update_stdlib_from_typeshed(dist_stdlib_path, typeshed_path)

    ## always update the _mpy_shed
    update_mpy_shed(rootpath, dist_stdlib_path)
    ## always update the asyncio stubs
    update_asyncio_manual(dist_stdlib_path)

    if merge:
        merge_docstubs_into_stdlib(
            dist_stdlib_path=dist_stdlib_path,
            docstubs_path=docstubs_path,
            boardstub_path=boardstub_path,
        )

    # tidy up the stubs
    do_post_processing([dist_stdlib_path / "stdlib"], stubgen=False, black=True, autoflake=True)

    # remove typerchecker noise from typeshed ,
    # so that the actual issues caused by micropython stubs are more visible
    add_type_ignore(dist_stdlib_path / "stdlib")

    # comment out some lines that cause issues
    comment_out_lines(dist_stdlib_path / "stdlib")

    # hide cpython APIs by renaming defs in the stdlib stubs
    change_lines(dist_stdlib_path / "stdlib")

    # update the last changed date-time so uv can detect the update
    Path(dist_stdlib_path / "pyproject.toml").touch()

    # do some patches to typings.pyi
    update_typing_pyi(dist_stdlib_path)

    if build:
        subprocess.check_call(
            # ["uv", "build", "--wheel"],
            ["uv", "build", "--index-strategy", "unsafe-best-match", "--wheel"],
            cwd=dist_stdlib_path,
        )


if __name__ == "__main__":
    update()
