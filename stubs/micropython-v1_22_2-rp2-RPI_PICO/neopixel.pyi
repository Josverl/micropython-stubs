"""
Module: 'neopixel' on micropython-v1.22.2-rp2-RPI_PICO
"""

# MCU: {'build': '', 'ver': '1.22.2', 'version': '1.22.2', 'port': 'rp2', 'board': 'RPI_PICO', 'mpy': 'v6.2', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete

def bitstream(*args, **kwargs) -> Incomplete: ...

class NeoPixel:
    ORDER: tuple = ()
    def write(self, *args, **kwargs) -> Incomplete: ...
    def fill(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
