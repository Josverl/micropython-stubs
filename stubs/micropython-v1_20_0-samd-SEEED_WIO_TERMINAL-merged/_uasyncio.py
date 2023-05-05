"""
Module: '_uasyncio' on micropython-v1.20.0-samd-SEEED_WIO_TERMINAL
"""
# MCU: OrderedDict({'family': 'micropython', 'version': '1.20.0', 'build': '', 'ver': 'v1.20.0', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'cpu': 'SAMD51P19A', 'mpy': 'v6.1', 'arch': 'armv7emsp'})
# Stubber: v1.13.4
from typing import Any


class TaskQueue:
    def push(self, *args, **kwargs) -> Any:
        ...

    def peek(self, *args, **kwargs) -> Any:
        ...

    def remove(self, *args, **kwargs) -> Any:
        ...

    def pop(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Task:
    def __init__(self, *argv, **kwargs) -> None:
        ...
