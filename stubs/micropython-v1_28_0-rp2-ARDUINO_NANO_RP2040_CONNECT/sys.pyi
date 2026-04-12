"""
Module: 'sys' on micropython-v1.28.0-rp2-ARDUINO_NANO_RP2040_CONNECT
"""

# MCU: {'mpy': 'v6.3', 'build': '', 'ver': '1.28.0', 'arch': 'armv6m', 'version': '1.28.0', 'port': 'rp2', 'board': 'ARDUINO_NANO_RP2040_CONNECT', 'family': 'micropython', 'board_id': 'ARDUINO_NANO_RP2040_CONNECT', 'variant': '', 'cpu': 'RP2040'}
# Stubber: v1.28.1
from __future__ import annotations
from _typeshed import Incomplete

platform: str = "rp2"
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
