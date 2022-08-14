"""
Module: 'esp32' on micropython-v1.18-esp32
"""
# MCU: {'ver': 'v1.18', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.18.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.18.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.5.4
from typing import Any

HEAP_DATA = 4  # type: int
HEAP_EXEC = 1  # type: int


class NVS:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def commit(self, *args, **kwargs) -> Any:
        ...

    def erase_key(self, *args, **kwargs) -> Any:
        ...

    def get_blob(self, *args, **kwargs) -> Any:
        ...

    def get_i32(self, *args, **kwargs) -> Any:
        ...

    def set_blob(self, *args, **kwargs) -> Any:
        ...

    def set_i32(self, *args, **kwargs) -> Any:
        ...


class Partition:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def find(self, *args, **kwargs) -> Any:
        ...

    BOOT = 0  # type: int
    RUNNING = 1  # type: int
    TYPE_APP = 0  # type: int
    TYPE_DATA = 1  # type: int

    def get_next_update(self, *args, **kwargs) -> Any:
        ...

    def info(self, *args, **kwargs) -> Any:
        ...

    def ioctl(self, *args, **kwargs) -> Any:
        ...

    @classmethod
    def mark_app_valid_cancel_rollback(cls, *args, **kwargs) -> Any:
        ...

    def readblocks(self, *args, **kwargs) -> Any:
        ...

    def set_boot(self, *args, **kwargs) -> Any:
        ...

    def writeblocks(self, *args, **kwargs) -> Any:
        ...


class RMT:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def bitstream_channel(self, *args, **kwargs) -> Any:
        ...

    def clock_div(self, *args, **kwargs) -> Any:
        ...

    def deinit(self, *args, **kwargs) -> Any:
        ...

    def loop(self, *args, **kwargs) -> Any:
        ...

    def source_freq(self, *args, **kwargs) -> Any:
        ...

    def wait_done(self, *args, **kwargs) -> Any:
        ...

    def write_pulses(self, *args, **kwargs) -> Any:
        ...


class ULP:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    RESERVE_MEM = 512  # type: int

    def load_binary(self, *args, **kwargs) -> Any:
        ...

    def run(self, *args, **kwargs) -> Any:
        ...

    def set_wakeup_period(self, *args, **kwargs) -> Any:
        ...


WAKEUP_ALL_LOW = False  # type: bool
WAKEUP_ANY_HIGH = True  # type: bool


def hall_sensor(*args, **kwargs) -> Any:
    ...


def idf_heap_info(*args, **kwargs) -> Any:
    ...


def raw_temperature(*args, **kwargs) -> Any:
    ...


def wake_on_ext0(*args, **kwargs) -> Any:
    ...


def wake_on_ext1(*args, **kwargs) -> Any:
    ...


def wake_on_touch(*args, **kwargs) -> Any:
    ...
