"""
Module: 'ds18x20' on micropython-v1.11-esp32
"""
# MCU: {'ver': 'v1.11', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module with ESP32', 'release': '1.11.0', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.11.0'}
# Stubber: 1.5.0
from typing import Any


def const(*args) -> Any:
    ...


class DS18X20:
    """"""

    def __init__(self, *args) -> None:
        ...

    def scan(self, *args) -> Any:
        ...

    def convert_temp(self, *args) -> Any:
        ...

    def read_scratch(self, *args) -> Any:
        ...

    def write_scratch(self, *args) -> Any:
        ...

    def read_temp(self, *args) -> Any:
        ...
