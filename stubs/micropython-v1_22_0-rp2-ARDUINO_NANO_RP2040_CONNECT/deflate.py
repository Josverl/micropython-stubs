"""
Module: 'deflate' on micropython-v1.22.0-rp2-ARDUINO_NANO_RP2040_CONNECT
"""
# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'rp2', 'board': 'ARDUINO_NANO_RP2040_CONNECT', 'cpu': 'RP2040', 'mpy': 'v6.2', 'arch': 'armv6m'}
# Stubber: v1.16.2
from _typeshed import Incomplete

GZIP = 3  # type: int
RAW = 1  # type: int
ZLIB = 2  # type: int
AUTO = 0  # type: int


class DeflateIO:
    def readline(self, *args, **kwargs) -> Incomplete:
        ...

    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def read(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
