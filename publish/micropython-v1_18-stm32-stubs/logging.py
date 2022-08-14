"""
Module: 'logging' on micropython-v1.18-stm32
"""
# MCU: {'ver': 'v1.18', 'port': 'stm32', 'arch': 'armv7emsp', 'sysname': 'pyboard', 'release': '1.18.0', 'name': 'micropython', 'mpy': 7685, 'version': '1.18.0', 'machine': 'PYBv1.1 with STM32F405RG', 'build': '', 'nodename': 'pyboard', 'platform': 'stm32', 'family': 'micropython'}
# Stubber: 1.5.6
from typing import Any


def debug(*args, **kwargs) -> Any:
    ...


def info(*args, **kwargs) -> Any:
    ...


def getLogger(*args, **kwargs) -> Any:
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

    def debug(self, *args, **kwargs) -> Any:
        ...

    def info(self, *args, **kwargs) -> Any:
        ...

    def log(self, *args, **kwargs) -> Any:
        ...

    def exception(self, *args, **kwargs) -> Any:
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
