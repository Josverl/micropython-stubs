"""
Module: 'vfs' on micropython-v1.24.1-windows-GENERIC
"""
# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'windows', 'board': 'GENERIC', 'cpu': 'win32 [GCC 12.0.0] version', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Generator
from _typeshed import Incomplete

def mount(*args, **kwargs) -> Incomplete:
    ...

def umount(*args, **kwargs) -> Incomplete:
    ...


class VfsPosix():
    def rename(self, *args, **kwargs) -> Incomplete:
        ...

    def mount(self, *args, **kwargs) -> Incomplete:
        ...

    def mkdir(self, *args, **kwargs) -> Incomplete:
        ...

    def rmdir(self, *args, **kwargs) -> Incomplete:
        ...

    def stat(self, *args, **kwargs) -> Incomplete:
        ...

    def umount(self, *args, **kwargs) -> Incomplete:
        ...

    def remove(self, *args, **kwargs) -> Incomplete:
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

