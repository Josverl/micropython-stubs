"""
Module: 'framebuf' on micropython-v1.17-rp2
"""
# MCU: {'family': 'micropython', 'sysname': 'rp2', 'version': '1.17.0', 'build': '', 'mpy': 5637, 'port': 'rp2', 'platform': 'rp2', 'name': 'micropython', 'arch': 'armv7m', 'machine': 'Raspberry Pi Pico with RP2040', 'nodename': 'rp2', 'ver': 'v1.17', 'release': '1.17.0'}
# Stubber: 1.5.2
from typing import Any


class FrameBuffer:
    """"""

    def blit(self, *args) -> Any:
        ...

    def fill(self, *args) -> Any:
        ...

    def fill_rect(self, *args) -> Any:
        ...

    def hline(self, *args) -> Any:
        ...

    def line(self, *args) -> Any:
        ...

    def pixel(self, *args) -> Any:
        ...

    def rect(self, *args) -> Any:
        ...

    def scroll(self, *args) -> Any:
        ...

    def text(self, *args) -> Any:
        ...

    def vline(self, *args) -> Any:
        ...


def FrameBuffer1(*args) -> Any:
    ...


GS2_HMSB = 5  # type: int
GS4_HMSB = 2  # type: int
GS8 = 6  # type: int
MONO_HLSB = 3  # type: int
MONO_HMSB = 4  # type: int
MONO_VLSB = 0  # type: int
MVLSB = 0  # type: int
RGB565 = 1  # type: int
