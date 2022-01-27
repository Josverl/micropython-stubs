"""
Module: 'uasyncio.event' on micropython-v1.18-pyboard
"""
# MCU: {'ver': 'v1.18', 'port': 'pyboard', 'arch': 'armv7emsp', 'sysname': 'pyboard', 'release': '1.18.0', 'name': 'micropython', 'mpy': 7685, 'version': '1.18.0', 'machine': 'PYBv1.1 with STM32F405RG', 'build': '', 'nodename': 'pyboard', 'platform': 'pyboard', 'family': 'micropython'}
# Stubber: 1.5.3
from typing import Any


class Event():
    ''
    def __init__(self, *argv, **kwargs) -> None:
        ''
        ...
    def clear(self, *args, **kwargs) -> Any:
        ...

    def set(self, *args, **kwargs) -> Any:
        ...

    def is_set(self, *args, **kwargs) -> Any:
        ...

    wait : Any ## <class 'generator'> = <generator>

class ThreadSafeFlag():
    ''
    def __init__(self, *argv, **kwargs) -> None:
        ''
        ...
    def set(self, *args, **kwargs) -> Any:
        ...

    def ioctl(self, *args, **kwargs) -> Any:
        ...

    wait : Any ## <class 'generator'> = <generator>
