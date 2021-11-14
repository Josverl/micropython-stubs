"""
Module: 'select' on micropython-esp32-1.10
"""
# MCU: {'ver': '1.10', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module with ESP32', 'release': '1.10.0', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.10.0'}
# Stubber: 1.4.2
from typing import Any

POLLERR = 8 # type: int
POLLHUP = 16 # type: int
POLLIN = 1 # type: int
POLLOUT = 4 # type: int
def poll(*args) -> Any:
    ...

def select(*args) -> Any:
    ...

