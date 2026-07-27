"""
Module: 'hashlib' on micropython-v1.28.0-unix-standard
"""
# MCU: {'family': 'micropython', 'version': '1.28.0', 'build': '', 'ver': '1.28.0', 'port': 'unix', 'board': 'standard', 'board_id': 'standard', 'variant': '', 'cpu': 'linux [GCC 12.5.0] version', 'mpy': 'v6.3', 'arch': 'x64'}
# Stubber: v1.28.3
from __future__ import annotations
from typing import Any, Final, Generator, AsyncGenerator
from _typeshed import Incomplete

def new(*args, **kwargs) -> Incomplete:
    ...


class sha1():
    def digest(self, *args, **kwargs) -> Incomplete:
        ...

    def update(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class sha512():
    digestsize: int = 64
    digest_size: int = 64
    _iv: list = []
    block_size: int = 128
    def _final(self, *args, **kwargs) -> Incomplete:
        ...

    def _transform(self, *args, **kwargs) -> Incomplete:
        ...

    def _update(self, *args, **kwargs) -> Incomplete:
        ...

    def hexdigest(self, *args, **kwargs) -> Incomplete:
        ...

    def copy(self, *args, **kwargs) -> Incomplete:
        ...

    def digest(self, *args, **kwargs) -> Incomplete:
        ...

    def update(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class md5():
    def digest(self, *args, **kwargs) -> Incomplete:
        ...

    def update(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class sha384():
    digestsize: int = 48
    digest_size: int = 48
    _iv: list = []
    block_size: int = 128
    def _final(self, *args, **kwargs) -> Incomplete:
        ...

    def _transform(self, *args, **kwargs) -> Incomplete:
        ...

    def _update(self, *args, **kwargs) -> Incomplete:
        ...

    def hexdigest(self, *args, **kwargs) -> Incomplete:
        ...

    def copy(self, *args, **kwargs) -> Incomplete:
        ...

    def digest(self, *args, **kwargs) -> Incomplete:
        ...

    def update(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class sha256():
    def digest(self, *args, **kwargs) -> Incomplete:
        ...

    def update(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class sha224():
    digestsize: int = 28
    digest_size: int = 28
    _iv: list = []
    block_size: int = 64
    def _final(self, *args, **kwargs) -> Incomplete:
        ...

    def _transform(self, *args, **kwargs) -> Incomplete:
        ...

    def _update(self, *args, **kwargs) -> Incomplete:
        ...

    def hexdigest(self, *args, **kwargs) -> Incomplete:
        ...

    def copy(self, *args, **kwargs) -> Incomplete:
        ...

    def digest(self, *args, **kwargs) -> Incomplete:
        ...

    def update(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

