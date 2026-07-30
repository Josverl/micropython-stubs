"""
Module: 'sys' on micropython-v1.29.0-preview-esp32-ESP32_GENERIC_C6
"""

# MCU: {'variant': '', 'build': 'preview.657.gf013bb5195', 'arch': 'rv32imc', 'port': 'esp32', 'board': 'ESP32_GENERIC_C6', 'board_id': 'ESP32_GENERIC_C6', 'mpy': 'v6.3', 'ver': '1.29.0-preview-preview.657.gf013bb5195', 'family': 'micropython', 'cpu': 'ESP32-C6', 'version': '1.29.0-preview'}
# Stubber: v1.28.3
from __future__ import annotations

from _typeshed import Incomplete

platform: str = "esp32"
version_info: tuple = ()
path: list = []
version: str = "3.4.0; MicroPython v1.29.0-preview.657.gf013bb5195 on 2026-07-30"
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
