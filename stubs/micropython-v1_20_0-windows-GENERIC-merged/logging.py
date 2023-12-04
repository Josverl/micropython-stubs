"""
Module: 'logging' on micropython-v1.20.0-win32-GENERIC
"""
# MCU: {'version': '1.20.0', 'mpy': '', 'port': 'win32', 'board': 'GENERIC', 'family': 'micropython', 'build': '', 'arch': '', 'ver': 'v1.20.0', 'cpu': ''}
# Stubber: v1.15.0
from typing import Any
from _typeshed import Incomplete

CRITICAL = 50  # type: int
INFO = 20  # type: int
ERROR = 40  # type: int
WARNING = 30  # type: int
DEBUG = 10  # type: int
NOTSET = 0  # type: int


def debug(*args, **kwargs) -> Incomplete:
    ...


def getLogger(*args, **kwargs) -> Incomplete:
    ...


def basicConfig(*args, **kwargs) -> Incomplete:
    ...


def info(*args, **kwargs) -> Incomplete:
    ...


class Logger:
    level = 0  # type: int

    def warning(self, *args, **kwargs) -> Incomplete:
        ...

    def debug(self, *args, **kwargs) -> Incomplete:
        ...

    def error(self, *args, **kwargs) -> Incomplete:
        ...

    def critical(self, *args, **kwargs) -> Incomplete:
        ...

    def exception(self, *args, **kwargs) -> Incomplete:
        ...

    def isEnabledFor(self, *args, **kwargs) -> Incomplete:
        ...

    def log(self, *args, **kwargs) -> Incomplete:
        ...

    def info(self, *args, **kwargs) -> Incomplete:
        ...

    def setLevel(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
