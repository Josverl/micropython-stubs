"""
Module: 'ntptime' on micropython-v1.12-esp32
"""
# MCU: {'ver': 'v1.12', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.12.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.12.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.5.4
from typing import Any


def time(*args, **kwargs) -> Any:
    ...


NTP_DELTA = 3155673600  # type: int
host = "pool.ntp.org"  # type: str


def settime(*args, **kwargs) -> Any:
    ...
