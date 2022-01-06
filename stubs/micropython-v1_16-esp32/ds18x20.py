"""
Module: 'ds18x20' on micropython-v1.16-esp32
"""
# MCU: {'ver': 'v1.16', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.16.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.16.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
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
