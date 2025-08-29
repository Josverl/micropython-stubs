"""
Module: 'sys' on micropython-v1.26.0-stm32-PYBV11-NETWORK
"""

# MCU: {'variant': 'NETWORK', 'build': '', 'arch': 'armv7emsp', 'port': 'stm32', 'board': 'PYBV11', 'board_id': 'PYBV11-NETWORK', 'mpy': 'v6.3', 'ver': '1.26.0', 'family': 'micropython', 'cpu': 'STM32F405RG', 'version': '1.26.0'}
# Stubber: v1.26.0
from __future__ import annotations
from _typeshed import Incomplete

platform: str = "pyboard"
version_info: tuple = ()
path: list = []
version: str = "3.4.0; MicroPython v1.26.0 on 2025-08-09"
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
