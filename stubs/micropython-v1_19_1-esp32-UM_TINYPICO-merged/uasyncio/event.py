"""
Module: 'uasyncio.event' on micropython-v1.19.1-esp32
"""

# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module (spiram) with ESP32', 'release': '1.19.1', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.19.1'}
# Stubber: 1.5.6
from typing import Any


class Event:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def clear(self, *args, **kwargs) -> Any: ...

    def set(self, *args, **kwargs) -> Any: ...

    def is_set(self, *args, **kwargs) -> Any: ...

    wait: Any  ## <class 'generator'> = <generator>


class ThreadSafeFlag:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def set(self, *args, **kwargs) -> Any: ...

    def ioctl(self, *args, **kwargs) -> Any: ...

    wait: Any  ## <class 'generator'> = <generator>
