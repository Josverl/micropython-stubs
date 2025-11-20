"""
Module: 'deflate' on micropython-v1.26.1-mimxrt-SEEED_ARCH_MIX
"""

# MCU: {'variant': '', 'build': '', 'arch': 'armv7emdp', 'port': 'mimxrt', 'board': 'SEEED_ARCH_MIX', 'board_id': 'SEEED_ARCH_MIX', 'mpy': 'v6.3', 'ver': '1.26.1', 'family': 'micropython', 'cpu': 'MIMXRT1052DVL5B', 'version': '1.26.1'}
# Stubber: v1.26.3
from __future__ import annotations
from typing import Final
from _typeshed import Incomplete

GZIP: Final[int] = 3
RAW: Final[int] = 1
ZLIB: Final[int] = 2
AUTO: Final[int] = 0

class DeflateIO:
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def readline(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
