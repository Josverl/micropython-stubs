"""
System specific functions.

MicroPython module: https://docs.micropython.org/en/v1.23.0-preview/library/sys.html

CPython module: :mod:`python:sys` https://docs.python.org/3/library/sys.html .

---
Module: 'usys' on micropython-v1.23.0-preview-esp32-ESP32_GENERIC_S3
"""
# MCU: {'version': '1.23.0-preview', 'mpy': 'v6.2', 'port': 'esp32', 'board': 'ESP32_GENERIC_S3', 'family': 'micropython', 'build': 'preview.176.g90e517862', 'arch': 'xtensawin', 'ver': '1.23.0-preview-preview.176.g90e517862', 'cpu': 'ESP32S3'}
# Stubber: v1.17.3
from __future__ import annotations
from _typeshed import Incomplete
from typing import Dict, List, Tuple

platform: str = "esp32"
version_info: tuple = ()
path: list = []
version: str = "3.4.0; MicroPython v1.23.0-preview.176.g90e517862 on 2024-03-04"
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

    Difference to CPython

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
    function raise as `SystemExit` exception. If an argument is given, its
    value given as an argument to `SystemExit`.
    """
    ...

stderr: Incomplete  ## <class 'FileIO'> = <io.FileIO 2>
stdout: Incomplete  ## <class 'FileIO'> = <io.FileIO 1>
stdin: Incomplete  ## <class 'FileIO'> = <io.FileIO 0>
