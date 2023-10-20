"""
Module: 'usys' on micropython-v1.21.0-stm32-PYBV11
"""
# MCU: {'version': '1.21.0', 'mpy': 'v6.1', 'port': 'stm32', 'board': 'PYBV11', 'family': 'micropython', 'build': '', 'arch': 'armv7emsp', 'ver': 'v1.21.0', 'cpu': 'STM32F405RG'}
# Stubber: v1.13.8
from typing import Any
from _typeshed import Incomplete

platform = "pyboard"  # type: str
version_info = ()  # type: tuple
path = []  # type: list
version = "3.4.0; MicroPython v1.21.0 on 2023-10-06"  # type: str
ps1 = ">>> "  # type: str
ps2 = "... "  # type: str
byteorder = "little"  # type: str
modules = {}  # type: dict
argv = []  # type: list
implementation = ()  # type: tuple
maxsize = 2147483647  # type: int


def print_exception(*args, **kwargs) -> Incomplete:
    ...


def exit(*args, **kwargs) -> Incomplete:
    ...


stderr: Incomplete  ## <class 'FileIO'> = <io.FileIO 2>
stdout: Incomplete  ## <class 'FileIO'> = <io.FileIO 1>
stdin: Incomplete  ## <class 'FileIO'> = <io.FileIO 0>
