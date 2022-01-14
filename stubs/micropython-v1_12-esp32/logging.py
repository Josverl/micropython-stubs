"""
Module: 'logging' on esp32 1.12.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.12.0', version='v1.12 on 2019-12-20', machine='ESP32 module (spiram) with ESP32')
# Stubber: 1.3.2
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
