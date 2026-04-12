"""
Module: 'asyncio.lock' on micropython-v1.28.0-stm32-PYBV11
"""

# MCU: {'variant': '', 'build': '', 'arch': 'armv7emsp', 'port': 'stm32', 'board': 'PYBV11', 'board_id': 'PYBV11', 'mpy': 'v6.3', 'ver': '1.28.0', 'family': 'micropython', 'cpu': 'STM32F405RG', 'version': '1.28.0'}
# Stubber: v1.28.0
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

class Lock:
    def locked(self, *args, **kwargs) -> Incomplete: ...
    def release(self, *args, **kwargs) -> Incomplete: ...
    def acquire(self, *args, **kwargs) -> Generator:  ## = <generator>
        ...
    def __init__(self, *argv, **kwargs) -> None: ...
