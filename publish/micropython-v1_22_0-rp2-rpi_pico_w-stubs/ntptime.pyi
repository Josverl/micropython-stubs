"""
Module: 'ntptime' on micropython-v1.22.0-rp2-RPI_PICO_W
"""

# MCU: {'build': '', 'ver': '1.22.0', 'version': '1.22.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.2', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.16.3
from __future__ import annotations
from _typeshed import Incomplete

host: str = "pool.ntp.org"
timeout: int = 1

def settime(*args, **kwargs) -> Incomplete: ...
def time(*args, **kwargs) -> Incomplete: ...
