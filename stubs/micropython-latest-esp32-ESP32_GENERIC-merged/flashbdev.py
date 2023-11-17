"""
Module: 'flashbdev' on micropython-v1.21.0-esp32-Generic_ESP32_module_with_SPIRAM_with_ESP32
"""
# MCU: {'family': 'micropython', 'version': '1.21.0', 'build': '', 'ver': 'v1.21.0', 'port': 'esp32', 'board': 'Generic_ESP32_module_with_SPIRAM_with_ESP32', 'cpu': 'SPIRAM', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.14.0
from _typeshed import Incomplete

bdev: Incomplete  ## <class 'Partition'> = <Partition type=1, subtype=129, address=2097152, size=2097152, label=vfs, encrypted=0>


class Partition:
    RUNNING = 1  # type: int
    TYPE_APP = 0  # type: int
    TYPE_DATA = 1  # type: int
    BOOT = 0  # type: int

    def readblocks(self, *args, **kwargs) -> Incomplete:
        ...

    def ioctl(self, *args, **kwargs) -> Incomplete:
        ...

    def set_boot(self, *args, **kwargs) -> Incomplete:
        ...

    def writeblocks(self, *args, **kwargs) -> Incomplete:
        ...

    def info(self, *args, **kwargs) -> Incomplete:
        ...

    def find(self, *args, **kwargs) -> Incomplete:
        ...

    def get_next_update(self, *args, **kwargs) -> Incomplete:
        ...

    @classmethod
    def mark_app_valid_cancel_rollback(cls, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
