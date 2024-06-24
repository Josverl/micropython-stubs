"""
Module: 'sys' on micropython-v1.24.0-preview-samd-SEEED_WIO_TERMINAL
"""

# MCU: {'version': '1.24.0-preview', 'mpy': 'v6.3', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'family': 'micropython', 'build': '62', 'arch': 'armv7emsp', 'ver': '1.24.0-preview-62', 'cpu': 'SAMD51P19A'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete

platform: str = "samd"
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
