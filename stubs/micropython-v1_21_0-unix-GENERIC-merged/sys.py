"""
System specific functions.

MicroPython module: https://docs.micropython.org/en/v1.21.0/library/sys.html

CPython module: :mod:`python:sys` https://docs.python.org/3/library/sys.html .
"""
# MCU: {'family': 'micropython', 'version': '1.21.0', 'build': '', 'ver': 'v1.21.0', 'port': 'unix', 'board': 'linux_[GCC_9.4.0]_version', 'cpu': '', 'mpy': '', 'arch': ''}
# Stubber: v1.15.1
from typing import Dict, List, Tuple, Any
from _typeshed import Incomplete

path = []  # type: list
platform = "linux"  # type: str
modules = {}  # type: dict
maxsize = 9223372036854775807  # type: int
version = "3.4.0; MicroPython v1.21.0 on 2023-12-05"  # type: str
ps1 = ">>> "  # type: str
ps2 = "... "  # type: str
version_info = ()  # type: tuple
byteorder = "little"  # type: str
implementation = ()  # type: tuple
argv = []  # type: list
executable = "/workspaces/micropython/ports/unix/build-standard/micropython"  # type: str


def exc_info(*args, **kwargs) -> Incomplete:
    ...


def exit(retval=0, /) -> Incomplete:
    """
    Terminate current program with a given exit code. Underlyingly, this
    function raise as `SystemExit` exception. If an argument is given, its
    value given as an argument to `SystemExit`.
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


stderr: Incomplete  ## <class 'TextIOWrapper'> = <io.TextIOWrapper 2>
stdin: Incomplete  ## <class 'TextIOWrapper'> = <io.TextIOWrapper 0>
stdout: Incomplete  ## <class 'TextIOWrapper'> = <io.TextIOWrapper 1>
