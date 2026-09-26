"""
Module: 'os.__init__' on micropython-v1.29.0-webassembly-pyscript
"""
# MCU: {'family': 'micropython', 'version': '1.29.0', 'build': '', 'ver': '1.29.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.29.0
from __future__ import annotations
from typing import Any, Final, Generator, AsyncGenerator
from _typeshed import Incomplete

sep: str = '/'
# inspect: arity=2
def namedtuple(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def umount(*args, **kwargs) -> Incomplete:
    ...

def mount(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def statvfs(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def stat(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=2
def rename(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def rmdir(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def unlink(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def chdir(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def remove(*args, **kwargs) -> Incomplete:
    ...

# inspect: arity=1
def mkdir(*args, **kwargs) -> Incomplete:
    ...

def listdir(*args, **kwargs) -> Incomplete:
    ...

def getcwd() -> Incomplete:
    ...

def ilistdir(*args, **kwargs) -> Incomplete:
    ...


class stat_result():
    def index(self, *args, **kwargs) -> Incomplete:
        ...

    def count(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class VfsPosix():
    def rename(self, *args, **kwargs) -> Incomplete:
        ...

    def umount(self, *args, **kwargs) -> Incomplete:
        ...

    def mount(self, *args, **kwargs) -> Incomplete:
        ...

    def statvfs(self, *args, **kwargs) -> Incomplete:
        ...

    def rmdir(self, *args, **kwargs) -> Incomplete:
        ...

    def stat(self, *args, **kwargs) -> Incomplete:
        ...

    def remove(self, *args, **kwargs) -> Incomplete:
        ...

    def mkdir(self, *args, **kwargs) -> Incomplete:
        ...

    def open(self, *args, **kwargs) -> Incomplete:
        ...

    def ilistdir(self, *args, **kwargs) -> Incomplete:
        ...

    def chdir(self, *args, **kwargs) -> Incomplete:
        ...

    def getcwd(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

