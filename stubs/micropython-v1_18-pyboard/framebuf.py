"""
Module: 'framebuf' on micropython-v1.18-pyboard
"""
# MCU: {'ver': 'v1.18', 'port': 'pyboard', 'arch': 'armv7emsp', 'sysname': 'pyboard', 'release': '1.18.0', 'name': 'micropython', 'mpy': 7685, 'version': '1.18.0', 'machine': 'PYBv1.1 with STM32F405RG', 'build': '', 'nodename': 'pyboard', 'platform': 'pyboard', 'family': 'micropython'}
# Stubber: 1.5.2
from typing import Any


class FrameBuffer:
    """"""

    def __init__(self, *argv) -> None:
        """"""
        ...

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
