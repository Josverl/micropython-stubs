"""
Module: 'deflate' on micropython-v1.23.0-preview-samd-SEEED_WIO_TERMINAL
"""
# MCU: {'version': '1.23.0-preview', 'mpy': 'v6.2', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'family': 'micropython', 'build': '203', 'arch': 'armv7emsp', 'ver': '1.23.0-preview-203', 'cpu': 'SAMD51P19A'}
# Stubber: v1.17.3
from __future__ import annotations
from _typeshed import Incomplete

GZIP: int = 3
RAW: int = 1
ZLIB: int = 2
AUTO: int = 0

class DeflateIO:
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def readline(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
