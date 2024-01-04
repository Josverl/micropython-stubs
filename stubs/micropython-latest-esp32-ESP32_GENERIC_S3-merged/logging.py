"""
Module: 'logging' on micropython-v1.22.0-esp32-ESP32_GENERIC_S3
"""
# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'esp32', 'board': 'ESP32_GENERIC_S3', 'cpu': 'ESP32S3', 'mpy': 'v6.2', 'arch': 'xtensawin'}
# Stubber: v1.16.2
from _typeshed import Incomplete

WARNING = 30  # type: int
INFO = 20  # type: int
CRITICAL = 50  # type: int
ERROR = 40  # type: int
NOTSET = 0  # type: int
DEBUG = 10  # type: int


def info(*args, **kwargs) -> Incomplete:
    ...


def getLogger(*args, **kwargs) -> Incomplete:
    ...


def basicConfig(*args, **kwargs) -> Incomplete:
    ...


def debug(*args, **kwargs) -> Incomplete:
    ...


class Logger:
    level = 0  # type: int

    def error(self, *args, **kwargs) -> Incomplete:
        ...

    def warning(self, *args, **kwargs) -> Incomplete:
        ...

    def setLevel(self, *args, **kwargs) -> Incomplete:
        ...

    def isEnabledFor(self, *args, **kwargs) -> Incomplete:
        ...

    def critical(self, *args, **kwargs) -> Incomplete:
        ...

    def debug(self, *args, **kwargs) -> Incomplete:
        ...

    def info(self, *args, **kwargs) -> Incomplete:
        ...

    def log(self, *args, **kwargs) -> Incomplete:
        ...

    def exception(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
