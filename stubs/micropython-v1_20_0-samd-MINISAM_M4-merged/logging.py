"""
Module: 'logging' on micropython-v1.20.0-samd-MINISAM_M4
"""

# MCU: OrderedDict({'build': '', 'ver': 'v1.20.0', 'version': '1.20.0', 'port': 'samd', 'board': 'MINISAM_M4', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'SAMD51G19A', 'arch': 'armv7emsp'})
# Stubber: v1.13.7
from typing import Any

CRITICAL = 50  # type: int
DEBUG = 10  # type: int
ERROR = 40  # type: int
WARNING = 30  # type: int
INFO = 20  # type: int
NOTSET = 0  # type: int


def debug(*args, **kwargs) -> Any: ...


def getLogger(*args, **kwargs) -> Any: ...


def info(*args, **kwargs) -> Any: ...


def basicConfig(*args, **kwargs) -> Any: ...


class Logger:
    level = 0  # type: int

    def debug(self, *args, **kwargs) -> Any: ...

    def isEnabledFor(self, *args, **kwargs) -> Any: ...

    def warning(self, *args, **kwargs) -> Any: ...

    def error(self, *args, **kwargs) -> Any: ...

    def critical(self, *args, **kwargs) -> Any: ...

    def setLevel(self, *args, **kwargs) -> Any: ...

    def log(self, *args, **kwargs) -> Any: ...

    def exception(self, *args, **kwargs) -> Any: ...

    def info(self, *args, **kwargs) -> Any: ...

    def __init__(self, *argv, **kwargs) -> None: ...
