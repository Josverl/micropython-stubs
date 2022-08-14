"""
Module: 'sys' on micropython-v1.19.1-esp32
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module (spiram) with ESP32', 'release': '1.19.1', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.19.1'}
# Stubber: 1.5.6
from typing import Any

argv = []  # type: list
byteorder = "little"  # type: str


def exit(*args, **kwargs) -> Any:
    ...


implementation = ()  # type: tuple
maxsize = 2147483647  # type: int
modules = {}  # type: dict
path = []  # type: list
platform = "esp32"  # type: str


def print_exception(*args, **kwargs) -> Any:
    ...


ps1 = ">>> "  # type: str
ps2 = "... "  # type: str
stderr: Any  ## <class 'FileIO'> = <io.FileIO 2>
stdin: Any  ## <class 'FileIO'> = <io.FileIO 0>
stdout: Any  ## <class 'FileIO'> = <io.FileIO 1>
version = "3.4.0; MicroPython v1.19.1 on 2022-06-18"  # type: str
version_info = ()  # type: tuple
