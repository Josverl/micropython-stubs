"""
Module: 'sys' on micropython-v1.24.1-webassembly
"""
# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'webassembly', 'board': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

platform: str = 'webassembly'
version_info: tuple = ()
path: list = []
version: str = '3.4.0; MicroPython v1.24.1 on 2024-11-30'
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
