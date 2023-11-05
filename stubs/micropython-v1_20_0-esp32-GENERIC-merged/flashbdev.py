"""
Module: 'flashbdev' on micropython-v1.20.0-esp32-GENERIC
"""
# MCU: OrderedDict({'family': 'micropython', 'version': '1.20.0', 'build': '', 'ver': 'v1.20.0', 'port': 'esp32', 'board': 'GENERIC', 'cpu': 'ESP32', 'mpy': 'v6.1', 'arch': 'xtensawin'})
# Stubber: v1.13.4
from typing import Any

bdev: Any  ## <class 'Partition'> = <Partition type=1, subtype=129, address=2097152, size=2097152, label=vfs, encrypted=0>


class Partition:
    RUNNING = 1  # type: int
    TYPE_APP = 0  # type: int
    TYPE_DATA = 1  # type: int
    BOOT = 0  # type: int

    def readblocks(self, *args, **kwargs) -> Any:
        ...

    def ioctl(self, *args, **kwargs) -> Any:
        ...

    def set_boot(self, *args, **kwargs) -> Any:
        ...

    def writeblocks(self, *args, **kwargs) -> Any:
        ...

    def info(self, *args, **kwargs) -> Any:
        ...

    def find(self, *args, **kwargs) -> Any:
        ...

    def get_next_update(self, *args, **kwargs) -> Any:
        ...

    @classmethod
    def mark_app_valid_cancel_rollback(cls, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
