"""
Module: 'upip_utarfile' on LEGO EV3 v1.0.0
"""
# MCU: sysname=ev3, nodename=ev3, release=('v1.0.0',), version=('0.0.0',), machine=ev3
# Stubber: 1.3.2 - updated
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
