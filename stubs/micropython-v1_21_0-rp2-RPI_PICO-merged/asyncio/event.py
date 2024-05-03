"""
Module: 'asyncio.event' on micropython-v1.21.0-rp2-RPI_PICO
"""

# MCU: {'build': '', 'ver': 'v1.21.0', 'version': '1.21.0', 'port': 'rp2', 'board': 'RPI_PICO', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
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
