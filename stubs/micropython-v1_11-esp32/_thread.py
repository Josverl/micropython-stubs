"""
Module: '_thread' on micropython-v1.11-esp32
"""
# MCU: {'ver': 'v1.11', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module with ESP32', 'release': '1.11.0', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.11.0'}
# Stubber: 1.5.3
from typing import Any


class LockType:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def acquire(self, *args, **kwargs) -> Any:
        ...

    def locked(self, *args, **kwargs) -> Any:
        ...

    def release(self, *args, **kwargs) -> Any:
        ...


def allocate_lock(*args, **kwargs) -> Any:
    ...


def exit(*args, **kwargs) -> Any:
    ...


def get_ident(*args, **kwargs) -> Any:
    ...


def stack_size(*args, **kwargs) -> Any:
    ...


def start_new_thread(*args, **kwargs) -> Any:
    ...
