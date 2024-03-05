"""
Module: 'logging' on micropython-v1.22.0.preview-unix-linux_[GCC_9.4.0]_version
"""
# MCU: {'family': 'micropython', 'version': '1.22.0.preview', 'build': '', 'ver': 'v1.22.0.preview', 'port': 'unix', 'board': 'linux_[GCC_9.4.0]_version', 'cpu': '', 'mpy': '', 'arch': ''}
# Stubber: v1.15.1
from typing import Any
from _typeshed import Incomplete

CRITICAL = 50  # type: int
INFO = 20  # type: int
DEBUG = 10  # type: int
ERROR = 40  # type: int
WARNING = 30  # type: int
NOTSET = 0  # type: int


def getLogger(*args, **kwargs) -> Incomplete:
    ...


def basicConfig(*args, **kwargs) -> Incomplete:
    ...


def info(*args, **kwargs) -> Incomplete:
    ...


def debug(*args, **kwargs) -> Incomplete:
    ...


class Logger:
    level = 0  # type: int

    def warning(self, *args, **kwargs) -> Incomplete:
        ...

    def critical(self, *args, **kwargs) -> Incomplete:
        ...

    def setLevel(self, *args, **kwargs) -> Incomplete:
        ...

    def isEnabledFor(self, *args, **kwargs) -> Incomplete:
        ...

    def exception(self, *args, **kwargs) -> Incomplete:
        ...

    def log(self, *args, **kwargs) -> Incomplete:
        ...

    def error(self, *args, **kwargs) -> Incomplete:
        ...

    def info(self, *args, **kwargs) -> Incomplete:
        ...

    def debug(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
