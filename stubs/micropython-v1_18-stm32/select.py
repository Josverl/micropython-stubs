"""
Module: 'select' on micropython-v1.18-stm32
"""
# MCU: {'ver': 'v1.18', 'port': 'stm32', 'arch': 'armv7emsp', 'sysname': 'pyboard', 'release': '1.18.0', 'name': 'micropython', 'mpy': 7685, 'version': '1.18.0', 'machine': 'PYBv1.1 with STM32F405RG', 'build': '', 'nodename': 'pyboard', 'platform': 'stm32', 'family': 'micropython'}
# Stubber: 1.5.6
from typing import Any

POLLERR = 8  # type: int
POLLHUP = 16  # type: int
POLLIN = 1  # type: int
POLLOUT = 4  # type: int


def poll(*args, **kwargs) -> Any:
    ...


def select(*args, **kwargs) -> Any:
    ...
