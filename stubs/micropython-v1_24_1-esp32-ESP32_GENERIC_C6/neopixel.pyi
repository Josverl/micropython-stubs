"""
Module: 'neopixel' on micropython-v1.24.1-esp32-ESP32_GENERIC_C6
"""

# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'esp32', 'board': 'ESP32_GENERIC_C6', 'cpu': 'ESP32C6', 'mpy': 'v6.3', 'arch': 'rv32imc'}
# Stubber: v1.24.0
from __future__ import annotations
from _typeshed import Incomplete

def bitstream(*args, **kwargs) -> Incomplete: ...

class NeoPixel:
    ORDER: tuple = ()
    def write(self, *args, **kwargs) -> Incomplete: ...
    def fill(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
