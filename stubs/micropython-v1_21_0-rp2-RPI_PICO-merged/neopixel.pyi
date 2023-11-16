from _typeshed import Incomplete as Incomplete
from typing import Tuple

def bitstream(*args, **kwargs) -> Incomplete: ...

class NeoPixel:
    """
    Construct an NeoPixel object.  The parameters are:

        - *pin* is a machine.Pin instance.
        - *n* is the number of LEDs in the strip.
        - *bpp* is 3 for RGB LEDs, and 4 for RGBW LEDs.
        - *timing* is 0 for 400KHz, and 1 for 800kHz LEDs (most are 800kHz).
    """

    ORDER: tuple
    def write(self) -> None:
        """
        Writes the current pixel data to the strip.
        """
    def fill(self, pixel) -> None:
        """
        Sets the value of all pixels to the specified *pixel* value (i.e. an
        RGB/RGBW tuple).
        """
    def __init__(self, pin, n, *, bpp: int = ..., timing: int = ...) -> None: ...
