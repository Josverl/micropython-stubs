"""
Module: 'uasyncio.event' on micropython-v1.17-rp2
"""
# MCU: {'family': 'micropython', 'sysname': 'rp2', 'version': '1.17.0', 'build': '', 'mpy': 5637, 'port': 'rp2', 'platform': 'rp2', 'name': 'micropython', 'arch': 'armv7m', 'machine': 'Raspberry Pi Pico with RP2040', 'nodename': 'rp2', 'ver': 'v1.17', 'release': '1.17.0'}
# Stubber: 1.5.2
from typing import Any


class Event:
    """"""

    def __init__(self, *args) -> None:
        ...

    def clear(self, *args) -> Any:
        ...

    def set(self, *args) -> Any:
        ...

    wait: Any  ## <class 'generator'> = <generator>

    def is_set(self, *args) -> Any:
        ...


class ThreadSafeFlag:
    """"""

    def __init__(self, *args) -> None:
        ...

    def set(self, *args) -> Any:
        ...

    def ioctl(self, *args) -> Any:
        ...

    wait: Any  ## <class 'generator'> = <generator>
