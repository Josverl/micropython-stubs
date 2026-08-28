"""
Module: 'sys' on micropython-v1.29.0-unix-standard
"""
# MCU: {'family': 'micropython', 'version': '1.29.0', 'build': '', 'ver': '1.29.0', 'port': 'unix', 'board': 'standard', 'board_id': 'standard', 'variant': '', 'cpu': 'linux [GCC 12.5.0] version', 'mpy': 'v6.3', 'arch': 'x64'}
# Stubber: v1.28.6
from __future__ import annotations
from typing import Any, Final, Generator, AsyncGenerator
from _typeshed import Incomplete

path: list = []
platform: str = 'linux'
modules: dict = {}
maxsize: int = 9223372036854775807
version: str = '3.4.0; MicroPython v1.29.0 on 2026-08-28'
ps1: str = '>>> '
ps2: str = '... '
version_info: tuple = ()
byteorder: str = 'little'
implementation: tuple = ()
argv: list = []
executable: str = '/mnt/c/Users/jos_v/Downloads/firmware/unix/unix-standard-v1.29.0'
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
