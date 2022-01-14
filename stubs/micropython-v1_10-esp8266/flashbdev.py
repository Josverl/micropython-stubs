"""
Module: 'flashbdev' on esp8266 v1.10
"""
# MCU: (sysname='esp8266', nodename='esp8266', release='2.2.0-dev(9422289)', version='v1.10-8-g8b7039d7d on 2019-01-26', machine='ESP module with ESP8266')
# Stubber: 1.1.0 - updated
from typing import Any


class FlashBdev:
    """"""

    NUM_BLK = 106
    RESERVED_SECS = 1
    SEC_SIZE = 4096
    START_SEC = 153

    def ioctl(self, *args) -> Any:
        pass

    def readblocks(self, *args) -> Any:
        pass

    def writeblocks(self, *args) -> Any:
        pass


bdev = None
esp = None
size = 4194304
