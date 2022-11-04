"""
Module: 'flashbdev' on micropython-v1.18-esp32
"""
# MCU: {'ver': 'v1.18', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.18.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.18.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.5.4
from typing import Any


class Partition:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def find(self, *args, **kwargs) -> Any:
        ...

    BOOT = 0  # type: int
    RUNNING = 1  # type: int
    TYPE_APP = 0  # type: int
    TYPE_DATA = 1  # type: int

    def get_next_update(self, *args, **kwargs) -> Any:
        ...

    def info(self, *args, **kwargs) -> Any:
        ...

    def ioctl(self, *args, **kwargs) -> Any:
        ...

    @classmethod
    def mark_app_valid_cancel_rollback(cls, *args, **kwargs) -> Any:
        ...

    def readblocks(self, *args, **kwargs) -> Any:
        ...

    def set_boot(self, *args, **kwargs) -> Any:
        ...

    def writeblocks(self, *args, **kwargs) -> Any:
        ...


bdev: Any  ## <class 'Partition'> = <Partition type=1, subtype=129, address=2097152, size=2097152, label=vfs, encrypted=0>
