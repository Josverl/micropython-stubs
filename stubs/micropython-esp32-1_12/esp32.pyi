
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class Partition:
    def find() -> None: ...
    def get_next_update() -> None: ...
    def info() -> None: ...
    def ioctl() -> None: ...
    def readblocks() -> None: ...
    def set_boot() -> None: ...
    def writeblocks() -> None: ...
class RMT:
    def clock_div() -> None: ...
    def deinit() -> None: ...
    def loop() -> None: ...
    def source_freq() -> None: ...
    def wait_done() -> None: ...
    def write_pulses() -> None: ...
class ULP:
    def load_binary() -> None: ...
    def run() -> None: ...
    def set_wakeup_period() -> None: ...
def hall_sensor() -> None: ...
def raw_temperature() -> None: ...
def wake_on_ext0() -> None: ...
def wake_on_ext1() -> None: ...
def wake_on_touch() -> None: ...
