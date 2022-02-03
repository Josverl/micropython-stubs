"""
Module: '_thread' on micropython-v1.10-pyboard
"""
# MCU: {'ver': 'v1.10', 'build': '', 'platform': 'pyboard', 'port': 'pyboard', 'machine': 'PYBv1.1 with STM32F405RG', 'release': '1.10.0', 'nodename': 'pyboard', 'name': 'micropython', 'family': 'micropython', 'sysname': 'pyboard', 'version': '1.10.0'}
# Stubber: 1.5.4
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
