"""
Module: 'neopixel' on micropython-v1.27.0-esp32-ESP32_GENERIC_C3
"""

# MCU: {'variant': '', 'build': '', 'arch': 'rv32imc', 'port': 'esp32', 'board': 'ESP32_GENERIC_C3', 'board_id': 'ESP32_GENERIC_C3', 'mpy': 'v6.3', 'ver': '1.27.0', 'family': 'micropython', 'cpu': 'ESP32C3', 'version': '1.27.0'}
# Stubber: v1.26.4
from __future__ import annotations
from _typeshed import Incomplete

def bitstream(*args, **kwargs) -> Incomplete: ...

class NeoPixel:
    ORDER: tuple = ()
    def write(self, *args, **kwargs) -> Incomplete: ...
    def fill(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
