"""
Module: 'uasyncio.event' on micropython-v1.18-rp2
"""
# MCU: {'family': 'micropython', 'sysname': 'rp2', 'version': '1.18.0', 'build': '', 'mpy': 5637, 'port': 'rp2', 'platform': 'rp2', 'name': 'micropython', 'arch': 'armv7m', 'machine': 'Arduino Nano RP2040 Connect with RP2040', 'nodename': 'rp2', 'ver': 'v1.18', 'release': '1.18.0'}
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

    wait : Any ## <class 'generator'> = <generator>
    def is_set(self, *args, **kwargs) -> Any:
        ...


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
