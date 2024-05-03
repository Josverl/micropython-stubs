"""
Module: 'ds18x20' on micropython-v1.20.0-esp32-GENERIC_S3
"""

# MCU: OrderedDict({'version': '1.20.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'GENERIC_S3', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': 'v1.20.0', 'cpu': 'ESP32S3'})
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
