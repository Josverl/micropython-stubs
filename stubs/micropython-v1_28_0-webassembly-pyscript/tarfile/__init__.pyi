"""
Module: 'tarfile.__init__' on micropython-v1.28.0-webassembly-pyscript
"""
# MCU: {'family': 'micropython', 'version': '1.28.0', 'build': '', 'ver': '1.28.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.28.3
from __future__ import annotations
from typing import Any, Final, Generator, AsyncGenerator
from _typeshed import Incomplete

DIRTYPE: Final[str] = 'dir'
REGTYPE: Final[str] = 'file'
_TAR_HEADER: dict = {}
def _roundup(x0, x1) -> Incomplete:
    ...


class FileSection():
    def readinto(self, x1) -> Incomplete:
        ...

    def skip(self) -> Incomplete:
        ...

    def read(self, x1) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class TarInfo():
    def isdir(self) -> Incomplete:
        ...

    def isreg(self) -> Incomplete:
        ...

    type: Incomplete ## <class 'property'> = <property>
    def __init__(self, *argv, **kwargs) -> None:
        ...


class TarFile():
    def _open_write(self, x1, x2, x3) -> Incomplete:
        ...

    def _close_write(self) -> Incomplete:
        ...

    def addfile(self, x1, x2) -> Incomplete:
        ...

    def extractfile(self, x1) -> Incomplete:
        ...

    def close(self) -> Incomplete:
        ...

    def add(self, x1, x2) -> Incomplete:
        ...

    def next(self) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

