"""
Module: 'tarfile.__init__' on micropython-v1.25.0-preview-webassembly
"""
# MCU: {'family': 'micropython', 'version': '1.25.0-preview', 'build': '301', 'ver': '1.25.0-preview-301', 'port': 'webassembly', 'board': '', 'board_id': '', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.26.2
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

DIRTYPE: Final[str] = 'dir'
REGTYPE: Final[str] = 'file'
_TAR_HEADER: dict = {}
def _roundup(*args, **kwargs) -> Incomplete:
    ...


class FileSection():
    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def skip(self, *args, **kwargs) -> Incomplete:
        ...

    def read(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class TarInfo():
    def isdir(self, *args, **kwargs) -> Incomplete:
        ...

    def isreg(self, *args, **kwargs) -> Incomplete:
        ...

    type: Incomplete ## <class 'property'> = <property>
    def __init__(self, *argv, **kwargs) -> None:
        ...


class TarFile():
    def _open_write(self, *args, **kwargs) -> Incomplete:
        ...

    def _close_write(self, *args, **kwargs) -> Incomplete:
        ...

    def addfile(self, *args, **kwargs) -> Incomplete:
        ...

    def extractfile(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    def add(self, *args, **kwargs) -> Incomplete:
        ...

    def next(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

