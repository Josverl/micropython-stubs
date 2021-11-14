"""
Module: 'ntptime' on micropython-esp32-1.17
"""
# MCU: {'ver': '1.17', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.17.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.17.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.4.2
from typing import Any

# import socket
# import struct
def time(*args) -> Any:
    ...

NTP_DELTA = 3155673600 # type: int
host = 'pool.ntp.org' # type: str
def settime(*args) -> Any:
    ...

