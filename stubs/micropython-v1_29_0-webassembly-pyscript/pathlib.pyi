"""
Module: 'pathlib' on micropython-v1.29.0-webassembly-pyscript
"""
# MCU: {'family': 'micropython', 'version': '1.29.0', 'build': '', 'ver': '1.29.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.28.6
from __future__ import annotations
from typing import Any, Final, Generator, AsyncGenerator
from _typeshed import Incomplete

def _mode_if_exists(x0) -> Incomplete:
    ...

def _clean_segment(x0) -> Incomplete:
    ...

def const(x0) -> Incomplete:
    ...


class Path():
    def is_file(self) -> Incomplete:
        ...

    def read_bytes(self) -> Incomplete:
        ...

    def read_text(self, x1) -> Incomplete:
        ...

    def is_dir(self) -> Incomplete:
        ...

    def glob(self, x1) -> Incomplete:
        ...

    def write_text(self, x1, x2) -> Incomplete:
        ...

    def with_suffix(self, x1) -> Incomplete:
        ...

    def write_bytes(self, x1) -> Incomplete:
        ...

    def resolve(self) -> Incomplete:
        ...

    def touch(self, x1) -> Incomplete:
        ...

    def rglob(self, x1) -> Incomplete:
        ...

    def rename(self, x1) -> Incomplete:
        ...

    def rmdir(self) -> Incomplete:
        ...

    def stat(self) -> Incomplete:
        ...

    def mkdir(self, x1, x2) -> Incomplete:
        ...

    def open(self, x1, x2) -> Incomplete:
        ...

    def expanduser(self) -> Incomplete:
        ...

    def absolute(self) -> Incomplete:
        ...

    def unlink(self, x1) -> Incomplete:
        ...

    def exists(self) -> Incomplete:
        ...

    async def _glob(self, x1, x2, x3) -> Incomplete:
        ...

    parent: Incomplete ## <class 'property'> = <property>
    stem: Incomplete ## <class 'property'> = <property>
    name: Incomplete ## <class 'property'> = <property>
    suffix: Incomplete ## <class 'property'> = <property>
    def __init__(self, *argv, **kwargs) -> None:
        ...

