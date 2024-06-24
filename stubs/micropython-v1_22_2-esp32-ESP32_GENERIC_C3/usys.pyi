"""
Module: 'usys' on micropython-v1.22.2-esp32-ESP32_GENERIC_C3
"""

# MCU: {'version': '1.22.2', 'mpy': 'v6.2', 'port': 'esp32', 'board': 'ESP32_GENERIC_C3', 'family': 'micropython', 'build': '', 'arch': '', 'ver': '1.22.2', 'cpu': 'ESP32C3'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete

platform: str = "esp32"
version_info: tuple = ()
path: list = []
version: str = "3.4.0; MicroPython v1.22.2 on 2024-02-22"
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
