"""
Module: 'deflate' on micropython-v1.26.0-windows-standard
"""
# MCU: {'family': 'micropython', 'version': '1.26.0', 'build': '', 'ver': '1.26.0', 'port': 'windows', 'board': 'standard', 'board_id': 'standard', 'variant': '', 'cpu': 'win32 [GCC 12.0.0] version', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.26.2
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

GZIP: Final[int] = 3
RAW: Final[int] = 1
ZLIB: Final[int] = 2
AUTO: Final[int] = 0

class DeflateIO():
    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def readline(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def read(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

