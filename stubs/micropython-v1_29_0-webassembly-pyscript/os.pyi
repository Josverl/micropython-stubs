"""
Module: 'os' on micropython-v1.29.0-webassembly-pyscript
"""
# MCU: {'family': 'micropython', 'version': '1.29.0', 'build': '', 'ver': '1.29.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.28.6
from __future__ import annotations
from typing import Any, Final, Generator, AsyncGenerator
from _typeshed import Incomplete

sep: str = '/'
def namedtuple(x0, x1) -> Incomplete:
    ...

def umount(x0) -> Incomplete:
    ...

def mount(*args, **kwargs) -> Incomplete:
    ...

def statvfs(x0) -> Incomplete:
    ...

def stat(x0) -> Incomplete:
    ...

def rename(x0, x1) -> Incomplete:
    ...

def rmdir(x0) -> Incomplete:
    ...

def unlink(x0) -> Incomplete:
    ...

def chdir(x0) -> Incomplete:
    ...

def remove(x0) -> Incomplete:
    ...

def mkdir(x0) -> Incomplete:
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

