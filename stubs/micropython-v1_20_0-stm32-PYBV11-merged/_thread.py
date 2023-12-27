"""
Multithreading support.

MicroPython module: https://docs.micropython.org/en/v1.20.0/library/_thread.html

CPython module: :mod:`python:_thread` https://docs.python.org/3/library/_thread.html .

This module implements multithreading support.

This module is highly experimental and its API is not yet fully settled
and not yet described in this documentation.

---
Module: '_thread' on micropython-v1.20.0-stm32-PYBV11
"""
# MCU: OrderedDict({'version': '1.20.0', 'mpy': 'v6.1', 'port': 'stm32', 'board': 'PYBV11', 'family': 'micropython', 'build': '', 'arch': 'armv7emsp', 'ver': 'v1.20.0', 'cpu': 'STM32F405RG'})
# Stubber: v1.13.7
from typing import Any
from _typeshed import Incomplete


def get_ident(*args, **kwargs) -> Any:
    ...


def start_new_thread(*args, **kwargs) -> Any:
    ...


def stack_size(*args, **kwargs) -> Any:
    ...


def exit(*args, **kwargs) -> Any:
    ...


def allocate_lock(*args, **kwargs) -> Any:
    ...


class LockType:
    def locked(self, *args, **kwargs) -> Any:
        ...

    def release(self, *args, **kwargs) -> Any:
        ...

    def acquire(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
