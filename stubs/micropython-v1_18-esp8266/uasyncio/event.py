"""
Module: 'uasyncio.event' on micropython-v1.18-esp8266
"""
# MCU: {'ver': 'v1.18', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '1.18', 'name': 'micropython', 'mpy': 9733, 'version': '1.18', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
# Stubber: 1.5.4
from typing import Any


class Event:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def clear(self, *args, **kwargs) -> Any:
        ...

    def set(self, *args, **kwargs) -> Any:
        ...

    def is_set(self, *args, **kwargs) -> Any:
        ...

    wait: Any  ## <class 'generator'> = <generator>


class ThreadSafeFlag:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def set(self, *args, **kwargs) -> Any:
        ...

    def ioctl(self, *args, **kwargs) -> Any:
        ...

    wait: Any  ## <class 'generator'> = <generator>
