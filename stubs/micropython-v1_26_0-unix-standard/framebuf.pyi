"""
Module: 'framebuf' on micropython-v1.26.0-unix-standard
"""
# MCU: {'family': 'micropython', 'version': '1.26.0', 'build': '', 'ver': '1.26.0', 'port': 'unix', 'board': 'standard', 'board_id': 'standard', 'variant': '', 'cpu': 'linux [GCC 12.4.0] version', 'mpy': 'v6.3', 'arch': 'x64'}
# Stubber: v1.26.2
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

MONO_HMSB: Final[int] = 4
MONO_HLSB: Final[int] = 3
RGB565: Final[int] = 1
MONO_VLSB: Final[int] = 0
MVLSB: Final[int] = 0
GS2_HMSB: Final[int] = 5
GS8: Final[int] = 6
GS4_HMSB: Final[int] = 2
def FrameBuffer1(*args, **kwargs) -> Incomplete:
    ...


class FrameBuffer():
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

