"""
Module: 'select' on micropython-v1.26.0-esp8266-ESP8266_GENERIC
"""

# MCU: {'variant': '', 'build': '', 'arch': 'xtensa', 'port': 'esp8266', 'board': 'ESP8266_GENERIC', 'board_id': 'ESP8266_GENERIC', 'mpy': 'v6.3', 'ver': '1.26.0', 'family': 'micropython', 'cpu': 'ESP8266', 'version': '1.26.0'}
# Stubber: v1.25.1
from __future__ import annotations
from typing import Final
from _typeshed import Incomplete

POLLOUT: Final[int] = 4
POLLIN: Final[int] = 1
POLLHUP: Final[int] = 16
POLLERR: Final[int] = 8

def select(*args, **kwargs) -> Incomplete: ...
def poll(*args, **kwargs) -> Incomplete: ...
