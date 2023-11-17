"""
System specific functions.

MicroPython module: https://docs.micropython.org/en/v1.21.0/library/sys.html

CPython module: :mod:`python:sys` https://docs.python.org/3/library/sys.html .
"""
from _typeshed import Incomplete, Incomplete as Incomplete
from typing import Dict, List, Tuple

platform: str
version_info: tuple
path: list
version: str
ps1: str
ps2: str
byteorder: str
modules: dict
argv: list
implementation: tuple
maxsize: int

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

stderr: Incomplete
stdout: Incomplete
stdin: Incomplete
