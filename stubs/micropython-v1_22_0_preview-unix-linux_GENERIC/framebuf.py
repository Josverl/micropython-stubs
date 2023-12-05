"""
Module: 'framebuf' on micropython-v1.22.0.preview-unix-linux_[GCC_9.4.0]_version
"""
# MCU: {'family': 'micropython', 'version': '1.22.0.preview', 'build': '', 'ver': 'v1.22.0.preview', 'port': 'unix', 'board': 'linux_[GCC_9.4.0]_version', 'cpu': '', 'mpy': '', 'arch': ''}
# Stubber: v1.15.1
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
