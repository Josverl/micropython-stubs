"""
System specific functions.

MicroPython module: https://docs.micropython.org/en/v1.21.0/library/sys.html

CPython module: :mod:`python:sys` https://docs.python.org/3/library/sys.html .

---
Module: 'usys' on micropython-v1.21.0-esp8266-ESP8266_GENERIC
"""

# MCU: {'version': '1.21.0', 'mpy': 'v6.1', 'port': 'esp8266', 'board': 'ESP8266_GENERIC', 'family': 'micropython', 'build': '', 'arch': 'xtensa', 'ver': '1.21.0', 'cpu': 'ESP8266'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete
from typing import Dict, List, Tuple

path: list = []
modules: dict = {}
version_info: tuple = ()
platform: str = "esp8266"
version: str = "3.4.0; MicroPython v1.21.0 on 2023-10-05"
byteorder: str = "little"
argv: list = []
maxsize: int = 2147483647
implementation: tuple = ()

def exit(
    retval=0,
) -> Incomplete:
    """
    Terminate current program with a given exit code. Underlyingly, this
    function raise as `SystemExit` exception. If an argument is given, its
    value given as an argument to `SystemExit`.
    """
    ...

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

stderr: Incomplete  ## <class 'FileIO'> = <io.FileIO 2>
stdout: Incomplete  ## <class 'FileIO'> = <io.FileIO 1>
stdin: Incomplete  ## <class 'FileIO'> = <io.FileIO 0>
