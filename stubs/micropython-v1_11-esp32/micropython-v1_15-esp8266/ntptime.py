"""
Module: 'ntptime' on micropython-v1.15-esp8266
"""
# MCU: {'ver': 'v1.15', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '1.15', 'name': 'micropython', 'mpy': 9733, 'version': '1.15', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
# Stubber: 1.5.0
from typing import Any


def time(*args) -> Any:
    ...


NTP_DELTA = 3155673600  # type: int
host = "pool.ntp.org"  # type: str


def settime(*args) -> Any:
    ...
