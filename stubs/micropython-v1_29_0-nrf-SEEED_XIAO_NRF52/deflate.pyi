"""
Module: 'deflate' on micropython-v1.29.0-nrf-SEEED_XIAO_NRF52
"""

# MCU: {'variant': '', 'build': '', 'arch': 'armv7emsp', 'port': 'nrf', 'board': 'SEEED_XIAO_NRF52', 'board_id': 'SEEED_XIAO_NRF52', 'mpy': 'v6.3', 'ver': '1.29.0', 'family': 'micropython', 'cpu': 'NRF52840', 'version': '1.29.0'}
# Stubber: v1.28.6
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
