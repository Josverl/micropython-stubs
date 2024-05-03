"""
Module: 'ds18x20' on micropython-v1.20.0-rp2-PIMORONI_PICOLIPO_16MB
"""

# MCU: OrderedDict({'family': 'micropython', 'version': '1.20.0', 'build': '', 'ver': 'v1.20.0', 'port': 'rp2', 'board': 'PIMORONI_PICOLIPO_16MB', 'cpu': 'RP2040', 'mpy': 'v6.1', 'arch': 'armv6m'})
# Stubber: v1.13.7
from typing import Any


def const(*args, **kwargs) -> Any: ...


class DS18X20:
    def read_scratch(self, *args, **kwargs) -> Any: ...

    def write_scratch(self, *args, **kwargs) -> Any: ...

    def read_temp(self, *args, **kwargs) -> Any: ...

    def convert_temp(self, *args, **kwargs) -> Any: ...

    def scan(self, *args, **kwargs) -> Any: ...

    def __init__(self, *argv, **kwargs) -> None: ...
