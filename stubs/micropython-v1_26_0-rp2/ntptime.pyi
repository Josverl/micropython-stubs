"""
Module: 'ntptime' on micropython-v1.26.0-rp2
"""

# MCU: {'family': 'micropython', 'version': '1.26.0', 'build': '', 'ver': '1.26.0', 'port': 'rp2', 'board': '', 'cpu': 'RP2040', 'mpy': 'v6.3', 'arch': 'armv6m'}
# Stubber: v1.24.0
from __future__ import annotations
from _typeshed import Incomplete

timeout: int = 1
host: str = "pool.ntp.org"

def time(*args, **kwargs) -> Incomplete: ...
def settime(*args, **kwargs) -> Incomplete: ...
def gmtime(*args, **kwargs) -> Incomplete: ...
