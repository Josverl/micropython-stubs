"""
Module: 'logging' on LEGO EV3 v1.0.0
"""
# MCU: sysname=ev3, nodename=ev3, release=('v1.0.0',), version=('0.0.0',), machine=ev3
# Stubber: 1.3.2 - updated
from typing import Any

CRITICAL = 50
DEBUG = 10
ERROR = 40
INFO = 20


class Logger:
    """"""

    def _level_str(self, *argv) -> Any:
        pass

    def critical(self, *argv) -> Any:
        pass

    def debug(self, *argv) -> Any:
        pass

    def error(self, *argv) -> Any:
        pass

    def exc(self, *argv) -> Any:
        pass

    def exception(self, *argv) -> Any:
        pass

    def info(self, *argv) -> Any:
        pass

    def isEnabledFor(self, *argv) -> Any:
        pass

    level = 0

    def log(self, *argv) -> Any:
        pass

    def setLevel(self, *argv) -> Any:
        pass

    def warning(self, *argv) -> Any:
        pass


NOTSET = 0
WARNING = 30
_level = 20
_level_dict = None
_loggers = None
_stream = None


def basicConfig():
    pass


def debug():
    pass


def getLogger():
    pass


def info():
    pass


sys = None
