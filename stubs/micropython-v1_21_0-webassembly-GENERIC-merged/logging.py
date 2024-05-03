"""
Module: 'logging' on micropython-v1.21.0-webassembly-GENERIC
"""

# MCU: {'family': 'micropython', 'version': '1.21.0', 'build': '', 'ver': 'v1.21.0', 'port': 'webassembly', 'board': 'GENERIC', 'cpu': 'Emscripten', 'mpy': '', 'arch': ''}
# Stubber: v1.15.0
from typing import Any
from _typeshed import Incomplete

DEBUG = 10  # type: int
INFO = 20  # type: int
WARNING = 30  # type: int
CRITICAL = 50  # type: int
ERROR = 40  # type: int
NOTSET = 0  # type: int


def getLogger(*args, **kwargs) -> Incomplete: ...


def basicConfig(*args, **kwargs) -> Incomplete: ...


def info(*args, **kwargs) -> Incomplete: ...


def debug(*args, **kwargs) -> Incomplete: ...


class Logger:
    level = 0  # type: int

    def setLevel(self, *args, **kwargs) -> Incomplete: ...

    def exception(self, *args, **kwargs) -> Incomplete: ...

    def isEnabledFor(self, *args, **kwargs) -> Incomplete: ...

    def critical(self, *args, **kwargs) -> Incomplete: ...

    def info(self, *args, **kwargs) -> Incomplete: ...

    def log(self, *args, **kwargs) -> Incomplete: ...

    def warning(self, *args, **kwargs) -> Incomplete: ...

    def debug(self, *args, **kwargs) -> Incomplete: ...

    def error(self, *args, **kwargs) -> Incomplete: ...

    def __init__(self, *argv, **kwargs) -> None: ...
