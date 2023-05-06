from _typeshed import Incomplete
from neopixel import NeoPixel

class APA102(NeoPixel):
    ORDER: Incomplete
    clock_pin: Incomplete
    def __init__(self, clock_pin, data_pin, n, bpp: int = ...) -> None: ...
    def write(self) -> None: ...
