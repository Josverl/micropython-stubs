"""
Module: 'pathlib' on micropython-v1.24.1-webassembly
"""
# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'webassembly', 'board': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

def _mode_if_exists(*args, **kwargs) -> Incomplete:
    ...

def _clean_segment(*args, **kwargs) -> Incomplete:
    ...

def const(*args, **kwargs) -> Incomplete:
    ...


class Path():
    def read_bytes(self, *args, **kwargs) -> Incomplete:
        ...

    def read_text(self, *args, **kwargs) -> Incomplete:
        ...

    def glob(self, *args, **kwargs) -> Incomplete:
        ...

    def is_file(self, *args, **kwargs) -> Incomplete:
        ...

    def is_dir(self, *args, **kwargs) -> Incomplete:
        ...

    def with_suffix(self, *args, **kwargs) -> Incomplete:
        ...

    def write_bytes(self, *args, **kwargs) -> Incomplete:
        ...

    def resolve(self, *args, **kwargs) -> Incomplete:
        ...

    def touch(self, *args, **kwargs) -> Incomplete:
        ...

    def rglob(self, *args, **kwargs) -> Incomplete:
        ...

    def write_text(self, *args, **kwargs) -> Incomplete:
        ...

    def rename(self, *args, **kwargs) -> Incomplete:
        ...

    def rmdir(self, *args, **kwargs) -> Incomplete:
        ...

    def exists(self, *args, **kwargs) -> Incomplete:
        ...

    def mkdir(self, *args, **kwargs) -> Incomplete:
        ...

    def open(self, *args, **kwargs) -> Incomplete:
        ...

    def stat(self, *args, **kwargs) -> Incomplete:
        ...

    def absolute(self, *args, **kwargs) -> Incomplete:
        ...

    def unlink(self, *args, **kwargs) -> Incomplete:
        ...

    parent: Incomplete ## <class 'property'> = <property>
    def _glob(*args, **kwargs) -> Generator:  ## = <generator>
        ...

    stem: Incomplete ## <class 'property'> = <property>
    name: Incomplete ## <class 'property'> = <property>
    suffix: Incomplete ## <class 'property'> = <property>
    def __init__(self, *argv, **kwargs) -> None:
        ...

