"""
Module: 'framebuf' on micropython-v1.20.0-449-esp32-Generic_ESP32_module_with_SPIRAM_with_ESP32
"""
# MCU: OrderedDict({'version': '1.20.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'Generic_ESP32_module_with_SPIRAM_with_ESP32', 'family': 'micropython', 'build': '449', 'arch': 'xtensawin', 'ver': 'v1.20.0-449', 'cpu': 'SPIRAM'})
# Stubber: v1.13.7
from typing import Any

MONO_HMSB = 4  # type: int
MONO_HLSB = 3  # type: int
RGB565 = 1  # type: int
MONO_VLSB = 0  # type: int
MVLSB = 0  # type: int
GS2_HMSB = 5  # type: int
GS8 = 6  # type: int
GS4_HMSB = 2  # type: int


def FrameBuffer1(*args, **kwargs) -> Any:
    ...


class FrameBuffer:
    def poly(self, *args, **kwargs) -> Any:
        ...

    def vline(self, *args, **kwargs) -> Any:
        ...

    def pixel(self, *args, **kwargs) -> Any:
        ...

    def text(self, *args, **kwargs) -> Any:
        ...

    def rect(self, *args, **kwargs) -> Any:
        ...

    def scroll(self, *args, **kwargs) -> Any:
        ...

    def ellipse(self, *args, **kwargs) -> Any:
        ...

    def line(self, *args, **kwargs) -> Any:
        ...

    def blit(self, *args, **kwargs) -> Any:
        ...

    def hline(self, *args, **kwargs) -> Any:
        ...

    def fill(self, *args, **kwargs) -> Any:
        ...

    def fill_rect(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
