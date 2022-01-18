"""
Module: 'logging' on micropython-v1.18-pyboard
"""
# MCU: {'ver': 'v1.18', 'port': 'pyboard', 'arch': 'armv7emsp', 'sysname': 'pyboard', 'release': '1.18.0', 'name': 'micropython', 'mpy': 7685, 'version': '1.18.0', 'machine': 'PYBv1.1 with STM32F405RG', 'build': '', 'nodename': 'pyboard', 'platform': 'pyboard', 'family': 'micropython'}
# Stubber: 1.5.2
from typing import Any


def debug(*args) -> Any:
    ...


def info(*args) -> Any:
    ...


def getLogger(*args) -> Any:
    ...


def basicConfig(*args) -> Any:
    ...


INFO = 20  # type: int
CRITICAL = 50  # type: int
ERROR = 40  # type: int
WARNING = 30  # type: int
DEBUG = 10  # type: int
NOTSET = 0  # type: int


class Logger:
    """"""

    def __init__(self, *argv) -> None:
        """"""
        ...

    def __init__(self, *args) -> None:
        ...

    def debug(self, *args) -> Any:
        ...

    def info(self, *args) -> Any:
        ...

    def log(self, *args) -> Any:
        ...

    def exception(self, *args) -> Any:
        ...

    def error(self, *args) -> Any:
        ...

    def warning(self, *args) -> Any:
        ...

    level = 0  # type: int

    def setLevel(self, *args) -> Any:
        ...

    def isEnabledFor(self, *args) -> Any:
        ...

    def critical(self, *args) -> Any:
        ...
