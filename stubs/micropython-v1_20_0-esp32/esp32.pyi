from typing import Any

WAKEUP_ANY_HIGH: bool
WAKEUP_ALL_LOW: bool
HEAP_EXEC: int
HEAP_DATA: int

def wake_on_ulp(*args, **kwargs) -> Any: ...
def idf_heap_info(*args, **kwargs) -> Any: ...
def raw_temperature(*args, **kwargs) -> Any: ...
def wake_on_touch(*args, **kwargs) -> Any: ...
def wake_on_ext1(*args, **kwargs) -> Any: ...
def wake_on_ext0(*args, **kwargs) -> Any: ...
def hall_sensor(*args, **kwargs) -> Any: ...
def gpio_deep_sleep_hold(*args, **kwargs) -> Any: ...

class ULP:
    RESERVE_MEM: int
    def run(self, *args, **kwargs) -> Any: ...
    def set_wakeup_period(self, *args, **kwargs) -> Any: ...
    def load_binary(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class NVS:
    def get_i32(self, *args, **kwargs) -> Any: ...
    def set_i32(self, *args, **kwargs) -> Any: ...
    def set_blob(self, *args, **kwargs) -> Any: ...
    def commit(self, *args, **kwargs) -> Any: ...
    def get_blob(self, *args, **kwargs) -> Any: ...
    def erase_key(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Partition:
    RUNNING: int
    TYPE_APP: int
    TYPE_DATA: int
    BOOT: int
    def readblocks(self, *args, **kwargs) -> Any: ...
    def ioctl(self, *args, **kwargs) -> Any: ...
    def set_boot(self, *args, **kwargs) -> Any: ...
    def writeblocks(self, *args, **kwargs) -> Any: ...
    def info(self, *args, **kwargs) -> Any: ...
    def find(self, *args, **kwargs) -> Any: ...
    def get_next_update(self, *args, **kwargs) -> Any: ...
    @classmethod
    def mark_app_valid_cancel_rollback(cls, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class RMT:
    def source_freq(self, *args, **kwargs) -> Any: ...
    def loop(self, *args, **kwargs) -> Any: ...
    def wait_done(self, *args, **kwargs) -> Any: ...
    def write_pulses(self, *args, **kwargs) -> Any: ...
    def bitstream_channel(self, *args, **kwargs) -> Any: ...
    def deinit(self, *args, **kwargs) -> Any: ...
    def clock_div(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...
