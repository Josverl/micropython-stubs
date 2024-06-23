"""
Module: 'ntptime' on micropython-v1.24.0-preview-esp32-ESP32_GENERIC
"""

# MCU: {'version': '1.24.0-preview', 'mpy': 'v6.3', 'port': 'esp32', 'board': 'ESP32_GENERIC', 'family': 'micropython', 'build': 'preview.60.gcebc9b0ae', 'arch': 'xtensawin', 'ver': '1.24.0-preview-preview.60.gcebc9b0ae', 'cpu': 'ESP32'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete

host: str = "pool.ntp.org"
timeout: int = 1

def settime(*args, **kwargs) -> Incomplete: ...
def time(*args, **kwargs) -> Incomplete: ...
