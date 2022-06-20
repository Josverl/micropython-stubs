"""
Module: 'framebuf' on micropython-v1.19.1-esp32
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module (spiram) with ESP32', 'release': '1.19.1', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.19.1'}
# Stubber: 1.5.6
from typing import Any


class FrameBuffer:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def blit(self, *args, **kwargs) -> Any:
        ...

    def fill(self, *args, **kwargs) -> Any:
        ...

    def fill_rect(self, *args, **kwargs) -> Any:
        ...

    def hline(self, *args, **kwargs) -> Any:
        ...

    def line(self, *args, **kwargs) -> Any:
        ...

    def pixel(self, *args, **kwargs) -> Any:
        ...

    def rect(self, *args, **kwargs) -> Any:
        ...

    def scroll(self, *args, **kwargs) -> Any:
        ...

    def text(self, *args, **kwargs) -> Any:
        ...

    def vline(self, *args, **kwargs) -> Any:
        ...


def FrameBuffer1(*args, **kwargs) -> Any:
    ...


GS2_HMSB = 5  # type: int
GS4_HMSB = 2  # type: int
GS8 = 6  # type: int
MONO_HLSB = 3  # type: int
MONO_HMSB = 4  # type: int
MONO_VLSB = 0  # type: int
MVLSB = 0  # type: int
RGB565 = 1  # type: int
