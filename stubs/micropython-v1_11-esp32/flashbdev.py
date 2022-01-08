"""
Module: 'flashbdev' on micropython-v1.11-esp32
"""
# MCU: {'ver': 'v1.11', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module with ESP32', 'release': '1.11.0', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.11.0'}
# Stubber: 1.5.0
from typing import Any

bdev: Any  ## <class 'FlashBdev'> = <FlashBdev object at 3f817800>
size = 4194304  # type: int


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
    START_SEC = 512  # type: int
