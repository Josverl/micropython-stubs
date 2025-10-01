"""
Module: 'micropython' on micropython-v1.26.1-unix-standard
"""
# MCU: {'family': 'micropython', 'version': '1.26.1', 'build': '', 'ver': '1.26.1', 'port': 'unix', 'board': 'standard', 'board_id': 'standard', 'variant': '', 'cpu': 'linux [GCC 12.4.0] version', 'mpy': 'v6.3', 'arch': 'x64'}
# Stubber: v1.26.2
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

def mem_total(*args, **kwargs) -> Incomplete:
    ...

def mem_info(*args, **kwargs) -> Incomplete:
    ...

def mem_peak(*args, **kwargs) -> Incomplete:
    ...

def schedule(*args, **kwargs) -> Incomplete:
    ...

def opt_level(*args, **kwargs) -> Incomplete:
    ...

def qstr_info(*args, **kwargs) -> Incomplete:
    ...

def stack_use(*args, **kwargs) -> Incomplete:
    ...

def heap_lock(*args, **kwargs) -> Incomplete:
    ...

def const(*args, **kwargs) -> Incomplete:
    ...

def mem_current(*args, **kwargs) -> Incomplete:
    ...

def kbd_intr(*args, **kwargs) -> Incomplete:
    ...

def heap_unlock(*args, **kwargs) -> Incomplete:
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

