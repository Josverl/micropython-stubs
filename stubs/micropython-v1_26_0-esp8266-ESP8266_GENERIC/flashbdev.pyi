"""
Module: 'flashbdev' on micropython-v1.26.0-esp8266-ESP8266_GENERIC
"""

# MCU: {'variant': '', 'build': '', 'arch': 'xtensa', 'port': 'esp8266', 'board': 'ESP8266_GENERIC', 'board_id': 'ESP8266_GENERIC', 'mpy': 'v6.3', 'ver': '1.26.0', 'family': 'micropython', 'cpu': 'ESP8266', 'version': '1.26.0'}
# Stubber: v1.26.0
from __future__ import annotations
from typing import Final
from _typeshed import Incomplete

start_sec: int = 256
size: int = 4194304

class FlashBdev:
    SEC_SIZE: Final[int] = 4096
    def writeblocks(self, *args, **kwargs) -> Incomplete: ...
    def ioctl(self, *args, **kwargs) -> Incomplete: ...
    def readblocks(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

bdev: Incomplete  ## <class 'FlashBdev'> = <FlashBdev object at ...>
