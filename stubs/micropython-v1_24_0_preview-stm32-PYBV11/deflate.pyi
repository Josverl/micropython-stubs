"""
Module: 'deflate' on micropython-v1.24.0-preview-stm32-PYBV11
"""

# MCU: {'version': '1.24.0-preview', 'mpy': 'v6.3', 'port': 'stm32', 'board': 'PYBV11', 'family': 'micropython', 'build': 'preview.60.gcebc9b0ae', 'arch': 'armv7emsp', 'ver': '1.24.0-preview-preview.60.gcebc9b0ae', 'cpu': 'STM32F405RG'}
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
