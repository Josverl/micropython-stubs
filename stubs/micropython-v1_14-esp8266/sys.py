"""
Module: 'sys' on micropython-v1.14-esp8266
"""
# MCU: {'ver': 'v1.14', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '1.14', 'name': 'micropython', 'mpy': 9733, 'version': '1.14', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
# Stubber: 1.5.4
from typing import Any

argv = []  # type: list
byteorder = "little"  # type: str


def exit(*args, **kwargs) -> Any:
    ...


implementation = ()  # type: tuple
maxsize = 2147483647  # type: int
modules = {}  # type: dict
path = []  # type: list
platform = "esp8266"  # type: str


def print_exception(*args, **kwargs) -> Any:
    ...


stderr: Any  ## <class 'FileIO'> = <io.FileIO 2>
stdin: Any  ## <class 'FileIO'> = <io.FileIO 0>
stdout: Any  ## <class 'FileIO'> = <io.FileIO 1>
version = "3.4.0"  # type: str
version_info = ()  # type: tuple
