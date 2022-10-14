"""
Module: 'uselect' on micropython-v1.19.1-esp8266
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp8266', 'port': 'esp8266', 'machine': 'ESP module (1M) with ESP8266', 'release': '1.19.1', 'nodename': 'esp8266', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp8266', 'version': '1.19.1'}
# Stubber: 1.9.11
from typing import Any

POLLOUT = 4  # type: int
POLLIN = 1  # type: int
POLLHUP = 16  # type: int
POLLERR = 8  # type: int


def select(*args, **kwargs) -> Any:
    ...


def poll(*args, **kwargs) -> Any:
    ...
