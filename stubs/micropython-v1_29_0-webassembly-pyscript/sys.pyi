"""
Module: 'sys' on micropython-v1.29.0-webassembly-pyscript
"""
# MCU: {'family': 'micropython', 'version': '1.29.0', 'build': '', 'ver': '1.29.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.28.6
from __future__ import annotations
from typing import Any, Final, Generator, AsyncGenerator
from _typeshed import Incomplete

platform: str = 'webassembly'
version_info: tuple = ()
path: list = []
version: str = '3.4.0; MicroPython v1.29.0 on 2026-08-28'
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
