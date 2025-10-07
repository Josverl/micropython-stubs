"""
Module: 'mip' on micropython-v1.25.0-preview-webassembly
"""
# MCU: {'family': 'micropython', 'version': '1.25.0-preview', 'build': '301', 'ver': '1.25.0-preview-301', 'port': 'webassembly', 'board': '', 'board_id': '', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.26.2
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

_D: Final[bool] = True
_E: Final[str] = 'user-agent'
_F: Final[str] = 'github:'
_B: Final[str] = '/'
HEADERS_TO_IGNORE: tuple = ()
_CHUNK_SIZE: Final[int] = 128
_C: Final[bool] = False
def _install_package(*args, **kwargs) -> Incomplete:
    ...

def _chunk(*args, **kwargs) -> Incomplete:
    ...

def _ensure_path_exists(*args, **kwargs) -> Incomplete:
    ...

def _rewrite_url(*args, **kwargs) -> Incomplete:
    ...

def _download_file(*args, **kwargs) -> Incomplete:
    ...

def _check_exists(*args, **kwargs) -> Incomplete:
    ...

def _install_json(*args, **kwargs) -> Incomplete:
    ...

def install(*args, **kwargs) -> Incomplete:
    ...

def request(*args, **kwargs) -> Incomplete:
    ...

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
    def json(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    content: Incomplete ## <class 'property'> = <property>
    text: Incomplete ## <class 'property'> = <property>
    def __init__(self, *argv, **kwargs) -> None:
        ...

_A: Incomplete ## <class 'NoneType'> = None
