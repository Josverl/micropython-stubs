"""
Module: 'framebuf' on micropython-v1.25.0-preview-rp2-UNKNOWN_BOARD
"""

# MCU: {'family': 'micropython', 'version': '1.25.0-preview', 'build': 'preview.236.gbfb1bee6f', 'ver': '1.25.0-preview-preview.236.gbfb1bee6f', 'port': 'rp2', 'board': 'UNKNOWN_BOARD', 'cpu': 'RP2350', 'mpy': 'v6.3', 'arch': 'armv7emsp'}
# Stubber: v1.24.0
from __future__ import annotations
from _typeshed import Incomplete

MONO_HMSB: int = 4
MONO_HLSB: int = 3
RGB565: int = 1
MONO_VLSB: int = 0
MVLSB: int = 0
GS2_HMSB: int = 5
GS8: int = 6
GS4_HMSB: int = 2

def FrameBuffer1(*args, **kwargs) -> Incomplete: ...

class FrameBuffer:
    def poly(self, *args, **kwargs) -> Incomplete: ...
    def vline(self, *args, **kwargs) -> Incomplete: ...
    def pixel(self, *args, **kwargs) -> Incomplete: ...
    def text(self, *args, **kwargs) -> Incomplete: ...
    def rect(self, *args, **kwargs) -> Incomplete: ...
    def scroll(self, *args, **kwargs) -> Incomplete: ...
    def ellipse(self, *args, **kwargs) -> Incomplete: ...
    def line(self, *args, **kwargs) -> Incomplete: ...
    def blit(self, *args, **kwargs) -> Incomplete: ...
    def hline(self, *args, **kwargs) -> Incomplete: ...
    def fill(self, *args, **kwargs) -> Incomplete: ...
    def fill_rect(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
