"""
Module: 'uos' on micropython-v1.17-esp8266
"""
# MCU: {'ver': 'v1.17', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '1.17', 'name': 'micropython', 'mpy': 9733, 'version': '1.17', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
# Stubber: 1.5.4
from typing import Any


def remove(*args, **kwargs) -> Any:
    ...


class VfsFat:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def open(self, *args, **kwargs) -> Any:
        ...

    def remove(self, *args, **kwargs) -> Any:
        ...

    def chdir(self, *args, **kwargs) -> Any:
        ...

    def getcwd(self, *args, **kwargs) -> Any:
        ...

    def ilistdir(self, *args, **kwargs) -> Any:
        ...

    def mkdir(self, *args, **kwargs) -> Any:
        ...

    def mkfs(self, *args, **kwargs) -> Any:
        ...

    def mount(self, *args, **kwargs) -> Any:
        ...

    def rename(self, *args, **kwargs) -> Any:
        ...

    def rmdir(self, *args, **kwargs) -> Any:
        ...

    def stat(self, *args, **kwargs) -> Any:
        ...

    def statvfs(self, *args, **kwargs) -> Any:
        ...

    def umount(self, *args, **kwargs) -> Any:
        ...


class VfsLfs2:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def open(self, *args, **kwargs) -> Any:
        ...

    def remove(self, *args, **kwargs) -> Any:
        ...

    def chdir(self, *args, **kwargs) -> Any:
        ...

    def getcwd(self, *args, **kwargs) -> Any:
        ...

    def ilistdir(self, *args, **kwargs) -> Any:
        ...

    def mkdir(self, *args, **kwargs) -> Any:
        ...

    def mkfs(self, *args, **kwargs) -> Any:
        ...

    def mount(self, *args, **kwargs) -> Any:
        ...

    def rename(self, *args, **kwargs) -> Any:
        ...

    def rmdir(self, *args, **kwargs) -> Any:
        ...

    def stat(self, *args, **kwargs) -> Any:
        ...

    def statvfs(self, *args, **kwargs) -> Any:
        ...

    def umount(self, *args, **kwargs) -> Any:
        ...


def chdir(*args, **kwargs) -> Any:
    ...


def dupterm(*args, **kwargs) -> Any:
    ...


def dupterm_notify(*args, **kwargs) -> Any:
    ...


def getcwd(*args, **kwargs) -> Any:
    ...


def ilistdir(*args, **kwargs) -> Any:
    ...


def listdir(*args, **kwargs) -> Any:
    ...


def mkdir(*args, **kwargs) -> Any:
    ...


def mount(*args, **kwargs) -> Any:
    ...


def rename(*args, **kwargs) -> Any:
    ...


def rmdir(*args, **kwargs) -> Any:
    ...


def stat(*args, **kwargs) -> Any:
    ...


def statvfs(*args, **kwargs) -> Any:
    ...


def umount(*args, **kwargs) -> Any:
    ...


def uname(*args, **kwargs) -> Any:
    ...


def urandom(*args, **kwargs) -> Any:
    ...
