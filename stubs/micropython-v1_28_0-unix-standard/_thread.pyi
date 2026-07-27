"""
Module: '_thread' on micropython-v1.28.0-unix-standard
"""
# MCU: {'family': 'micropython', 'version': '1.28.0', 'build': '', 'ver': '1.28.0', 'port': 'unix', 'board': 'standard', 'board_id': 'standard', 'variant': '', 'cpu': 'linux [GCC 12.5.0] version', 'mpy': 'v6.3', 'arch': 'x64'}
# Stubber: v1.28.3
from __future__ import annotations
from typing import Any, Final, Generator, AsyncGenerator
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

