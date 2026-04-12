"""
Module: 'ntptime' on micropython-v1.28.0-esp32-ESP32_GENERIC_S3
"""

# MCU: {'variant': '', 'build': '', 'arch': 'xtensawin', 'port': 'esp32', 'board': 'ESP32_GENERIC_S3', 'board_id': 'ESP32_GENERIC_S3', 'mpy': 'v6.3', 'ver': '1.28.0', 'family': 'micropython', 'cpu': 'ESP32S3', 'version': '1.28.0'}
# Stubber: v1.28.0
from __future__ import annotations
from _typeshed import Incomplete

timeout: int = 1
host: str = "pool.ntp.org"

def time() -> Incomplete: ...
def settime() -> Incomplete: ...
def gmtime(*args, **kwargs) -> Incomplete: ...
