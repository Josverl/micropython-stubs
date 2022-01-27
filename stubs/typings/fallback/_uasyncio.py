"""
Module: '_uasyncio' on micropython-v1.18-esp32
"""
# MCU: {'ver': 'v1.18', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.18.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.18.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.5.3
from typing import Any


class Task:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


class TaskQueue:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def remove(self, *args, **kwargs) -> Any:
        ...

    def peek(self, *args, **kwargs) -> Any:
        ...

    def pop_head(self, *args, **kwargs) -> Any:
        ...

    def push_head(self, *args, **kwargs) -> Any:
        ...

    def push_sorted(self, *args, **kwargs) -> Any:
        ...
