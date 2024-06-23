"""
Module: 'ntptime' on micropython-v1.21.0-esp32-ESP32_GENERIC_S3
"""

# MCU: {'version': '1.21.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'ESP32_GENERIC_S3', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': '1.21.0', 'cpu': 'ESP32S3'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete

timeout: int = 1
host: str = "pool.ntp.org"

def settime(*args, **kwargs) -> Incomplete: ...
def time(*args, **kwargs) -> Incomplete: ...
