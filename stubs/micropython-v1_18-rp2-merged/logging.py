"""
Module: 'logging' on micropython-v1.18-rp2
"""
# MCU: {'family': 'micropython', 'sysname': 'rp2', 'version': '1.18.0', 'build': '', 'mpy': 5637, 'port': 'rp2', 'platform': 'rp2', 'name': 'micropython', 'arch': 'armv7m', 'machine': 'Arduino Nano RP2040 Connect with RP2040', 'nodename': 'rp2', 'ver': 'v1.18', 'release': '1.18.0'}
# Stubber: 1.5.3
from typing import Any


def getLogger(*args, **kwargs) -> Any:
    ...


def info(*args, **kwargs) -> Any:
    ...


def debug(*args, **kwargs) -> Any:
    ...


def basicConfig(*args, **kwargs) -> Any:
    ...


INFO = 20  # type: int
CRITICAL = 50  # type: int
ERROR = 40  # type: int
WARNING = 30  # type: int
DEBUG = 10  # type: int
NOTSET = 0  # type: int


class Logger:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def log(self, *args, **kwargs) -> Any:
        ...

    def exception(self, *args, **kwargs) -> Any:
        ...

    def info(self, *args, **kwargs) -> Any:
        ...

    def debug(self, *args, **kwargs) -> Any:
        ...

    def error(self, *args, **kwargs) -> Any:
        ...

    def warning(self, *args, **kwargs) -> Any:
        ...

    level = 0  # type: int

    def setLevel(self, *args, **kwargs) -> Any:
        ...

    def isEnabledFor(self, *args, **kwargs) -> Any:
        ...

    def critical(self, *args, **kwargs) -> Any:
        ...
