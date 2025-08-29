"""
Multithreading support.

MicroPython module: https://docs.micropython.org/en/v1.26.0/library/_thread.html

CPython module: :mod:`python:_thread` https://docs.python.org/3/library/_thread.html .

This module implements multithreading support.

This module is highly experimental and its API is not yet fully settled
and not yet described in this documentation.

---
Module: '_thread' on micropython-v1.26.0-rp2-RPI_PICO2
"""

# MCU: {'mpy': 'v6.3', 'build': '', 'ver': '1.26.0', 'arch': 'armv7emsp', 'version': '1.26.0', 'port': 'rp2', 'board': 'RPI_PICO2', 'family': 'micropython', 'board_id': 'RPI_PICO2', 'variant': '', 'cpu': 'RP2350'}
# Stubber: v1.26.0
from __future__ import annotations
from _typeshed import Incomplete
from typing_extensions import Awaitable, TypeAlias, TypeVar

def get_ident(*args, **kwargs) -> Incomplete: ...
def start_new_thread(*args, **kwargs) -> Incomplete: ...
def stack_size(*args, **kwargs) -> Incomplete: ...
def exit(*args, **kwargs) -> Incomplete: ...
def allocate_lock(*args, **kwargs) -> Incomplete: ...

class LockType:
    def locked(self, *args, **kwargs) -> Incomplete: ...
    def release(self, *args, **kwargs) -> Incomplete: ...
    def acquire(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
