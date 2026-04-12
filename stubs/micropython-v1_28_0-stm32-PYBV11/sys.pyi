"""
Module: 'sys' on micropython-v1.28.0-stm32-PYBV11
"""

# MCU: {'variant': '', 'build': '', 'arch': 'armv7emsp', 'port': 'stm32', 'board': 'PYBV11', 'board_id': 'PYBV11', 'mpy': 'v6.3', 'ver': '1.28.0', 'family': 'micropython', 'cpu': 'STM32F405RG', 'version': '1.28.0'}
# Stubber: v1.28.0
from __future__ import annotations
from _typeshed import Incomplete

platform: str = "pyboard"
version_info: tuple = ()
path: list = []
version: str = "3.4.0; MicroPython v1.28.0 on 2026-04-06"
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
