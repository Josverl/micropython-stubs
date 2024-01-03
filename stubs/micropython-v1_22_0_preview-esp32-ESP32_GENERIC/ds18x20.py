"""
Module: 'ds18x20' on micropython-v1.22.0.preview-esp32-ESP32_GENERIC
"""
# MCU: {'family': 'micropython', 'version': '1.22.0.preview', 'build': '', 'ver': 'v1.22.0.preview', 'port': 'esp32', 'board': 'ESP32_GENERIC', 'cpu': 'ESP32', 'mpy': 'v6.2', 'arch': 'xtensawin'}
# Stubber: v1.16.2
from _typeshed import Incomplete


def const(*args, **kwargs) -> Incomplete:
    ...


class DS18X20:
    def read_scratch(self, *args, **kwargs) -> Incomplete:
        ...

    def read_temp(self, *args, **kwargs) -> Incomplete:
        ...

    def write_scratch(self, *args, **kwargs) -> Incomplete:
        ...

    def convert_temp(self, *args, **kwargs) -> Incomplete:
        ...

    def scan(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
