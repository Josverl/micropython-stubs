"""
system specific functions. See: https://docs.micropython.org/en/v1.19.1/library/sys.html

|see_cpython_module| :mod:`python:sys` https://docs.python.org/3/library/sys.html .
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp8266', 'port': 'esp8266', 'machine': 'ESP module (1M) with ESP8266', 'release': '1.19.1', 'nodename': 'esp8266', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp8266', 'version': '1.19.1'}
# Stubber: 1.9.11
from typing import Dict, List, Tuple, Any

path = []  # type: list
modules = {}  # type: dict
version_info = ()  # type: tuple
platform = "esp8266"  # type: str
version = "3.4.0; MicroPython v1.19.1 on 2022-06-18"  # type: str
byteorder = "little"  # type: str
argv = []  # type: list
maxsize = 2147483647  # type: int
implementation = ()  # type: tuple


def exit(retval=0, /) -> Any:
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
    """
    ...


stderr: Any  ## <class 'FileIO'> = <io.FileIO 2>
stdout: Any  ## <class 'FileIO'> = <io.FileIO 1>
stdin: Any  ## <class 'FileIO'> = <io.FileIO 0>
