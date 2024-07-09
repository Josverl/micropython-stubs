"""
Module: 'uasyncio.lock' on micropython-v1.23.0-stm32-PYBV11
"""

# MCU: {'version': '1.23.0', 'mpy': 'v6.3', 'port': 'stm32', 'board': 'PYBV11', 'family': 'micropython', 'build': '', 'arch': 'armv7emsp', 'ver': '1.23.0', 'cpu': 'STM32F405RG'}
# Stubber: v1.23.0
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

class Lock:
    def locked(self, *args, **kwargs) -> Incomplete: ...
    def release(self, *args, **kwargs) -> Incomplete: ...

    acquire: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...
