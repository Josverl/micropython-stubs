"""
Module: 'select' on micropython-v1.20.0-samd-ADAFRUIT_ITSYBITSY_M4_EXPRESS
"""
# MCU: OrderedDict({'build': '', 'ver': 'v1.20.0', 'version': '1.20.0', 'port': 'samd', 'board': 'ADAFRUIT_ITSYBITSY_M4_EXPRESS', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'SAMD51G19A', 'arch': 'armv7emsp'})
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
