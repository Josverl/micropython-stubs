"""
Module: 'select' on micropython-v1.20.0-449-esp32-Generic_ESP32_module_with_SPIRAM_with_ESP32
"""
# MCU: OrderedDict({'version': '1.20.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'Generic_ESP32_module_with_SPIRAM_with_ESP32', 'family': 'micropython', 'build': '449', 'arch': 'xtensawin', 'ver': 'v1.20.0-449', 'cpu': 'SPIRAM'})
# Stubber: v1.13.7
from typing import Any

POLLOUT = 4  # type: int
POLLIN = 1  # type: int
POLLHUP = 16  # type: int
POLLERR = 8  # type: int


def select(*args, **kwargs) -> Any:
    ...


def poll(*args, **kwargs) -> Any:
    ...
