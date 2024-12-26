"""
Module: 'sys' on micropython-v1.24.1-stm32-PYBV11
"""

# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'stm32', 'board': 'PYBV11', 'cpu': 'STM32F405RG', 'mpy': 'v6.3', 'arch': 'armv7emsp'}
# Stubber: v1.24.0
from __future__ import annotations
from _typeshed import Incomplete

platform: str = "pyboard"
version_info: tuple = ()
path: list = []
version: str = "3.4.0; MicroPython v1.24.1 on 2024-11-29"
ps1: str = ">>> "
ps2: str = "... "
byteorder: str = "little"
modules: dict = {}
argv: list = []
implementation: tuple = ()
maxsize: int = 2147483647

def print_exception(*args, **kwargs) -> Incomplete: ...
def exit(*args, **kwargs) -> Incomplete: ...

stderr: Incomplete  ## <class 'TextIOWrapper'> = <io.TextIOWrapper 2>
stdout: Incomplete  ## <class 'TextIOWrapper'> = <io.TextIOWrapper 1>
stdin: Incomplete  ## <class 'TextIOWrapper'> = <io.TextIOWrapper 0>
