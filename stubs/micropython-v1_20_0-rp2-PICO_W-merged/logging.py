"""
Module: 'logging' on micropython-v1.20-rp2-PICO_W
"""
# MCU: OrderedDict({'family': 'micropython', 'version': '1.20', 'build': '', 'ver': 'v1.20', 'port': 'rp2', 'board': 'PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.1', 'arch': 'armv6m'})
# Stubber: v1.12.2
from typing import Any

WARNING = 30  # type: int
INFO = 20  # type: int
CRITICAL = 50  # type: int
ERROR = 40  # type: int
DEBUG = 10  # type: int
NOTSET = 0  # type: int


def info(*args, **kwargs) -> Any:
    ...


def debug(*args, **kwargs) -> Any:
    ...


def getLogger(*args, **kwargs) -> Any:
    ...


def basicConfig(*args, **kwargs) -> Any:
    ...


class Logger:
    level = 0  # type: int

    def warning(self, *args, **kwargs) -> Any:
        ...

    def critical(self, *args, **kwargs) -> Any:
        ...

    def setLevel(self, *args, **kwargs) -> Any:
        ...

    def isEnabledFor(self, *args, **kwargs) -> Any:
        ...

    def exception(self, *args, **kwargs) -> Any:
        ...

    def log(self, *args, **kwargs) -> Any:
        ...

    def error(self, *args, **kwargs) -> Any:
        ...

    def info(self, *args, **kwargs) -> Any:
        ...

    def debug(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
