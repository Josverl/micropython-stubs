"""
Module: 'logging' on micropython-esp32-1.16
"""
# MCU: {'ver': '1.16', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.16.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.16.0', 'machine': 'ESP32 module with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.3.9
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
