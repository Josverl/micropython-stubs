"""
Module: 'esp32' on micropython-v1.24.1-esp32-ESP32_GENERIC_S3
"""

# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'esp32', 'board': 'ESP32_GENERIC_S3', 'cpu': 'ESP32S3', 'mpy': 'v6.3', 'arch': 'xtensawin'}
# Stubber: v1.24.0
from __future__ import annotations
from _typeshed import Incomplete

WAKEUP_ALL_LOW: bool = False
WAKEUP_ANY_HIGH: bool = True
HEAP_EXEC: int = 1
HEAP_DATA: int = 4

def mcu_temperature(*args, **kwargs) -> Incomplete: ...
def idf_heap_info(*args, **kwargs) -> Incomplete: ...
def wake_on_touch(*args, **kwargs) -> Incomplete: ...
def wake_on_ext0(*args, **kwargs) -> Incomplete: ...
def wake_on_ext1(*args, **kwargs) -> Incomplete: ...
def wake_on_ulp(*args, **kwargs) -> Incomplete: ...
def gpio_deep_sleep_hold(*args, **kwargs) -> Incomplete: ...

class ULP:
    RESERVE_MEM: int = 2040
    def run(self, *args, **kwargs) -> Incomplete: ...
    def set_wakeup_period(self, *args, **kwargs) -> Incomplete: ...
    def load_binary(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class NVS:
    def get_i32(self, *args, **kwargs) -> Incomplete: ...
    def set_i32(self, *args, **kwargs) -> Incomplete: ...
    def set_blob(self, *args, **kwargs) -> Incomplete: ...
    def commit(self, *args, **kwargs) -> Incomplete: ...
    def get_blob(self, *args, **kwargs) -> Incomplete: ...
    def erase_key(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Partition:
    RUNNING: int = 1
    TYPE_APP: int = 0
    TYPE_DATA: int = 1
    BOOT: int = 0
    def readblocks(self, *args, **kwargs) -> Incomplete: ...
    def ioctl(self, *args, **kwargs) -> Incomplete: ...
    def set_boot(self, *args, **kwargs) -> Incomplete: ...
    def writeblocks(self, *args, **kwargs) -> Incomplete: ...
    def info(self, *args, **kwargs) -> Incomplete: ...
    def find(self, *args, **kwargs) -> Incomplete: ...
    def get_next_update(self, *args, **kwargs) -> Incomplete: ...
    @classmethod
    def mark_app_valid_cancel_rollback(cls, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class RMT:
    PULSE_MAX: int = 32767
    def source_freq(self, *args, **kwargs) -> Incomplete: ...
    def loop(self, *args, **kwargs) -> Incomplete: ...
    def wait_done(self, *args, **kwargs) -> Incomplete: ...
    def write_pulses(self, *args, **kwargs) -> Incomplete: ...
    def bitstream_channel(self, *args, **kwargs) -> Incomplete: ...
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def clock_div(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
