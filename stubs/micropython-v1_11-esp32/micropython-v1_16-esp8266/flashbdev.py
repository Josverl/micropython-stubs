"""
Module: 'flashbdev' on micropython-v1.16-esp8266
"""
# MCU: {'ver': 'v1.16', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '1.16', 'name': 'micropython', 'mpy': 9733, 'version': '1.16', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
# Stubber: 1.5.0
from typing import Any

bdev: Any  ## <class 'FlashBdev'> = <FlashBdev object at 3ffeef50>
start_sec = 256  # type: int


class FlashBdev:
    """"""

    def __init__(self, *args) -> None:
        ...

    def ioctl(self, *args) -> Any:
        ...

    def readblocks(self, *args) -> Any:
        ...

    def writeblocks(self, *args) -> Any:
        ...

    SEC_SIZE = 4096  # type: int


size = 4194304  # type: int
