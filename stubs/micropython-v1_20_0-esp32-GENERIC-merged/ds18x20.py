"""
Module: 'ds18x20' on micropython-v1.20.0-esp32-GENERIC
"""
# MCU: OrderedDict({'family': 'micropython', 'version': '1.20.0', 'build': '', 'ver': 'v1.20.0', 'port': 'esp32', 'board': 'GENERIC', 'cpu': 'ESP32', 'mpy': 'v6.1', 'arch': 'xtensawin'})
# Stubber: v1.13.4
from typing import Any


def const(*args, **kwargs) -> Any:
    ...


class DS18X20:
    def read_scratch(self, *args, **kwargs) -> Any:
        ...

    def write_scratch(self, *args, **kwargs) -> Any:
        ...

    def read_temp(self, *args, **kwargs) -> Any:
        ...

    def convert_temp(self, *args, **kwargs) -> Any:
        ...

    def scan(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
