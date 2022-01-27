"""
Module: 'select' on micropython-v1.18-esp8266
"""
# MCU: {'ver': 'v1.18', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '1.18', 'name': 'micropython', 'mpy': 9733, 'version': '1.18', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
# Stubber: 1.5.3
from typing import Any

POLLERR = 8 # type: int
POLLHUP = 16 # type: int
POLLIN = 1 # type: int
POLLOUT = 4 # type: int
def poll(*args) -> Any:
    ...

def select(*args) -> Any:
    ...

