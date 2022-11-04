"""
system specific functions. See: https://docs.micropython.org/en/v1.18/library/sys.html

|see_cpython_module| :mod:`python:sys` https://docs.python.org/3/library/sys.html .
"""
# MCU: {'ver': 'v1.18', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.18.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.18.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
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
platform = "esp32"  # type: str


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
