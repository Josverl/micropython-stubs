"""
Module: 'esp32' on micropython-v1.15-esp32
"""
# MCU: {'ver': 'v1.15', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.15.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.15.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.5.0
from typing import Any

HEAP_DATA = 4  # type: int
HEAP_EXEC = 1  # type: int


class NVS:
    """"""

    def commit(self, *args) -> Any:
        ...

    def erase_key(self, *args) -> Any:
        ...

    def get_blob(self, *args) -> Any:
        ...

    def get_i32(self, *args) -> Any:
        ...

    def set_blob(self, *args) -> Any:
        ...

    def set_i32(self, *args) -> Any:
        ...


class Partition:
    """"""

    def find(self, *args) -> Any:
        ...

    BOOT = 0  # type: int
    RUNNING = 1  # type: int
    TYPE_APP = 0  # type: int
    TYPE_DATA = 1  # type: int

    def get_next_update(self, *args) -> Any:
        ...

    def info(self, *args) -> Any:
        ...

    def ioctl(self, *args) -> Any:
        ...

    @classmethod
    def mark_app_valid_cancel_rollback(cls, *args) -> Any:
        ...

    def readblocks(self, *args) -> Any:
        ...

    def set_boot(self, *args) -> Any:
        ...

    def writeblocks(self, *args) -> Any:
        ...


class RMT:
    """"""

    def clock_div(self, *args) -> Any:
        ...

    def deinit(self, *args) -> Any:
        ...

    def loop(self, *args) -> Any:
        ...

    def source_freq(self, *args) -> Any:
        ...

    def wait_done(self, *args) -> Any:
        ...

    def write_pulses(self, *args) -> Any:
        ...


class ULP:
    """"""

    RESERVE_MEM = 512  # type: int

    def load_binary(self, *args) -> Any:
        ...

    def run(self, *args) -> Any:
        ...

    def set_wakeup_period(self, *args) -> Any:
        ...


WAKEUP_ALL_LOW = False  # type: bool
WAKEUP_ANY_HIGH = True  # type: bool


def hall_sensor(*args) -> Any:
    ...


def idf_heap_info(*args) -> Any:
    ...


def raw_temperature(*args) -> Any:
    ...


def wake_on_ext0(*args) -> Any:
    ...


def wake_on_ext1(*args) -> Any:
    ...


def wake_on_touch(*args) -> Any:
    ...
