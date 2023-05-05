"""
Module: 'neopixel' on micropython-v1.20.0-rp2-PICO
"""
# MCU: OrderedDict({'family': 'micropython', 'version': '1.20.0', 'build': '', 'ver': 'v1.20.0', 'port': 'rp2', 'board': 'PICO', 'cpu': 'RP2040', 'mpy': 'v6.1', 'arch': 'armv6m'})
# Stubber: v1.13.4
from typing import Any


def bitstream(*args, **kwargs) -> Any:
    ...


class NeoPixel:
    ORDER = ()  # type: tuple

    def write(self, *args, **kwargs) -> Any:
        ...

    def fill(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
