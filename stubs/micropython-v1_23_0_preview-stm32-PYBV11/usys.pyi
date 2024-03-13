"""
Module: 'usys' on micropython-v1.23.0-preview-stm32-PYBV11
"""
# MCU: {'version': '1.23.0-preview', 'mpy': 'v6.2', 'port': 'stm32', 'board': 'PYBV11', 'family': 'micropython', 'build': 'preview.203.gd712feb68', 'arch': 'armv7emsp', 'ver': '1.23.0-preview-preview.203.gd712feb68', 'cpu': 'STM32F405RG'}
# Stubber: v1.17.3
from __future__ import annotations
from _typeshed import Incomplete

platform: str = "pyboard"
version_info: tuple = ()
path: list = []
version: str = "3.4.0; MicroPython v1.23.0-preview.203.gd712feb68 on 2024-03-09"
ps1: str = ">>> "
ps2: str = "... "
byteorder: str = "little"
modules: dict = {}
argv: list = []
implementation: tuple = ()
maxsize: int = 2147483647

def print_exception(*args, **kwargs) -> Incomplete: ...
def exit(*args, **kwargs) -> Incomplete: ...

stderr: Incomplete  ## <class 'FileIO'> = <io.FileIO 2>
stdout: Incomplete  ## <class 'FileIO'> = <io.FileIO 1>
stdin: Incomplete  ## <class 'FileIO'> = <io.FileIO 0>
