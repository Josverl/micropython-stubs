"""
Module: 'deflate' on micropython-v1.26.0-rp2-PIMORONI_PICOLIPO-FLASH_16M
"""

# MCU: {'mpy': 'v6.3', 'build': '', 'ver': '1.26.0', 'arch': 'armv6m', 'version': '1.26.0', 'port': 'rp2', 'board': 'PIMORONI_PICOLIPO', 'family': 'micropython', 'board_id': 'PIMORONI_PICOLIPO-FLASH_16M', 'variant': 'FLASH_16M', 'cpu': 'RP2040'}
# Stubber: v1.25.1
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
