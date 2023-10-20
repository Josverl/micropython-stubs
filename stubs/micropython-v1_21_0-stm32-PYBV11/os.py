"""
Module: 'os' on micropython-v1.21.0-stm32-PYBV11
"""
# MCU: {'version': '1.21.0', 'mpy': 'v6.1', 'port': 'stm32', 'board': 'PYBV11', 'family': 'micropython', 'build': '', 'arch': 'armv7emsp', 'ver': 'v1.21.0', 'cpu': 'STM32F405RG'}
# Stubber: v1.13.8
from typing import Any
from _typeshed import Incomplete

sep = "/"  # type: str


def statvfs(*args, **kwargs) -> Incomplete:
    ...


def stat(*args, **kwargs) -> Incomplete:
    ...


def rmdir(*args, **kwargs) -> Incomplete:
    ...


def rename(*args, **kwargs) -> Incomplete:
    ...


def mount(*args, **kwargs) -> Incomplete:
    ...


def sync(*args, **kwargs) -> Incomplete:
    ...


def unlink(*args, **kwargs) -> Incomplete:
    ...


def uname(*args, **kwargs) -> Incomplete:
    ...


def umount(*args, **kwargs) -> Incomplete:
    ...


def urandom(*args, **kwargs) -> Incomplete:
    ...


def chdir(*args, **kwargs) -> Incomplete:
    ...


def dupterm(*args, **kwargs) -> Incomplete:
    ...


def remove(*args, **kwargs) -> Incomplete:
    ...


def mkdir(*args, **kwargs) -> Incomplete:
    ...


def getcwd(*args, **kwargs) -> Incomplete:
    ...


def listdir(*args, **kwargs) -> Incomplete:
    ...


def ilistdir(*args, **kwargs) -> Incomplete:
    ...


class VfsLfs2:
    def rename(self, *args, **kwargs) -> Incomplete:
        ...

    def mkfs(self, *args, **kwargs) -> Incomplete:
        ...

    def mount(self, *args, **kwargs) -> Incomplete:
        ...

    def statvfs(self, *args, **kwargs) -> Incomplete:
        ...

    def rmdir(self, *args, **kwargs) -> Incomplete:
        ...

    def stat(self, *args, **kwargs) -> Incomplete:
        ...

    def umount(self, *args, **kwargs) -> Incomplete:
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


class VfsFat:
    def rename(self, *args, **kwargs) -> Incomplete:
        ...

    def mkfs(self, *args, **kwargs) -> Incomplete:
        ...

    def mount(self, *args, **kwargs) -> Incomplete:
        ...

    def statvfs(self, *args, **kwargs) -> Incomplete:
        ...

    def rmdir(self, *args, **kwargs) -> Incomplete:
        ...

    def stat(self, *args, **kwargs) -> Incomplete:
        ...

    def umount(self, *args, **kwargs) -> Incomplete:
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
