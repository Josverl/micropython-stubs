"""
Module: '_thread' on micropython-v1.12-pyboard
"""
# MCU: {'ver': 'v1.12', 'port': 'pyboard', 'arch': 'armv7emsp', 'sysname': 'pyboard', 'release': '1.12.0', 'name': 'micropython', 'mpy': 7685, 'version': '1.12.0', 'machine': 'PYBv1.1 with STM32F405RG', 'build': '', 'nodename': 'pyboard', 'platform': 'pyboard', 'family': 'micropython'}
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
