"""
Module: 'select' on micropython-v1.18-pyboard
"""
# MCU: {'ver': 'v1.18', 'port': 'pyboard', 'arch': 'armv7emsp', 'sysname': 'pyboard', 'release': '1.18.0', 'name': 'micropython', 'mpy': 7685, 'version': '1.18.0', 'machine': 'PYBv1.1 with STM32F405RG', 'build': '', 'nodename': 'pyboard', 'platform': 'pyboard', 'family': 'micropython'}
# Stubber: 1.5.2
from typing import Any

POLLERR = 8  # type: int
POLLHUP = 16  # type: int
POLLIN = 1  # type: int
POLLOUT = 4  # type: int


def poll(*args) -> Any:
    ...


def select(*args) -> Any:
    ...
