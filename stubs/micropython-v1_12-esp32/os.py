"""
Module: 'os' on micropython-v1.12-esp32
"""
# MCU: {'ver': 'v1.12', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.12.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.12.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.5.0
from typing import Any


def remove(*args) -> Any:
    ...


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


def dupterm_notify(*args) -> Any:
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


def umount(*args) -> Any:
    ...


def uname(*args) -> Any:
    ...


def urandom(*args) -> Any:
    ...
