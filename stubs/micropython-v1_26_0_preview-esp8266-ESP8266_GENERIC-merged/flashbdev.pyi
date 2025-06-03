"""
Module: 'flashbdev' on micropython-v1.25.0-esp8266-ESP8266_GENERIC-FLASH_2M_ROMFS
"""

# MCU: {'variant': 'FLASH_2M_ROMFS', 'build': '', 'arch': 'xtensa', 'port': 'esp8266', 'board': 'ESP8266_GENERIC', 'board_id': 'ESP8266_GENERIC-FLASH_2M_ROMFS', 'mpy': 'v6.3', 'ver': '1.25.0', 'family': 'micropython', 'cpu': 'ESP8266', 'version': '1.25.0'}
# Stubber: v1.25.0
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
