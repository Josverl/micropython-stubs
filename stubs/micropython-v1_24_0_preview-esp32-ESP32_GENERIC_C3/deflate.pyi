"""
Module: 'deflate' on micropython-v1.24.0-preview-esp32-ESP32_GENERIC_C3
"""

# MCU: {'version': '1.24.0-preview', 'mpy': 'v6.3', 'port': 'esp32', 'board': 'ESP32_GENERIC_C3', 'family': 'micropython', 'build': 'preview.62.g908ab1cec', 'arch': '', 'ver': '1.24.0-preview-preview.62.g908ab1cec', 'cpu': 'ESP32C3'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete

GZIP: int = 3
RAW: int = 1
ZLIB: int = 2
AUTO: int = 0

class DeflateIO:
    def readline(self, *args, **kwargs) -> Incomplete: ...
    def readinto(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
