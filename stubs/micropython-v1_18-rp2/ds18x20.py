"""
Module: 'ds18x20' on micropython-v1.18-rp2
"""
# MCU: {'family': 'micropython', 'sysname': 'rp2', 'version': '1.18.0', 'build': '', 'mpy': 5637, 'port': 'rp2', 'platform': 'rp2', 'name': 'micropython', 'arch': 'armv7m', 'machine': 'Arduino Nano RP2040 Connect with RP2040', 'nodename': 'rp2', 'ver': 'v1.18', 'release': '1.18.0'}
# Stubber: 1.5.3
from typing import Any

def const(*args, **kwargs) -> Any:
    ...


class DS18X20():
    ''
    def __init__(self, *argv, **kwargs) -> None:
        ''
        ...
    def scan(self, *args, **kwargs) -> Any:
        ...

    def convert_temp(self, *args, **kwargs) -> Any:
        ...

    def read_scratch(self, *args, **kwargs) -> Any:
        ...

    def write_scratch(self, *args, **kwargs) -> Any:
        ...

    def read_temp(self, *args, **kwargs) -> Any:
        ...

