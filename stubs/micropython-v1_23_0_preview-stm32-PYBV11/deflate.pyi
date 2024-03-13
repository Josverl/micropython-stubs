"""
Module: 'deflate' on micropython-v1.23.0-preview-stm32-PYBV11
"""
# MCU: {'version': '1.23.0-preview', 'mpy': 'v6.2', 'port': 'stm32', 'board': 'PYBV11', 'family': 'micropython', 'build': 'preview.203.gd712feb68', 'arch': 'armv7emsp', 'ver': '1.23.0-preview-preview.203.gd712feb68', 'cpu': 'STM32F405RG'}
# Stubber: v1.17.3
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
