"""
Module: 'upip_utarfile' on micropython-v1.14-esp8266
"""
# MCU: {'ver': 'v1.14', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '1.14', 'name': 'micropython', 'mpy': 9733, 'version': '1.14', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
# Stubber: 1.5.0
from typing import Any

DIRTYPE = "dir"  # type: str


class TarFile:
    """"""

    def __init__(self, *args) -> None:
        ...

    def next(self, *args) -> Any:
        ...

    def extractfile(self, *args) -> Any:
        ...


TAR_HEADER = {}  # type: dict
REGTYPE = "file"  # type: str


def roundup(*args) -> Any:
    ...


class FileSection:
    """"""

    def __init__(self, *args) -> None:
        ...

    def read(self, *args) -> Any:
        ...

    def readinto(self, *args) -> Any:
        ...

    def skip(self, *args) -> Any:
        ...


class TarInfo:
    """"""
