"""
Module: 'flashbdev' on esp8266 v1.9.4
"""
# MCU: (sysname='esp8266', nodename='esp8266', release='2.2.0-dev(9422289)', version='v1.9.4-8-ga9a3caad0 on 2018-05-11', machine='ESP module with ESP8266')
# Stubber: 1.1.2 - updated
from typing import Any


class FlashBdev:
    """"""

    NUM_BLK = 106
    RESERVED_SECS = 1
    SEC_SIZE = 4096
    START_SEC = 153

    def ioctl(self, *argv) -> Any:
        pass

    def readblocks(self, *argv) -> Any:
        pass

    def writeblocks(self, *argv) -> Any:
        pass


bdev = None
esp = None
size = 4194304
