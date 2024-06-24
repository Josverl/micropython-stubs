"""
System specific functions.

MicroPython module: https://docs.micropython.org/en/v1.21.0/library/sys.html

CPython module: :mod:`python:sys` https://docs.python.org/3/library/sys.html .

---
Module: 'usys' on micropython-v1.21.0-samd-SEEED_WIO_TERMINAL
"""

from __future__ import annotations

# MCU: {'family': 'micropython', 'version': '1.21.0', 'build': '', 'ver': 'v1.21.0', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'cpu': 'SAMD51P19A', 'mpy': 'v6.1', 'arch': 'armv7emsp'}
# Stubber: v1.16.2
from _typeshed import Incomplete
from typing import Dict, List, Tuple

platform = "samd"  # type: str
version_info = ()  # type: tuple
path = []  # type: list
version = "3.4.0; MicroPython v1.21.0 on 2023-10-06"  # type: str
ps1 = ">>> "  # type: str
ps2 = "... "  # type: str
byteorder = "little"  # type: str
modules = {}  # type: dict
argv = []  # type: list
implementation = ()  # type: tuple
maxsize = 2147483647  # type: int


def print_exception(
    exc,
    file=stdout,
) -> None:
    """
    Print exception with a traceback to a file-like object *file* (or
    `sys.stdout` by default).

    Difference to CPython

       This is simplified version of a function which appears in the
       ``traceback`` module in CPython. Unlike ``traceback.print_exception()``,
       this function takes just exception value instead of exception type,
       exception value, and traceback object; *file* argument should be
       positional; further arguments are not supported. CPython-compatible
       ``traceback`` module can be found in `micropython-lib`.
    """
    ...


def exit(
    retval=0,
) -> Incomplete:
    """
    Terminate current program with a given exit code. Underlyingly, this
    function raise as `SystemExit` exception. If an argument is given, its
    value given as an argument to `SystemExit`.
    """
    ...


stderr: Incomplete  ## <class 'FileIO'> = <io.FileIO 2>
stdout: Incomplete  ## <class 'FileIO'> = <io.FileIO 1>
stdin: Incomplete  ## <class 'FileIO'> = <io.FileIO 0>
