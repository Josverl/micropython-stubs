"""
Module: 'uasyncio.event' on micropython-v1.19.1-stm32
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'stm32', 'port': 'stm32', 'machine': 'PYBv1.1 with STM32F405RG', 'release': '1.19.1', 'nodename': 'pyboard', 'name': 'micropython', 'family': 'micropython', 'sysname': 'pyboard', 'version': '1.19.1'}
# Stubber: 1.9.11
from typing import Any


class ThreadSafeFlag:
    def ioctl(self, *args, **kwargs) -> Any:
        ...

    def set(self, *args, **kwargs) -> Any:
        ...

    wait: Any  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Event:
    def set(self, *args, **kwargs) -> Any:
        ...

    def is_set(self, *args, **kwargs) -> Any:
        ...

    def clear(self, *args, **kwargs) -> Any:
        ...

    wait: Any  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...
