"""
Module: 'sys' on micropython-v1.27.0-rp2-RPI_PICO
"""

# MCU: {'mpy': 'v6.3', 'build': '', 'ver': '1.27.0', 'arch': 'armv6m', 'version': '1.27.0', 'port': 'rp2', 'board': 'RPI_PICO', 'family': 'micropython', 'board_id': 'RPI_PICO', 'variant': '', 'cpu': 'RP2040'}
# Stubber: v1.26.4
from __future__ import annotations
from _typeshed import Incomplete

platform: str = "rp2"
version_info: tuple = ()
path: list = []
version: str = "3.4.0; MicroPython v1.27.0 on 2025-12-09"
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
