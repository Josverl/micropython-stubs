"""
Module: 'neopixel' on micropython-v1.20-rp2-PICO_W
"""
# MCU: OrderedDict({'family': 'micropython', 'version': '1.20', 'build': '', 'ver': 'v1.20', 'port': 'rp2', 'board': 'PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.1', 'arch': 'armv6m'})
# Stubber: v1.12.2
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
