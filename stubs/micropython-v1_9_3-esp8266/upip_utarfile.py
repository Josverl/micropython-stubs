"""
Module: 'upip_utarfile' on esp8266 v1.9.3
"""
# MCU: (sysname='esp8266', nodename='esp8266', release='2.0.0(5a875ba)', version='v1.9.3-8-g63826ac5c on 2017-11-01', machine='ESP module with ESP8266')
# Stubber: 1.1.2 - updated
from typing import Any

DIRTYPE = "dir"


class FileSection:
    """"""

    def read(self, *argv) -> Any:
        pass

    def readinto(self, *argv) -> Any:
        pass

    def skip(self, *argv) -> Any:
        pass


REGTYPE = "file"
TAR_HEADER = None


class TarFile:
    """"""

    def extractfile(self, *argv) -> Any:
        pass

    def next(self, *argv) -> Any:
        pass


class TarInfo:
    """"""


def roundup():
    pass


uctypes = None
