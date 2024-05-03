"""
Module: 'flashbdev' on micropython-v1.20.0-esp32-GENERIC_S3
"""

# MCU: OrderedDict({'version': '1.20.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'GENERIC_S3', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': 'v1.20.0', 'cpu': 'ESP32S3'})
# Stubber: v1.13.7
from typing import Any

bdev: Any  ## <class 'Partition'> = <Partition type=1, subtype=129, address=2097152, size=6291456, label=vfs, encrypted=0>


class Partition:
    RUNNING = 1  # type: int
    TYPE_APP = 0  # type: int
    TYPE_DATA = 1  # type: int
    BOOT = 0  # type: int

    def readblocks(self, *args, **kwargs) -> Any: ...

    def ioctl(self, *args, **kwargs) -> Any: ...

    def set_boot(self, *args, **kwargs) -> Any: ...

    def writeblocks(self, *args, **kwargs) -> Any: ...

    def info(self, *args, **kwargs) -> Any: ...

    def find(self, *args, **kwargs) -> Any: ...

    def get_next_update(self, *args, **kwargs) -> Any: ...

    @classmethod
    def mark_app_valid_cancel_rollback(cls, *args, **kwargs) -> Any: ...

    def __init__(self, *argv, **kwargs) -> None: ...
