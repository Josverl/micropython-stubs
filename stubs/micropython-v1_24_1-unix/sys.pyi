"""
Module: 'sys' on micropython-v1.24.1-unix
"""
# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'unix', 'board': '', 'cpu': 'linux [GCC 12.4.0] version', 'mpy': 'v6.3', 'arch': 'x64'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

path: list = []
platform: str = 'linux'
modules: dict = {}
maxsize: int = 9223372036854775807
version: str = '3.4.0; MicroPython v1.24.1-dirty on 2025-02-23'
ps1: str = '>>> '
ps2: str = '... '
version_info: tuple = ()
byteorder: str = 'little'
implementation: tuple = ()
argv: list = []
executable: str = '/home/jos/micropython-stubber/firmware/unix/unix-v1.24.1'
def exc_info(*args, **kwargs) -> Incomplete:
    ...

def exit(*args, **kwargs) -> Incomplete:
    ...

def atexit(*args, **kwargs) -> Incomplete:
    ...

def print_exception(*args, **kwargs) -> Incomplete:
    ...

stderr: Incomplete ## <class 'TextIOWrapper'> = <io.TextIOWrapper 2>
stdin: Incomplete ## <class 'TextIOWrapper'> = <io.TextIOWrapper 0>
stdout: Incomplete ## <class 'TextIOWrapper'> = <io.TextIOWrapper 1>
