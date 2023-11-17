"""
Multithreading support.

MicroPython module: https://docs.micropython.org/en/latest/library/_thread.html

CPython module: :mod:`python:_thread` https://docs.python.org/3/library/_thread.html .

This module implements multithreading support.

This module is highly experimental and its API is not yet fully settled
and not yet described in this documentation.
"""
# MCU: {'build': '', 'ver': 'v1.21.0', 'version': '1.21.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.13.8
from typing import Any
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


class LockType:
    def locked(self, *args, **kwargs) -> Incomplete:
        ...

    def release(self, *args, **kwargs) -> Incomplete:
        ...

    def acquire(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
