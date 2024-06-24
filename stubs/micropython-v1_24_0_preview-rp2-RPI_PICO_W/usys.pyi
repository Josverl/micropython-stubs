"""
Module: 'usys' on micropython-v1.24.0-preview-rp2-RPI_PICO_W
"""

# MCU: {'build': 'preview.62.g908ab1cec', 'ver': '1.24.0-preview-preview.62.g908ab1cec', 'version': '1.24.0-preview', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.3', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete

platform: str = "rp2"
version_info: tuple = ()
path: list = []
version: str = "3.4.0; MicroPython v1.24.0-preview.62.g908ab1cec on 2024-06-24"
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
