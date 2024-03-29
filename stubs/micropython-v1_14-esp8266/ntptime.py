"""
Module: 'ntptime' on micropython-v1.14-esp8266
"""
# MCU: {'ver': 'v1.14', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '1.14', 'name': 'micropython', 'mpy': 9733, 'version': '1.14', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
# Stubber: 1.5.4
from typing import Any


def time(*args, **kwargs) -> Any:
    ...


NTP_DELTA = 3155673600  # type: int
host = "pool.ntp.org"  # type: str


def settime(*args, **kwargs) -> Any:
    ...
