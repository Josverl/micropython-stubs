"""
Module: '_thread' on micropython-v1.17-esp32
"""
# MCU: {'ver': 'v1.17', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.17.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.17.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.5.0
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
