"""
Module: 'usys' on micropython-v1.22.2-samd-SEEED_WIO_TERMINAL
"""

# MCU: {'build': '', 'ver': '1.22.2', 'version': '1.22.2', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'mpy': 'v6.2', 'family': 'micropython', 'cpu': 'SAMD51P19A', 'arch': 'armv7emsp'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete

platform: str = "samd"
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
