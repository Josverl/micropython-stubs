"""
System specific functions.

MicroPython module: https://docs.micropython.org/en/v1.25.0/library/sys.html

CPython module: :mod:`python:sys` https://docs.python.org/3/library/sys.html .

---
Module: 'sys' on micropython-v1.24.1-esp32-ESP32_GENERIC_C6
"""

# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'esp32', 'board': 'ESP32_GENERIC_C6', 'cpu': 'ESP32C6', 'mpy': 'v6.3', 'arch': 'rv32imc'}
# Stubber: v1.24.0
from __future__ import annotations
from _typeshed import Incomplete
from typing import Dict, List, Tuple
from typing_extensions import Awaitable, TypeAlias, TypeVar

platform: str = "esp32"
version_info: tuple = ()
path: list = []
version: str = "3.4.0; MicroPython v1.24.1 on 2024-11-29"
ps1: str = ">>> "
ps2: str = "... "
byteorder: str = "little"
modules: dict = {}
argv: list = []
implementation: tuple = ()
maxsize: int = 2147483647

def print_exception(exc, file=stdout, /) -> None:
    """
    Print exception with a traceback to a file-like object *file* (or
    `sys.stdout` by default).

    Admonition:Difference to CPython
       :class: attention

       This is simplified version of a function which appears in the
       ``traceback`` module in CPython. Unlike ``traceback.print_exception()``,
       this function takes just exception value instead of exception type,
       exception value, and traceback object; *file* argument should be
       positional; further arguments are not supported. CPython-compatible
       ``traceback`` module can be found in `micropython-lib`.
    """
    ...

def exit(retval=0, /) -> Incomplete:
    """
    Terminate current program with a given exit code. Underlyingly, this
    function raises a `SystemExit` exception. If an argument is given, its
    value given as an argument to `SystemExit`.

    On embedded ports (i.e. all ports but Windows and Unix), an unhandled
    `SystemExit` currently causes a :ref:`soft_reset` of MicroPython.
    """
    ...

stderr: Incomplete  ## <class 'TextIOWrapper'> = <io.TextIOWrapper 2>
stdout: Incomplete  ## <class 'TextIOWrapper'> = <io.TextIOWrapper 1>
stdin: Incomplete  ## <class 'TextIOWrapper'> = <io.TextIOWrapper 0>
