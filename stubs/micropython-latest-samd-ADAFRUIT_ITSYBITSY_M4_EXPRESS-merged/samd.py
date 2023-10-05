"""
Module: 'samd' on micropython-v1.20.0-samd-ADAFRUIT_ITSYBITSY_M4_EXPRESS
"""
# MCU: OrderedDict({'build': '', 'ver': 'v1.20.0', 'version': '1.20.0', 'port': 'samd', 'board': 'ADAFRUIT_ITSYBITSY_M4_EXPRESS', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'SAMD51G19A', 'arch': 'armv7emsp'})
# Stubber: v1.13.7
from typing import Any


def pininfo(*args, **kwargs) -> Any:
    ...


class Flash:
    def ioctl(self, *args, **kwargs) -> Any:
        ...

    def writeblocks(self, *args, **kwargs) -> Any:
        ...

    def readblocks(self, *args, **kwargs) -> Any:
        ...

    def flash_init(self, *args, **kwargs) -> Any:
        ...

    def flash_version(self, *args, **kwargs) -> Any:
        ...

    def flash_size(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
