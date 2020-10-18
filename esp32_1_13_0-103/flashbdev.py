"""
Module: 'flashbdev' on esp32 1.13.0-103
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.13.0', version='v1.13-103-gb137d064e on 2020-10-09', machine='ESP32 module (spiram) with ESP32')
# Stubber: 1.3.4

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

    def mark_app_valid_cancel_rollback():
        pass

    def readblocks():
        pass

    def set_boot():
        pass

    def writeblocks():
        pass

bdev = None
