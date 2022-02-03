"""
Module: 'sys' on micropython-v1.10-pyboard
"""
# MCU: {'ver': 'v1.10', 'build': '', 'platform': 'pyboard', 'port': 'pyboard', 'machine': 'PYBv1.1 with STM32F405RG', 'release': '1.10.0', 'nodename': 'pyboard', 'name': 'micropython', 'family': 'micropython', 'sysname': 'pyboard', 'version': '1.10.0'}
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
platform = "pyboard"  # type: str


def print_exception(*args, **kwargs) -> Any:
    ...


stderr: Any  ## <class 'FileIO'> = <io.FileIO 2>
stdin: Any  ## <class 'FileIO'> = <io.FileIO 0>
stdout: Any  ## <class 'FileIO'> = <io.FileIO 1>
version = "3.4.0"  # type: str
version_info = ()  # type: tuple
