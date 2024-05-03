"""
Module: 'apa106' on micropython-v1.20.0-esp32-GENERIC_S3
"""

# MCU: OrderedDict({'version': '1.20.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'GENERIC_S3', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': 'v1.20.0', 'cpu': 'ESP32S3'})
# Stubber: v1.13.7
from typing import Any


class APA106:
    ORDER = ()  # type: tuple

    def write(self, *args, **kwargs) -> Any: ...

    def fill(self, *args, **kwargs) -> Any: ...

    def __init__(self, *argv, **kwargs) -> None: ...


class NeoPixel:
    ORDER = ()  # type: tuple

    def write(self, *args, **kwargs) -> Any: ...

    def fill(self, *args, **kwargs) -> Any: ...

    def __init__(self, *argv, **kwargs) -> None: ...
