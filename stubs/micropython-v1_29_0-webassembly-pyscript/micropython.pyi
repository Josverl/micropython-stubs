"""
Module: 'micropython' on micropython-v1.29.0-webassembly-pyscript
"""
# MCU: {'family': 'micropython', 'version': '1.29.0', 'build': '', 'ver': '1.29.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.28.6
from __future__ import annotations
from typing import Any, Final, Generator, AsyncGenerator
from _typeshed import Incomplete

def pystack_use() -> Incomplete:
    ...

def opt_level(*args, **kwargs) -> Incomplete:
    ...

def mem_info(*args, **kwargs) -> Incomplete:
    ...

def qstr_info(*args, **kwargs) -> Incomplete:
    ...

def schedule(x0, x1) -> Incomplete:
    ...

def stack_use() -> Incomplete:
    ...

def kbd_intr(x0) -> Incomplete:
    ...

def const(x0) -> Incomplete:
    ...

def heap_unlock() -> Incomplete:
    ...

def heap_lock() -> Incomplete:
    ...


class RingIO():
    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def readline(self, *args, **kwargs) -> Incomplete:
        ...

    def any(self, *args, **kwargs) -> Incomplete:
        ...

    def read(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

