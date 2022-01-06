"""
Module: 'flashbdev' on esp8266 v1.9.3
"""
# MCU: (sysname='esp8266', nodename='esp8266', release='2.0.0(5a875ba)', version='v1.9.3-8-g63826ac5c on 2017-11-01', machine='ESP module with ESP8266')
# Stubber: 1.1.2

class FlashBdev:
    ''
    NUM_BLK = 106
    RESERVED_SECS = 1
    SEC_SIZE = 4096
    START_SEC = 153
    def ioctl():
        pass

    def readblocks():
        pass

    def writeblocks():
        pass

bdev = None
esp = None
size = 4194304
