"""
Module: 'flashbdev' on micropython-v1.23.0-esp8266-ESP8266_GENERIC
"""

# MCU: {'version': '1.23.0', 'mpy': 'v6.3', 'port': 'esp8266', 'board': 'ESP8266_GENERIC', 'family': 'micropython', 'build': '', 'arch': 'xtensa', 'ver': '1.23.0', 'cpu': 'ESP8266'}
# Stubber: v1.23.0
from __future__ import annotations
from _typeshed import Incomplete

start_sec: int = 256
size: int = 4194304

class FlashBdev:
    SEC_SIZE: int = 4096
    def writeblocks(self, *args, **kwargs) -> Incomplete: ...
    def ioctl(self, *args, **kwargs) -> Incomplete: ...
    def readblocks(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

bdev: Incomplete  ## <class 'FlashBdev'> = <FlashBdev object at ...>
