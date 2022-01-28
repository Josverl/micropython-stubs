"""
Module: 'uselect' on micropython-v1.13-266-esp32
"""
# MCU: {'ver': 'v1.13-266', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.13.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.13.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '266', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.5.3
from typing import Any

POLLERR = 8  # type: int
POLLHUP = 16  # type: int
POLLIN = 1  # type: int
POLLOUT = 4  # type: int


def poll(*args, **kwargs) -> Any:
    ...


def select(*args, **kwargs) -> Any:
    ...