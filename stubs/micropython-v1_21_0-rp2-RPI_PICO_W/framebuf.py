"""
Module: 'framebuf' on micropython-v1.21.0-rp2-RPI_PICO_W
"""
# MCU: {'build': '', 'ver': 'v1.21.0', 'version': '1.21.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.13.8
from typing import Any
from _typeshed import Incomplete

MONO_HMSB = 4  # type: int
MONO_HLSB = 3  # type: int
RGB565 = 1  # type: int
MONO_VLSB = 0  # type: int
MVLSB = 0  # type: int
GS2_HMSB = 5  # type: int
GS8 = 6  # type: int
GS4_HMSB = 2  # type: int


def FrameBuffer1(*args, **kwargs) -> Incomplete:
    ...


class FrameBuffer:
    def poly(self, *args, **kwargs) -> Incomplete:
        ...

    def vline(self, *args, **kwargs) -> Incomplete:
        ...

    def pixel(self, *args, **kwargs) -> Incomplete:
        ...

    def text(self, *args, **kwargs) -> Incomplete:
        ...

    def rect(self, *args, **kwargs) -> Incomplete:
        ...

    def scroll(self, *args, **kwargs) -> Incomplete:
        ...

    def ellipse(self, *args, **kwargs) -> Incomplete:
        ...

    def line(self, *args, **kwargs) -> Incomplete:
        ...

    def blit(self, *args, **kwargs) -> Incomplete:
        ...

    def hline(self, *args, **kwargs) -> Incomplete:
        ...

    def fill(self, *args, **kwargs) -> Incomplete:
        ...

    def fill_rect(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
