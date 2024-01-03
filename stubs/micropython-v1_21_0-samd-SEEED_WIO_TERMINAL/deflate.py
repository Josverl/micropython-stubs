"""
Module: 'deflate' on micropython-v1.21.0-samd-SEEED_WIO_TERMINAL
"""
# MCU: {'family': 'micropython', 'version': '1.21.0', 'build': '', 'ver': 'v1.21.0', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'cpu': 'SAMD51P19A', 'mpy': 'v6.1', 'arch': 'armv7emsp'}
# Stubber: v1.16.2
from _typeshed import Incomplete

GZIP = 3  # type: int
RAW = 1  # type: int
ZLIB = 2  # type: int
AUTO = 0  # type: int


class DeflateIO:
    def readinto(self, *args, **kwargs) -> Incomplete:
        ...

    def readline(self, *args, **kwargs) -> Incomplete:
        ...

    def write(self, *args, **kwargs) -> Incomplete:
        ...

    def read(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
