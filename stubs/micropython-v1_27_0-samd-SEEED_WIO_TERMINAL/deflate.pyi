"""
Module: 'deflate' on micropython-v1.27.0-samd-SEEED_WIO_TERMINAL
"""

# MCU: {'variant': '', 'build': '', 'arch': 'armv7emsp', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'board_id': 'SEEED_WIO_TERMINAL', 'mpy': 'v6.3', 'ver': '1.27.0', 'family': 'micropython', 'cpu': 'SAMD51P19A', 'version': '1.27.0'}
# Stubber: v1.26.4
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
