"""
Module: 'select' on micropython-v1.24.1-stm32-PYBV11
"""

# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'stm32', 'board': 'PYBV11', 'cpu': 'STM32F405RG', 'mpy': 'v6.3', 'arch': 'armv7emsp'}
# Stubber: v1.24.0
from __future__ import annotations
from _typeshed import Incomplete

POLLOUT: int = 4
POLLIN: int = 1
POLLHUP: int = 16
POLLERR: int = 8

def select(*args, **kwargs) -> Incomplete: ...
def poll(*args, **kwargs) -> Incomplete: ...
