"""
Module: 'logging' on pyboard 1.13.0-95
"""
# MCU: (sysname='pyboard', nodename='pyboard', release='1.13.0', version='v1.13-95-g0fff2e03f on 2020-10-03', machine='PYBv1.1 with STM32F405RG')
# Stubber: 1.3.4 - updated
from typing import Any

CRITICAL = 50
DEBUG = 10
ERROR = 40
INFO = 20


class Logger:
    """"""

    def _level_str(self, *args) -> Any:
        pass

    def critical(self, *args) -> Any:
        pass

    def debug(self, *args) -> Any:
        pass

    def error(self, *args) -> Any:
        pass

    def exc(self, *args) -> Any:
        pass

    def exception(self, *args) -> Any:
        pass

    def info(self, *args) -> Any:
        pass

    def isEnabledFor(self, *args) -> Any:
        pass

    level = 0

    def log(self, *args) -> Any:
        pass

    def setLevel(self, *args) -> Any:
        pass

    def warning(self, *args) -> Any:
        pass


NOTSET = 0
WARNING = 30
_level = 20
_level_dict = None
_loggers = None
_stream = None


def basicConfig(*args) -> Any:
    pass


def debug(*args) -> Any:
    pass


def getLogger(*args) -> Any:
    pass


def info(*args) -> Any:
    pass


sys = None
