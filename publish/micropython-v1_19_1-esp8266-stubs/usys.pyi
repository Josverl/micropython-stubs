"""
System specific functions.

MicroPython module: https://docs.micropython.org/en/v1.19.1/library/sys.html

CPython module: :mod:`python:sys` https://docs.python.org/3/library/sys.html .
"""

from typing import Dict, List, Tuple, Any
from _typeshed import Incomplete

path: list
modules: dict
version_info: tuple
platform: str
version: str
byteorder: str
argv: list
maxsize: int
implementation: tuple

def exit(retval=0, /) -> Incomplete:
    """
    Terminate current program with a given exit code. Underlyingly, this
    function raise as `SystemExit` exception. If an argument is given, its
    value given as an argument to `SystemExit`.
    """
    ...

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

stderr: Any
stdout: Any
stdin: Any
