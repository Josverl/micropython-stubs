"""
Module: 'os' on micropython-v1.17-pyboard
"""
# MCU: {'ver': 'v1.17', 'port': 'pyboard', 'arch': 'armv7emsp', 'sysname': 'pyboard', 'release': '1.17.0', 'name': 'micropython', 'mpy': 7685, 'version': '1.17.0', 'machine': 'PYBv1.1 with STM32F405RG', 'build': '', 'nodename': 'pyboard', 'platform': 'pyboard', 'family': 'micropython'}
# Stubber: 1.5.2
from typing import Any


def remove(*args) -> Any:
    ...


sep = "/"  # type: str


class VfsFat:
    """"""

    def open(self, *args) -> Any:
        ...

    def remove(self, *args) -> Any:
        ...

    def chdir(self, *args) -> Any:
        ...

    def getcwd(self, *args) -> Any:
        ...

    def ilistdir(self, *args) -> Any:
        ...

    def mkdir(self, *args) -> Any:
        ...

    def mkfs(self, *args) -> Any:
        ...

    def mount(self, *args) -> Any:
        ...

    def rename(self, *args) -> Any:
        ...

    def rmdir(self, *args) -> Any:
        ...

    def stat(self, *args) -> Any:
        ...

    def statvfs(self, *args) -> Any:
        ...

    def umount(self, *args) -> Any:
        ...


class VfsLfs2:
    """"""

    def open(self, *args) -> Any:
        ...

    def remove(self, *args) -> Any:
        ...

    def chdir(self, *args) -> Any:
        ...

    def getcwd(self, *args) -> Any:
        ...

    def ilistdir(self, *args) -> Any:
        ...

    def mkdir(self, *args) -> Any:
        ...

    def mkfs(self, *args) -> Any:
        ...

    def mount(self, *args) -> Any:
        ...

    def rename(self, *args) -> Any:
        ...

    def rmdir(self, *args) -> Any:
        ...

    def stat(self, *args) -> Any:
        ...

    def statvfs(self, *args) -> Any:
        ...

    def umount(self, *args) -> Any:
        ...


def chdir(*args) -> Any:
    ...


def dupterm(*args) -> Any:
    ...


def getcwd(*args) -> Any:
    ...


def ilistdir(*args) -> Any:
    ...


def listdir(*args) -> Any:
    ...


def mkdir(*args) -> Any:
    ...


def mount(*args) -> Any:
    ...


def rename(*args) -> Any:
    ...


def rmdir(*args) -> Any:
    ...


def stat(*args) -> Any:
    ...


def statvfs(*args) -> Any:
    ...


def sync(*args) -> Any:
    ...


def umount(*args) -> Any:
    ...


def uname(*args) -> Any:
    ...


def unlink(*args) -> Any:
    ...


def urandom(*args) -> Any:
    ...
