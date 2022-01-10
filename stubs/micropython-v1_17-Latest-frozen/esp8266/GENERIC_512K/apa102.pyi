from neopixel import NeoPixel
from typing import Any

class APA102(NeoPixel):
    ORDER: Any
    clock_pin: Any
    def __init__(self, clock_pin, data_pin, n, bpp: int = ...) -> None: ...
    def write(self) -> None: ...
