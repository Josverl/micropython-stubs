"""
Module: 'esp32' on micropython-esp32-1.16
"""
# MCU: {'ver': '1.16', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.16.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.16.0', 'machine': 'ESP32 module with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.3.9
HEAP_DATA = 4
HEAP_EXEC = 1

class NVS:
    ''
    def commit():
        pass

    def erase_key():
        pass

    def get_blob():
        pass

    def get_i32():
        pass

    def set_blob():
        pass

    def set_i32():
        pass


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

