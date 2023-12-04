"""
Module: 'deflate' on micropython-v1.22.0.preview-win32-GENERIC
"""
# MCU: {'version': '1.22.0.preview', 'mpy': '', 'port': 'win32', 'board': 'GENERIC', 'family': 'micropython', 'build': '', 'arch': '', 'ver': 'v1.22.0.preview', 'cpu': ''}
# Stubber: v1.15.0
from typing import Any
from _typeshed import Incomplete

GZIP = 3  # type: int
RAW = 1  # type: int
ZLIB = 2  # type: int
AUTO = 0  # type: int


class DeflateIO:
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
