
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class AK8963:
    def _register_char() -> None: ...
    def _register_short() -> None: ...
    def _register_three_shorts() -> None: ...
class I2C:
    def address() -> None: ...
    def begin() -> None: ...
    def callback() -> None: ...
    def clock_timing() -> None: ...
    def data_timing() -> None: ...
    def deinit() -> None: ...
    def end() -> None: ...
    def getdata() -> None: ...
    def init() -> None: ...
    def is_ready() -> None: ...
    def read_byte() -> None: ...
    def read_bytes() -> None: ...
    def readfrom() -> None: ...
    def readfrom_into() -> None: ...
    def readfrom_mem() -> None: ...
    def readfrom_mem_into() -> None: ...
    def resetbusy() -> None: ...
    def scan() -> None: ...
    def setdata() -> None: ...
    def start() -> None: ...
    def start_timing() -> None: ...
    def stop() -> None: ...
    def stop_timing() -> None: ...
    def timeout() -> None: ...
    def write_byte() -> None: ...
    def write_bytes() -> None: ...
    def writeto() -> None: ...
    def writeto_mem() -> None: ...
class Pin:
    def init() -> None: ...
    def irqvalue() -> None: ...
    def value() -> None: ...
def const() -> None: ...
