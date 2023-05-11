"""
Module: 'uselect' on micropython-v1.20.0-stm32-PYBV11
"""
# MCU: OrderedDict({'version': '1.20.0', 'mpy': 'v6.1', 'port': 'stm32', 'board': 'PYBV11', 'family': 'micropython', 'build': '', 'arch': 'armv7emsp', 'ver': 'v1.20.0', 'cpu': 'STM32F405RG'})
# Stubber: v1.13.7
from typing import Any

POLLOUT = 4  # type: int
POLLIN = 1  # type: int
POLLHUP = 16  # type: int
POLLERR = 8  # type: int


def select(*args, **kwargs) -> Any:
    ...


def poll(*args, **kwargs) -> Any:
    ...
