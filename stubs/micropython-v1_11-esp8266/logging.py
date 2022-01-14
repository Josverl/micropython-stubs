"""
Module: 'logging' on esp8266 v1.11
"""
# MCU: (sysname='esp8266', nodename='esp8266', release='2.2.0-dev(9422289)', version='v1.11-8-g48dcbbe60 on 2019-05-29', machine='ESP module with ESP8266')
# Stubber: 1.1.0 - updated
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
