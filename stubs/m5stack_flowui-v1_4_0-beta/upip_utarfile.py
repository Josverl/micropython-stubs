"""
Module: 'upip_utarfile' on M5 FlowUI v1.4.0-beta
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-284-g5d8e1c867 on 2019-08-30', machine='ESP32 module with ESP32')
# Stubber: 1.3.1 - updated
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
