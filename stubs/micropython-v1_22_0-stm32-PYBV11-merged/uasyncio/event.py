"""
Module: 'uasyncio.event' on micropython-v1.22.0-stm32-PYBV11
"""

# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'stm32', 'board': 'PYBV11', 'cpu': 'STM32F405RG', 'mpy': 'v6.2', 'arch': 'armv7emsp'}
# Stubber: v1.16.2
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
