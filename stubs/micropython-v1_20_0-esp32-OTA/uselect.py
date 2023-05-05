"""
Module: 'uselect' on micropython-v1.20.0-esp32-GENERIC_OTA
"""
# MCU: OrderedDict({'family': 'micropython', 'version': '1.20.0', 'build': '', 'ver': 'v1.20.0', 'port': 'esp32', 'board': 'GENERIC_OTA', 'cpu': 'ESP32', 'mpy': 'v6.1', 'arch': 'xtensawin'})
# Stubber: v1.13.4
from typing import Any

POLLOUT = 4  # type: int
POLLIN = 1  # type: int
POLLHUP = 16  # type: int
POLLERR = 8  # type: int


def select(*args, **kwargs) -> Any:
    ...


def poll(*args, **kwargs) -> Any:
    ...
