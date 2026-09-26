"""
Module: 'mip' on micropython-v1.29.0-webassembly-pyscript
"""
# MCU: {'family': 'micropython', 'version': '1.29.0', 'build': '', 'ver': '1.29.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.29.0
from __future__ import annotations
from typing import Any, Final, Generator, AsyncGenerator
from _typeshed import Incomplete

_D: Final[bool] = True
_E: Final[str] = 'user-agent'
_F: Final[str] = 'github:'
_B: Final[str] = '/'
HEADERS_TO_IGNORE: tuple = ()
_CHUNK_SIZE: Final[int] = 128
_C: Final[bool] = False
# inspect: arity=5
def _install_package(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=2
def _chunk(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def _ensure_path_exists(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=2
def _rewrite_url(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=2
def _download_file(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=2
def _check_exists(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=5
def _install_json(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=5
def install(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=5
def request(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def get(*args, **kwargs) -> Incomplete:
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


class Response():
    # inspect: arity=1
    def json(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def close(self, *args, **kwargs) -> Incomplete:
        ...

    content: Incomplete ## <class 'property'> = <property>
    text: Incomplete ## <class 'property'> = <property>
    def __init__(self, *argv, **kwargs) -> None:
        ...

_A: Incomplete ## <class 'NoneType'> = None
