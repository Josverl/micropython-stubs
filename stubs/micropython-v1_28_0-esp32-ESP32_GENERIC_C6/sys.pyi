"""
Module: 'sys' on micropython-v1.28.0-esp32-ESP32_GENERIC_C6
"""

# MCU: {'variant': '', 'build': '', 'arch': 'rv32imc', 'port': 'esp32', 'board': 'ESP32_GENERIC_C6', 'board_id': 'ESP32_GENERIC_C6', 'mpy': 'v6.3', 'ver': '1.28.0', 'family': 'micropython', 'cpu': 'ESP32C6', 'version': '1.28.0'}
# Stubber: v1.28.1
from __future__ import annotations
from _typeshed import Incomplete

platform: str = "esp32"
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
