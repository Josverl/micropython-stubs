"""
Module: 'ds18x20' on micropython-v1.19.1-esp32
"""

# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32S3 module with ESP32S3', 'release': '1.19.1', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.19.1'}
# Stubber: 1.11.2
from typing import Any


def const(*args, **kwargs) -> Any: ...


class DS18X20:
    def read_scratch(self, *args, **kwargs) -> Any: ...

    def write_scratch(self, *args, **kwargs) -> Any: ...

    def read_temp(self, *args, **kwargs) -> Any: ...

    def convert_temp(self, *args, **kwargs) -> Any: ...

    def scan(self, *args, **kwargs) -> Any: ...

    def __init__(self, *argv, **kwargs) -> None: ...
