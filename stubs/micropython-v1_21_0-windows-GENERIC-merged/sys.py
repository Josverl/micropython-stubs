"""
System specific functions.

MicroPython module: https://docs.micropython.org/en/v1.21.0/library/sys.html

CPython module: :mod:`python:sys` https://docs.python.org/3/library/sys.html .
"""
# MCU: {'version': '1.21.0', 'mpy': '', 'port': 'win32', 'board': 'GENERIC', 'family': 'micropython', 'build': '', 'arch': '', 'ver': 'v1.21.0', 'cpu': ''}
# Stubber: v1.15.0
from typing import Dict, List, Tuple, Any
from _typeshed import Incomplete

modules = {}  # type: dict
version_info = ()  # type: tuple
maxsize = 2147483647  # type: int
version = "3.4.0; MicroPython v1.21.0 on 2023-12-04"  # type: str
path = []  # type: list
platform = "win32"  # type: str
byteorder = "little"  # type: str
argv = []  # type: list
implementation = ()  # type: tuple


def exc_info(*args, **kwargs) -> Incomplete:
    ...


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


def atexit(func) -> Incomplete:
    """
    Register *func* to be called upon termination.  *func* must be a callable
    that takes no arguments, or ``None`` to disable the call.  The ``atexit``
    function will return the previous value set by this function, which is
    initially ``None``.

    Difference to CPython

       This function is a MicroPython extension intended to provide similar
       functionality to the :mod:`atexit` module in CPython.
    """
    ...


stderr: Incomplete  ## <class 'TextIOWrapper'> = <io.TextIOWrapper 2>
stdin: Incomplete  ## <class 'TextIOWrapper'> = <io.TextIOWrapper 0>
stdout: Incomplete  ## <class 'TextIOWrapper'> = <io.TextIOWrapper 1>
