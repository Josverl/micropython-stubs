"""
Module: 'framebuf' on micropython-v1.18-stm32
"""
# MCU: {'ver': 'v1.18', 'port': 'stm32', 'arch': 'armv7emsp', 'sysname': 'pyboard', 'release': '1.18.0', 'name': 'micropython', 'mpy': 7685, 'version': '1.18.0', 'machine': 'PYBv1.1 with STM32F405RG', 'build': '', 'nodename': 'pyboard', 'platform': 'stm32', 'family': 'micropython'}
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
