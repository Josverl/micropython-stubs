"""
system specific functions. See: https://docs.micropython.org/en/v1.17/library/sys.html

|see_cpython_module| :mod:`python:sys` https://docs.python.org/3/library/sys.html .
"""
# MCU: {'ver': 'v1.17', 'port': 'pyboard', 'arch': 'armv7emsp', 'sysname': 'pyboard', 'release': '1.17.0', 'name': 'micropython', 'mpy': 7685, 'version': '1.17.0', 'machine': 'PYBv1.1 with STM32F405RG', 'build': '', 'nodename': 'pyboard', 'platform': 'pyboard', 'family': 'micropython'}
# Stubber: 1.5.4
from typing import Any

argv = []  # type: list
byteorder = "little"  # type: str


def exit(retval=0, /) -> Any:
    """
    Terminate current program with a given exit code. Underlyingly, this
    function raise as `SystemExit` exception. If an argument is given, its
    value given as an argument to `SystemExit`.
    """
    ...


implementation = ()  # type: tuple
maxsize = 2147483647  # type: int
modules = {}  # type: dict
path = []  # type: list
platform = "pyboard"  # type: str


def print_exception(exc, file=stdout, /) -> None:
    """
    Print exception with a traceback to a file-like object *file* (or
    `sys.stdout` by default).
    """
    ...


stderr: Any  ## <class 'FileIO'> = <io.FileIO 2>
stdin: Any  ## <class 'FileIO'> = <io.FileIO 0>
stdout: Any  ## <class 'FileIO'> = <io.FileIO 1>
version = "3.4.0"  # type: str
version_info = ()  # type: tuple
