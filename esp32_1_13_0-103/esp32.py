"""
Module: 'esp32' on esp32 1.13.0-103
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.13.0', version='v1.13-103-gb137d064e on 2020-10-09', machine='ESP32 module (spiram) with ESP32')
# Stubber: 1.3.4
HEAP_DATA = 4
HEAP_EXEC = 1

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


class RMT:
    ''
    def clock_div():
        pass

    def deinit():
        pass

    def loop():
        pass

    def source_freq():
        pass

    def wait_done():
        pass

    def write_pulses():
        pass


class ULP:
    ''
    RESERVE_MEM = 512
    def load_binary():
        pass

    def run():
        pass

    def set_wakeup_period():
        pass

WAKEUP_ALL_LOW = None
WAKEUP_ANY_HIGH = None
def hall_sensor():
    pass

def idf_heap_info():
    pass

def raw_temperature():
    pass

def wake_on_ext0():
    pass

def wake_on_ext1():
    pass

def wake_on_touch():
    pass

