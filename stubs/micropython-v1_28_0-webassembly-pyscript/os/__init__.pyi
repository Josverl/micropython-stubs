"""
Module: 'os.__init__' on micropython-v1.28.0-webassembly-pyscript
"""
# MCU: {'family': 'micropython', 'version': '1.28.0', 'build': '', 'ver': '1.28.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.28.3
from __future__ import annotations
from typing import Any, Final, Generator, AsyncGenerator
from _typeshed import Incomplete

sep: str = '/'
def rename(x0, x1) -> Incomplete:
    ...

def rmdir(x0) -> Incomplete:
    ...

def mount(*args, **kwargs) -> Incomplete:
    ...

def unlink(x0) -> Incomplete:
    ...

def umount(x0) -> Incomplete:
    ...

def stat(x0) -> Incomplete:
    ...

def statvfs(x0) -> Incomplete:
    ...

def chdir(x0) -> Incomplete:
    ...

def getcwd() -> Incomplete:
    ...

def remove(x0) -> Incomplete:
    ...

def mkdir(x0) -> Incomplete:
    ...

def ilistdir(*args, **kwargs) -> Incomplete:
    ...

def listdir(*args, **kwargs) -> Incomplete:
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

