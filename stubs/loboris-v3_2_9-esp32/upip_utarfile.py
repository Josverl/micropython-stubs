"""
Module: 'upip_utarfile' on esp32_LoBo 3.2.9
"""
# MCU: (sysname='esp32_LoBo', nodename='esp32_LoBo', release='3.2.9', version='ESP32_LoBo_v3.2.9 on 2018-04-12', machine='ESP32 board with ESP32')
# Stubber: 1.1.2 - updated
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
