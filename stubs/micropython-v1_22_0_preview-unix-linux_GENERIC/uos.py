"""
Module: 'uos' on micropython-v1.22.0.preview-unix-linux_[GCC_9.4.0]_version
"""
# MCU: {'family': 'micropython', 'version': '1.22.0.preview', 'build': '', 'ver': 'v1.22.0.preview', 'port': 'unix', 'board': 'linux_[GCC_9.4.0]_version', 'cpu': '', 'mpy': '', 'arch': ''}
# Stubber: v1.15.1
from typing import Any
from _typeshed import Incomplete

sep = "/"  # type: str


def rename(*args, **kwargs) -> Incomplete:
    ...


def rmdir(*args, **kwargs) -> Incomplete:
    ...


def stat(*args, **kwargs) -> Incomplete:
    ...


def putenv(*args, **kwargs) -> Incomplete:
    ...


def mount(*args, **kwargs) -> Incomplete:
    ...


def mkdir(*args, **kwargs) -> Incomplete:
    ...


def unlink(*args, **kwargs) -> Incomplete:
    ...


def unsetenv(*args, **kwargs) -> Incomplete:
    ...


def statvfs(*args, **kwargs) -> Incomplete:
    ...


def umount(*args, **kwargs) -> Incomplete:
    ...


def system(*args, **kwargs) -> Incomplete:
    ...


def urandom(*args, **kwargs) -> Incomplete:
    ...


def chdir(*args, **kwargs) -> Incomplete:
    ...


def errno(*args, **kwargs) -> Incomplete:
    ...


def remove(*args, **kwargs) -> Incomplete:
    ...


def listdir(*args, **kwargs) -> Incomplete:
    ...


def getcwd(*args, **kwargs) -> Incomplete:
    ...


def ilistdir(*args, **kwargs) -> Incomplete:
    ...


def getenv(*args, **kwargs) -> Incomplete:
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


class VfsPosix:
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


class VfsLfs1:
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
