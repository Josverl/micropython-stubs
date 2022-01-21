"""
Module: 'logging' on micropython-v1.18-esp32
"""
# MCU: {'ver': 'v1.18', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.18.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.18.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.5.3
from typing import Any

def info(*args, **kwargs) -> Any:
    ...

def debug(*args, **kwargs) -> Any:
    ...

DEBUG = 10 # type: int
def getLogger(*args, **kwargs) -> Any:
    ...

def basicConfig(*args, **kwargs) -> Any:
    ...

INFO = 20 # type: int
CRITICAL = 50 # type: int
ERROR = 40 # type: int
WARNING = 30 # type: int
NOTSET = 0 # type: int

class Logger():
    ''
    def __init__(self, *argv, **kwargs) -> None:
        ''
        ...
    def info(self, *args, **kwargs) -> Any:
        ...

    level = 0 # type: int
    def log(self, *args, **kwargs) -> Any:
        ...

    def debug(self, *args, **kwargs) -> Any:
        ...

    def exception(self, *args, **kwargs) -> Any:
        ...

    def error(self, *args, **kwargs) -> Any:
        ...

    def warning(self, *args, **kwargs) -> Any:
        ...

    def setLevel(self, *args, **kwargs) -> Any:
        ...

    def isEnabledFor(self, *args, **kwargs) -> Any:
        ...

    def critical(self, *args, **kwargs) -> Any:
        ...

