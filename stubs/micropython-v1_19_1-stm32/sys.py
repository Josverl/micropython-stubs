"""
Module: 'sys' on micropython-v1.19.1-stm32
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'stm32', 'port': 'stm32', 'machine': 'PYBv1.1 with STM32F405RG', 'release': '1.19.1', 'nodename': 'pyboard', 'name': 'micropython', 'family': 'micropython', 'sysname': 'pyboard', 'version': '1.19.1'}
# Stubber: 1.9.11
from typing import Any

platform = "pyboard"  # type: str
version_info = ()  # type: tuple
path = []  # type: list
version = "3.4.0; MicroPython v1.19.1 on 2022-06-18"  # type: str
ps1 = ">>> "  # type: str
ps2 = "... "  # type: str
byteorder = "little"  # type: str
modules = {}  # type: dict
argv = []  # type: list
implementation = ()  # type: tuple
maxsize = 2147483647  # type: int


def print_exception(*args, **kwargs) -> Any:
    ...


def exit(*args, **kwargs) -> Any:
    ...


stderr: Any  ## <class 'FileIO'> = <io.FileIO 2>
stdout: Any  ## <class 'FileIO'> = <io.FileIO 1>
stdin: Any  ## <class 'FileIO'> = <io.FileIO 0>
