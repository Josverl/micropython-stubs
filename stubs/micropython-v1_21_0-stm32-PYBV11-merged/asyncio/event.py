"""
Module: 'asyncio.event' on micropython-v1.21.0-stm32-PYBV11
"""

# MCU: {'version': '1.21.0', 'mpy': 'v6.1', 'port': 'stm32', 'board': 'PYBV11', 'family': 'micropython', 'build': '', 'arch': 'armv7emsp', 'ver': 'v1.21.0', 'cpu': 'STM32F405RG'}
# Stubber: v1.13.8
from typing import Any
from _typeshed import Incomplete


class ThreadSafeFlag:
    def set(self, *args, **kwargs) -> Incomplete: ...

    def ioctl(self, *args, **kwargs) -> Incomplete: ...

    def clear(self, *args, **kwargs) -> Incomplete: ...

    wait: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...


class Event:
    def set(self, *args, **kwargs) -> Incomplete: ...

    def is_set(self, *args, **kwargs) -> Incomplete: ...

    def clear(self, *args, **kwargs) -> Incomplete: ...

    wait: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...
