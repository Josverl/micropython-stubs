"""
Module: 'usys' on micropython-v1.27.0-preview-webassembly-pyscript
"""
# MCU: {'family': 'micropython', 'version': '1.27.0-preview', 'build': '252', 'ver': '1.27.0-preview-252', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.26.2
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

platform: str = 'webassembly'
version_info: tuple = ()
path: list = []
version: str = '3.4.0; MicroPython v1.27.0-preview.252.gb2871e0d0a.dirty on 2025-10-02'
ps1: str = '>>> '
ps2: str = '... '
byteorder: str = 'little'
modules: dict = {}
argv: list = []
implementation: tuple = ()
maxsize: int = 2147483647
def print_exception(*args, **kwargs) -> Incomplete:
    ...

def exit(*args, **kwargs) -> Incomplete:
    ...

stderr: Incomplete ## <class 'TextIOWrapper'> = <io.TextIOWrapper 2>
stdout: Incomplete ## <class 'TextIOWrapper'> = <io.TextIOWrapper 1>
stdin: Incomplete ## <class 'TextIOWrapper'> = <io.TextIOWrapper 0>
