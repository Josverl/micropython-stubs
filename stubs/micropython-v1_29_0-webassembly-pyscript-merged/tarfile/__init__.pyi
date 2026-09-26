"""
Module: 'tarfile.__init__' on micropython-v1.29.0-webassembly-pyscript
"""

# MCU: {'family': 'micropython', 'version': '1.29.0', 'build': '', 'ver': '1.29.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.29.0
from __future__ import annotations
from typing import Any, Final, Generator, AsyncGenerator
from _typeshed import Incomplete

DIRTYPE: Final[str] = "dir"
REGTYPE: Final[str] = "file"
_TAR_HEADER: dict = {}

# inspect: arity=2
def _roundup(*args, **kwargs) -> Incomplete: ...

class FileSection:
    # inspect: arity=2
    def readinto(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=1
    def skip(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=2
    def read(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class TarInfo:
    # inspect: arity=1
    def isdir(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=1
    def isreg(self, *args, **kwargs) -> Incomplete: ...

    type: Incomplete  ## <class 'property'> = <property>
    def __init__(self, *argv, **kwargs) -> None: ...

class TarFile:
    # inspect: arity=4
    def _open_write(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=1
    def _close_write(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=3
    def addfile(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=2
    def extractfile(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=1
    def close(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=3
    def add(self, *args, **kwargs) -> Incomplete: ...

    # inspect: arity=1
    def next(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
