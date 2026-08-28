"""
Module: 'usys' on micropython-v1.29.0-nrf-SEEED_XIAO_NRF52
"""

# MCU: {'variant': '', 'build': '', 'arch': 'armv7emsp', 'port': 'nrf', 'board': 'SEEED_XIAO_NRF52', 'board_id': 'SEEED_XIAO_NRF52', 'mpy': 'v6.3', 'ver': '1.29.0', 'family': 'micropython', 'cpu': 'NRF52840', 'version': '1.29.0'}
# Stubber: v1.28.6
from __future__ import annotations

from typing import Any, AsyncGenerator, Final, Generator

from _typeshed import Incomplete

platform: str = "nrf"
version_info: tuple = ()
path: list = []
version: str = "3.4.0; MicroPython v1.29.0 on 2026-08-24"
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
