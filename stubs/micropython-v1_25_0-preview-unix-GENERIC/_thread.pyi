"""
Module: '_thread' on micropython-v1.25.0-preview-unix
"""
# MCU: {'family': 'micropython', 'version': '1.25.0-preview', 'build': '301', 'ver': '1.25.0-preview-301', 'port': 'unix', 'board': '', 'cpu': 'linux [GCC 12.4.0] version', 'mpy': 'v6.3', 'arch': 'x64'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

def get_ident(*args, **kwargs) -> Incomplete:
    ...

def start_new_thread(*args, **kwargs) -> Incomplete:
    ...

def stack_size(*args, **kwargs) -> Incomplete:
    ...

def exit(*args, **kwargs) -> Incomplete:
    ...

def allocate_lock(*args, **kwargs) -> Incomplete:
    ...


class LockType():
    def locked(self, *args, **kwargs) -> Incomplete:
        ...

    def release(self, *args, **kwargs) -> Incomplete:
        ...

    def acquire(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

