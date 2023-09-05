"""
Module: 'esp32' on micropython-v1.20.0-449-esp32-Generic_ESP32_module_with_SPIRAM_with_ESP32
"""
# MCU: OrderedDict({'version': '1.20.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'Generic_ESP32_module_with_SPIRAM_with_ESP32', 'family': 'micropython', 'build': '449', 'arch': 'xtensawin', 'ver': 'v1.20.0-449', 'cpu': 'SPIRAM'})
# Stubber: v1.13.7
from typing import Any

WAKEUP_ALL_LOW = False # type: bool
WAKEUP_ANY_HIGH = True # type: bool
HEAP_EXEC = 1 # type: int
HEAP_DATA = 4 # type: int
def raw_temperature(*args, **kwargs) -> Any:
    ...

def idf_heap_info(*args, **kwargs) -> Any:
    ...

def wake_on_touch(*args, **kwargs) -> Any:
    ...

def wake_on_ext0(*args, **kwargs) -> Any:
    ...

def wake_on_ext1(*args, **kwargs) -> Any:
    ...

def wake_on_ulp(*args, **kwargs) -> Any:
    ...

def gpio_deep_sleep_hold(*args, **kwargs) -> Any:
    ...


class ULP():
    RESERVE_MEM = 2040 # type: int
    def run(self, *args, **kwargs) -> Any:
        ...

    def set_wakeup_period(self, *args, **kwargs) -> Any:
        ...

    def load_binary(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class NVS():
    def get_i32(self, *args, **kwargs) -> Any:
        ...

    def set_i32(self, *args, **kwargs) -> Any:
        ...

    def set_blob(self, *args, **kwargs) -> Any:
        ...

    def commit(self, *args, **kwargs) -> Any:
        ...

    def get_blob(self, *args, **kwargs) -> Any:
        ...

    def erase_key(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Partition():
    RUNNING = 1 # type: int
    TYPE_APP = 0 # type: int
    TYPE_DATA = 1 # type: int
    BOOT = 0 # type: int
    def readblocks(self, *args, **kwargs) -> Any:
        ...

    def ioctl(self, *args, **kwargs) -> Any:
        ...

    def set_boot(self, *args, **kwargs) -> Any:
        ...

    def writeblocks(self, *args, **kwargs) -> Any:
        ...

    def info(self, *args, **kwargs) -> Any:
        ...

    def find(self, *args, **kwargs) -> Any:
        ...

    def get_next_update(self, *args, **kwargs) -> Any:
        ...

    @classmethod
    def mark_app_valid_cancel_rollback(cls, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class RMT():
    def source_freq(self, *args, **kwargs) -> Any:
        ...

    def loop(self, *args, **kwargs) -> Any:
        ...

    def wait_done(self, *args, **kwargs) -> Any:
        ...

    def write_pulses(self, *args, **kwargs) -> Any:
        ...

    def bitstream_channel(self, *args, **kwargs) -> Any:
        ...

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def clock_div(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

