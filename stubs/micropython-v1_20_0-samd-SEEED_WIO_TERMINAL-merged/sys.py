"""
system specific functions. See: https://docs.micropython.org/en/v1.20.0/library/sys.html

|see_cpython_module| :mod:`python:sys` https://docs.python.org/3/library/sys.html .
"""
# MCU: OrderedDict({'family': 'micropython', 'version': '1.20.0', 'build': '', 'ver': 'v1.20.0', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'cpu': 'SAMD51P19A', 'mpy': 'v6.1', 'arch': 'armv7emsp'})
# Stubber: v1.13.4
from typing import Dict, List, Tuple, Any

platform = "samd"  # type: str
version_info = ()  # type: tuple
path = []  # type: list
version = "3.4.0; MicroPython v1.20.0 on 2023-04-26"  # type: str
ps1 = ">>> "  # type: str
ps2 = "... "  # type: str
byteorder = "little"  # type: str
modules = {}  # type: dict
argv = []  # type: list
implementation = ()  # type: tuple
maxsize = 2147483647  # type: int


def print_exception(exc, file=stdout, /) -> None:
    """
    Print exception with a traceback to a file-like object *file* (or
    `sys.stdout` by default).
    """
    ...


def exit(retval=0, /) -> Any:
    """
    Terminate current program with a given exit code. Underlyingly, this
    function raise as `SystemExit` exception. If an argument is given, its
    value given as an argument to `SystemExit`.
    """
    ...


stderr: Any  ## <class 'FileIO'> = <io.FileIO 2>
stdout: Any  ## <class 'FileIO'> = <io.FileIO 1>
stdin: Any  ## <class 'FileIO'> = <io.FileIO 0>
