from typing import Any

Node = Any

class AK8963:
    def _register_char() -> None: ...
    def _register_short() -> None: ...
    def _register_three_shorts() -> None: ...

class I2C:
    def address() -> None: ...
    def begin() -> None: ...
    def callback() -> None: ...
    def deinit() -> None: ...
    def end() -> None: ...
    def getdata() -> None: ...
    def init() -> None: ...
    def read_byte() -> None: ...
    def read_bytes() -> None: ...
    def readfrom() -> None: ...
    def readfrom_into() -> None: ...
    def readfrom_mem() -> None: ...
    def readfrom_mem_into() -> None: ...
    def scan() -> None: ...
    def setdata() -> None: ...
    def slavewrite() -> None: ...
    def start() -> None: ...
    def stop() -> None: ...
    def write_byte() -> None: ...
    def write_bytes() -> None: ...
    def writeto() -> None: ...
    def writeto_mem() -> None: ...

class Pin:
    def init() -> None: ...
    def irq() -> None: ...
    def value() -> None: ...

def const() -> None: ...
