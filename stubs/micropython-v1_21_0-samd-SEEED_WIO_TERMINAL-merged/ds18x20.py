"""
Module: 'ds18x20' on micropython-v1.21.0-samd-SEEED_WIO_TERMINAL
"""

# MCU: {'family': 'micropython', 'version': '1.21.0', 'build': '', 'ver': 'v1.21.0', 'port': 'samd', 'board': 'SEEED_WIO_TERMINAL', 'cpu': 'SAMD51P19A', 'mpy': 'v6.1', 'arch': 'armv7emsp'}
# Stubber: v1.16.2
from _typeshed import Incomplete


def const(*args, **kwargs) -> Incomplete: ...


class DS18X20:
    def read_scratch(self, *args, **kwargs) -> Incomplete: ...

    def write_scratch(self, *args, **kwargs) -> Incomplete: ...

    def read_temp(self, *args, **kwargs) -> Incomplete: ...

    def convert_temp(self, *args, **kwargs) -> Incomplete: ...

    def scan(self, *args, **kwargs) -> Incomplete: ...

    def __init__(self, *argv, **kwargs) -> None: ...
