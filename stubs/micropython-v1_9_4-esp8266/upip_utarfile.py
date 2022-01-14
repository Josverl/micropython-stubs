"""
Module: 'upip_utarfile' on esp8266 v1.9.4
"""
# MCU: (sysname='esp8266', nodename='esp8266', release='2.2.0-dev(9422289)', version='v1.9.4-8-ga9a3caad0 on 2018-05-11', machine='ESP module with ESP8266')
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
