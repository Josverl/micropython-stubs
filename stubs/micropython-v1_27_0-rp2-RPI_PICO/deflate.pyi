"""
Module: 'deflate' on micropython-v1.27.0-rp2-RPI_PICO
"""

# MCU: {'mpy': 'v6.3', 'build': '', 'ver': '1.27.0', 'arch': 'armv6m', 'version': '1.27.0', 'port': 'rp2', 'board': 'RPI_PICO', 'family': 'micropython', 'board_id': 'RPI_PICO', 'variant': '', 'cpu': 'RP2040'}
# Stubber: v1.26.4
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
