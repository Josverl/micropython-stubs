"""
Module: '_uasyncio' on micropython-v1.18-pyboard
"""
# MCU: {'ver': 'v1.18', 'port': 'pyboard', 'arch': 'armv7emsp', 'sysname': 'pyboard', 'release': '1.18.0', 'name': 'micropython', 'mpy': 7685, 'version': '1.18.0', 'machine': 'PYBv1.1 with STM32F405RG', 'build': '', 'nodename': 'pyboard', 'platform': 'pyboard', 'family': 'micropython'}
# Stubber: 1.5.2
from typing import Any


class Task:
    """"""

    def __init__(self, *argv) -> None:
        """"""
        ...


class TaskQueue:
    """"""

    def __init__(self, *argv) -> None:
        """"""
        ...

    def remove(self, *args) -> Any:
        ...

    def peek(self, *args) -> Any:
        ...

    def pop_head(self, *args) -> Any:
        ...

    def push_head(self, *args) -> Any:
        ...

    def push_sorted(self, *args) -> Any:
        ...
