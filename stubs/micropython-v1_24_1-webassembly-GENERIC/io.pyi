"""
Module: 'io' on micropython-v1.24.1-webassembly
"""
# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'webassembly', 'board': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

SEEK_CUR: Final[int] = 1
SEEK_SET: Final[int] = 0
SEEK_END: Final[int] = 2
def open(*args, **kwargs) -> Incomplete:
    ...


class IOBase():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class BytesIO():
    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def flush(self, *args, **kwargs) -> Incomplete:
        ...

    def getvalue(self, *args, **kwargs) -> Incomplete:
        ...

    def seek(self, *args, **kwargs) -> Incomplete:
        ...

    def tell(self, *args, **kwargs) -> Incomplete:
        ...

    def readline(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    def read(self, *args, **kwargs) -> Incomplete:
        ...

    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class StringIO():
    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def flush(self, *args, **kwargs) -> Incomplete:
        ...

    def getvalue(self, *args, **kwargs) -> Incomplete:
        ...

    def seek(self, *args, **kwargs) -> Incomplete:
        ...

    def tell(self, *args, **kwargs) -> Incomplete:
        ...

    def readline(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    def read(self, *args, **kwargs) -> Incomplete:
        ...

    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

