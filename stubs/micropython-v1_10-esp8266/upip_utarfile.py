"""
Module: 'upip_utarfile' on esp8266 v1.10
"""
# MCU: (sysname='esp8266', nodename='esp8266', release='2.2.0-dev(9422289)', version='v1.10-8-g8b7039d7d on 2019-01-26', machine='ESP module with ESP8266')
# Stubber: 1.1.0 - updated
from typing import Any

DIRTYPE = "dir"


class FileSection:
    """"""

    def read(self, *args) -> Any:
        pass

    def readinto(self, *args) -> Any:
        pass

    def skip(self, *args) -> Any:
        pass


REGTYPE = "file"
TAR_HEADER = None


class TarFile:
    """"""

    def extractfile(self, *args) -> Any:
        pass

    def next(self, *args) -> Any:
        pass


class TarInfo:
    """"""


def roundup(*args) -> Any:
    pass


uctypes = None
