"""
Module: 'upip_utarfile' on micropython-esp32-1.10
"""
# MCU: {'ver': '1.10', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module with ESP32', 'release': '1.10.0', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.10.0'}
# Stubber: 1.4.2
from typing import Any

# import uctypes
DIRTYPE = 'dir' # type: str

class TarFile:
    ''
    def __init__(self, *args) -> None:
        ...

    def next(self, *args) -> Any:
        ...

    def extractfile(self, *args) -> Any:
        ...

TAR_HEADER = {} # type: dict
REGTYPE = 'file' # type: str
def roundup(*args) -> Any:
    ...


class FileSection:
    ''
    def __init__(self, *args) -> None:
        ...

    def read(self, *args) -> Any:
        ...

    def readinto(self, *args) -> Any:
        ...

    def skip(self, *args) -> Any:
        ...


class TarInfo:
    ''
