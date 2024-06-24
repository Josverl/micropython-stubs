"""
Module: 'asyncio.lock' on micropython-v1.24.0-preview-stm32-PYBV11
"""

# MCU: {'version': '1.24.0-preview', 'mpy': 'v6.3', 'port': 'stm32', 'board': 'PYBV11', 'family': 'micropython', 'build': 'preview.62.g908ab1cec', 'arch': 'armv7emsp', 'ver': '1.24.0-preview-preview.62.g908ab1cec', 'cpu': 'STM32F405RG'}
# Stubber: v1.20.0
from __future__ import annotations
from typing import Generator
from _typeshed import Incomplete

class Lock:
    def locked(self, *args, **kwargs) -> Incomplete: ...
    def release(self, *args, **kwargs) -> Incomplete: ...

    acquire: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...
