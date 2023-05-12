"""
Module: 'collections' on micropython-v1.20.0-stm32-PYBV11
"""
# MCU: OrderedDict({'version': '1.20.0', 'mpy': 'v6.1', 'port': 'stm32', 'board': 'PYBV11', 'family': 'micropython', 'build': '', 'arch': 'armv7emsp', 'ver': 'v1.20.0', 'cpu': 'STM32F405RG'})
# Stubber: v1.13.7
from typing import Any


def namedtuple(*args, **kwargs) -> Any:
    ...


class OrderedDict:
    def popitem(self, *args, **kwargs) -> Any:
        ...

    def pop(self, *args, **kwargs) -> Any:
        ...

    def values(self, *args, **kwargs) -> Any:
        ...

    def setdefault(self, *args, **kwargs) -> Any:
        ...

    def update(self, *args, **kwargs) -> Any:
        ...

    def copy(self, *args, **kwargs) -> Any:
        ...

    def clear(self, *args, **kwargs) -> Any:
        ...

    def keys(self, *args, **kwargs) -> Any:
        ...

    def get(self, *args, **kwargs) -> Any:
        ...

    def items(self, *args, **kwargs) -> Any:
        ...

    @classmethod
    def fromkeys(cls, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class deque:
    def popleft(self, *args, **kwargs) -> Any:
        ...

    def append(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
