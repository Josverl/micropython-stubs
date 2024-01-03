"""
Module: 'framebuf' on micropython-v1.22.0-esp32-Generic_ESP32S3_module
"""
# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'esp32', 'board': 'Generic_ESP32S3_module', 'cpu': 'ESP32S3', 'mpy': 'v6.2', 'arch': 'xtensawin'}
# Stubber: v1.16.2
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
