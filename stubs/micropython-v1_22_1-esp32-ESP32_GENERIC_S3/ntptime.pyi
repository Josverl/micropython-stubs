"""
Module: 'ntptime' on micropython-v1.22.1-esp32-ESP32_GENERIC_S3
"""
# MCU: {'version': '1.22.1', 'mpy': 'v6.2', 'port': 'esp32', 'board': 'ESP32_GENERIC_S3', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': '1.22.1', 'cpu': 'ESP32S3'}
# Stubber: v1.17.3
from __future__ import annotations
from _typeshed import Incomplete

host: str = "pool.ntp.org"
timeout: int = 1

def settime(*args, **kwargs) -> Incomplete: ...
def time(*args, **kwargs) -> Incomplete: ...
