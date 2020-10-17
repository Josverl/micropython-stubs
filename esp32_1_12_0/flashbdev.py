"""
Module: 'flashbdev' on esp32 1.12.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.12.0', version='v1.12 on 2019-12-20', machine='ESP32 module (spiram) with ESP32')
# Stubber: 1.3.2

class Partition:
    ''
    BOOT = 0
    RUNNING = 1
    TYPE_APP = 0
    TYPE_DATA = 1
    def find():
        pass

    def get_next_update():
        pass

    def info():
        pass

    def ioctl():
        pass

    def readblocks():
        pass

    def set_boot():
        pass

    def writeblocks():
        pass

bdev = None
