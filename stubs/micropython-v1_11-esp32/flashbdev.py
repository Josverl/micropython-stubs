"""
Module: 'flashbdev' on micropython-v1.11-esp32
"""
# MCU: {'ver': 'v1.11', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module with ESP32', 'release': '1.11.0', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.11.0'}
# Stubber: 1.5.4
from typing import Any

bdev: Any  ## <class 'FlashBdev'> = <FlashBdev object at 3f817800>
size = 4194304  # type: int


class FlashBdev:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def ioctl(self, *args, **kwargs) -> Any:
        ...

    def readblocks(self, *args, **kwargs) -> Any:
        ...

    def writeblocks(self, *args, **kwargs) -> Any:
        ...

    SEC_SIZE = 4096  # type: int
    START_SEC = 512  # type: int
