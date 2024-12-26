"""
Module: 'ntptime' on micropython-v1.24.1-rp2-RPI_PICO_W
"""

# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'rp2', 'board': 'RPI_PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.3', 'arch': 'armv6m'}
# Stubber: v1.24.0
from __future__ import annotations
from _typeshed import Incomplete

timeout: int = 1
host: str = "pool.ntp.org"

def time(*args, **kwargs) -> Incomplete: ...
def settime(*args, **kwargs) -> Incomplete: ...
def gmtime(*args, **kwargs) -> Incomplete: ...
