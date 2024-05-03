"""
Module: '_uasyncio' on micropython-v1.20.0-stm32-PYBV11
"""

# MCU: OrderedDict({'version': '1.20.0', 'mpy': 'v6.1', 'port': 'stm32', 'board': 'PYBV11', 'family': 'micropython', 'build': '', 'arch': 'armv7emsp', 'ver': 'v1.20.0', 'cpu': 'STM32F405RG'})
# Stubber: v1.13.7
from typing import Any


class TaskQueue:
    def push(self, *args, **kwargs) -> Any: ...

    def peek(self, *args, **kwargs) -> Any: ...

    def remove(self, *args, **kwargs) -> Any: ...

    def pop(self, *args, **kwargs) -> Any: ...

    def __init__(self, *argv, **kwargs) -> None: ...


class Task:
    def __init__(self, *argv, **kwargs) -> None: ...
