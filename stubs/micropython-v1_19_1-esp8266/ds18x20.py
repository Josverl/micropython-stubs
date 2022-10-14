"""
Module: 'ds18x20' on micropython-v1.19.1-esp8266
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp8266', 'port': 'esp8266', 'machine': 'ESP module (1M) with ESP8266', 'release': '1.19.1', 'nodename': 'esp8266', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp8266', 'version': '1.19.1'}
# Stubber: 1.9.11
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
