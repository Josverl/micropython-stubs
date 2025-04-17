"""
Module: 'select' on micropython-v1.25.0-esp32-ESP32_GENERIC_S2
"""

# MCU: {'version': '1.25.0', 'mpy': 'v6.3', 'port': 'esp32', 'board': 'ESP32_GENERIC_S2', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': '1.25.0', 'cpu': 'ESP32S2'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Final
from _typeshed import Incomplete

POLLOUT: Final[int] = 4
POLLIN: Final[int] = 1
POLLHUP: Final[int] = 16
POLLERR: Final[int] = 8

def select(*args, **kwargs) -> Incomplete: ...
def poll(*args, **kwargs) -> Incomplete: ...
