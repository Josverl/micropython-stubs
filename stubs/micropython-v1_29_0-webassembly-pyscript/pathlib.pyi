"""
Module: 'pathlib' on micropython-v1.29.0-webassembly-pyscript
"""
# MCU: {'family': 'micropython', 'version': '1.29.0', 'build': '', 'ver': '1.29.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.29.0
from __future__ import annotations
from typing import Any, Final, Generator, AsyncGenerator
from _typeshed import Incomplete

# inspect: arity=1
def _mode_if_exists(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def _clean_segment(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def const(*args, **kwargs) -> Incomplete:
    ...


class Path():
    # inspect: arity=1
    def is_file(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def read_bytes(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=2
    def read_text(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def is_dir(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=2
    def glob(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=3
    def write_text(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=2
    def with_suffix(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=2
    def write_bytes(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def resolve(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=2
    def touch(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=2
    def rglob(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=2
    def rename(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def rmdir(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def stat(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=3
    def mkdir(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=3
    def open(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def expanduser(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def absolute(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=2
    def unlink(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=1
    def exists(self, *args, **kwargs) -> Incomplete:
        ...

    # inspect: arity=4
    async def _glob(self, *args, **kwargs) -> Incomplete:
        ...

    parent: Incomplete ## <class 'property'> = <property>
    stem: Incomplete ## <class 'property'> = <property>
    name: Incomplete ## <class 'property'> = <property>
    suffix: Incomplete ## <class 'property'> = <property>
    def __init__(self, *argv, **kwargs) -> None:
        ...

