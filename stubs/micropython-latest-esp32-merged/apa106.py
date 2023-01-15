"""
Module: 'apa106' on micropython-v1.19.1-esp32
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module (spiram) with ESP32', 'release': '1.19.1', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.19.1'}
# Stubber: 1.9.11
from typing import Any


class APA106:
    ORDER = ()  # type: tuple

    def write(self, *args, **kwargs) -> Any:
        ...

    def fill(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class NeoPixel:
    ORDER = ()  # type: tuple

    def write(self, *args, **kwargs) -> Any:
        ...

    def fill(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
