"""
Module: 'ntptime' on micropython-v1.23.0-preview-rp2-RPI_PICO_W
"""
# MCU: {'family': 'micropython', 'version': '1.23.0-preview', 'build': 'preview.58.gc3ca3612d', 'ver': '1.23.0-preview-preview.58.gc3ca3612d', 'port': 'rp2', 'board': 'RPI_PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.2', 'arch': 'armv6m'}
# Stubber: v1.17.1
from __future__ import annotations
from _typeshed import Incomplete

host: str = "pool.ntp.org"
timeout: int = 1

def settime(*args, **kwargs) -> Incomplete: ...
def time(*args, **kwargs) -> Incomplete: ...
