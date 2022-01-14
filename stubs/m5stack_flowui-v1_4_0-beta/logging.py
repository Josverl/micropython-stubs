"""
Module: 'logging' on M5 FlowUI v1.4.0-beta
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-284-g5d8e1c867 on 2019-08-30', machine='ESP32 module with ESP32')
# Stubber: 1.3.1 - updated
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
