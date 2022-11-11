"""
Module: 'logging' on micropython-v1.17-rp2
"""
# MCU: {'family': 'micropython', 'sysname': 'rp2', 'version': '1.17.0', 'build': '', 'mpy': 5637, 'port': 'rp2', 'platform': 'rp2', 'name': 'micropython', 'arch': 'armv7m', 'machine': 'Raspberry Pi Pico with RP2040', 'nodename': 'rp2', 'ver': 'v1.17', 'release': '1.17.0'}
# Stubber: 1.5.2
from typing import Any


def debug(*args) -> Any:
    ...


def getLogger(*args) -> Any:
    ...


def info(*args) -> Any:
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

    def __init__(self, *args) -> None:
        ...

    def debug(self, *args) -> Any:
        ...

    def log(self, *args) -> Any:
        ...

    def exception(self, *args) -> Any:
        ...

    def info(self, *args) -> Any:
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
