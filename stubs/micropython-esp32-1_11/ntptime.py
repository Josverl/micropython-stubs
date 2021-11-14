"""
Module: 'ntptime' on micropython-esp32-1.11
"""
# MCU: {'ver': '1.11', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module with ESP32', 'release': '1.11.0', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.11.0'}
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

