"""
Module: 'deflate' on micropython-v1.26.0-stm32-PYBV11-NETWORK
"""

# MCU: {'variant': 'NETWORK', 'build': '', 'arch': 'armv7emsp', 'port': 'stm32', 'board': 'PYBV11', 'board_id': 'PYBV11-NETWORK', 'mpy': 'v6.3', 'ver': '1.26.0', 'family': 'micropython', 'cpu': 'STM32F405RG', 'version': '1.26.0'}
# Stubber: v1.26.0
from __future__ import annotations
from typing import Final
from _typeshed import Incomplete

GZIP: Final[int] = 3
RAW: Final[int] = 1
ZLIB: Final[int] = 2
AUTO: Final[int] = 0

class DeflateIO:
    def readline(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
