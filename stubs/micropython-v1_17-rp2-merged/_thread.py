"""
multithreading support. See: https://docs.micropython.org/en/v1.17/library/_thread.html

|see_cpython_module| :mod:`python:_thread` https://docs.python.org/3/library/_thread.html .

This module implements multithreading support.

This module is highly experimental and its API is not yet fully settled
and not yet described in this documentation.
"""
# MCU: {'family': 'micropython', 'sysname': 'rp2', 'version': '1.17.0', 'build': '', 'mpy': 5637, 'port': 'rp2', 'platform': 'rp2', 'name': 'micropython', 'arch': 'armv7m', 'machine': 'Raspberry Pi Pico with RP2040', 'nodename': 'rp2', 'ver': 'v1.17', 'release': '1.17.0'}
# Stubber: 1.5.2
from typing import Any


class LockType:
    """"""

    def acquire(self, *args) -> Any:
        ...

    def locked(self, *args) -> Any:
        ...

    def release(self, *args) -> Any:
        ...


def allocate_lock(*args) -> Any:
    ...


def exit(*args) -> Any:
    ...


def get_ident(*args) -> Any:
    ...


def stack_size(*args) -> Any:
    ...


def start_new_thread(*args) -> Any:
    ...
