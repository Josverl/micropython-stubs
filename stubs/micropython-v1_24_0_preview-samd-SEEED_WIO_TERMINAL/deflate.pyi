"""
Module: 'deflate' on micropython-v1.24.0-preview-samd-SEEED_WIO_TERMINAL
"""

# MCU: {'version': '1.24.0-preview', 'mpy': 'v6.3', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'family': 'micropython', 'build': '62', 'arch': 'armv7emsp', 'ver': '1.24.0-preview-62', 'cpu': 'SAMD51P19A'}
# Stubber: v1.20.0
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
