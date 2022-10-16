"""
Module: 'upip_utarfile' on micropython-v1.19.1-esp8266
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp8266', 'port': 'esp8266', 'machine': 'ESP module (1M) with ESP8266', 'release': '1.19.1', 'nodename': 'esp8266', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp8266', 'version': '1.19.1'}
# Stubber: 1.5.6
from typing import Any

DIRTYPE = "dir"  # type: str


class TarFile:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def next(self, *args, **kwargs) -> Any:
        ...

    def extractfile(self, *args, **kwargs) -> Any:
        ...


class FileSection:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def read(self, *args, **kwargs) -> Any:
        ...

    def readinto(self, *args, **kwargs) -> Any:
        ...

    def skip(self, *args, **kwargs) -> Any:
        ...


class TarInfo:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...


def roundup(*args, **kwargs) -> Any:
    ...


TAR_HEADER = {}  # type: dict
REGTYPE = "file"  # type: str
