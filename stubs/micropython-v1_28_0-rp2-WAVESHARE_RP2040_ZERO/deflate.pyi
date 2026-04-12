"""
Module: 'deflate' on micropython-v1.28.0-rp2-WAVESHARE_RP2040_ZERO
"""

# MCU: {'mpy': 'v6.3', 'build': '', 'ver': '1.28.0', 'arch': 'armv6m', 'version': '1.28.0', 'port': 'rp2', 'board': 'WAVESHARE_RP2040_ZERO', 'family': 'micropython', 'board_id': 'WAVESHARE_RP2040_ZERO', 'variant': '', 'cpu': 'RP2040'}
# Stubber: v1.28.0
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
