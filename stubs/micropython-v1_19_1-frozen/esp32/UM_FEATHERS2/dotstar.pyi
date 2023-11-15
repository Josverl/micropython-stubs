from _typeshed import Incomplete

START_HEADER_SIZE: int
LED_START: int
RGB: Incomplete
RBG: Incomplete
GRB: Incomplete
GBR: Incomplete
BRG: Incomplete
BGR: Incomplete

class DotStar:
    """
    A sequence of dotstars.

    :param SPI spi: The SPI object to write output to.
    :param int n: The number of dotstars in the chain
    :param float brightness: Brightness of the pixels between 0.0 and 1.0
    :param bool auto_write: True if the dotstars should immediately change when
        set. If False, `show` must be called explicitly.
    :param tuple pixel_order: Set the pixel order on the strip - different
         strips implement this differently. If you send red, and it looks blue
         or green on the strip, modify this! It should be one of the values above


    Example for TinyPICO:

    .. code-block:: python

        from dotstar import DotStar
        from machine import Pin, SPI

        spi = SPI(sck=Pin(12), mosi=Pin(13), miso=Pin(18)) # Configure SPI - note: miso is unused
        dotstar = DotStar(spi, 1)
        dotstar[0] = (128, 0, 0) # Red
    """

    _spi: Incomplete
    _n: Incomplete
    end_header_size: Incomplete
    _buf: Incomplete
    end_header_index: Incomplete
    pixel_order: Incomplete
    _brightness: float
    auto_write: bool
    def __init__(self, spi, n, *, brightness: float = ..., auto_write: bool = ..., pixel_order=...) -> None: ...
    def deinit(self) -> None:
        """Blank out the DotStars and release the resources."""
    def __enter__(self): ...
    def __exit__(
        self, exception_type: type[BaseException] | None, exception_value: BaseException | None, traceback: types.TracebackType | None
    ) -> None: ...
    def __repr__(self) -> str: ...
    def _set_item(self, index, value) -> None:
        """
        value can be one of three things:
                a (r,g,b) list/tuple
                a (r,g,b, brightness) list/tuple
                a single, longer int that contains RGB values, like 0xFFFFFF
            brightness, if specified should be a float 0-1

        Set a pixel value. You can set per-pixel brightness here, if it's not passed it
        will use the max value for pixel brightness value, which is a good default.

        Important notes about the per-pixel brightness - it's accomplished by
        PWMing the entire output of the LED, and that PWM is at a much
        slower clock than the rest of the LEDs. This can cause problems in
        Persistence of Vision Applications
        """
    def __setitem__(self, index, val) -> None: ...
    def __getitem__(self, index): ...
    def __len__(self) -> int: ...
    @property
    def brightness(self):
        """Overall brightness of the pixel"""
    @brightness.setter
    def brightness(self, brightness) -> None: ...
    def fill(self, color) -> None:
        """Colors all pixels the given ***color***."""
    def show(self) -> None:
        """Shows the new colors on the pixels themselves if they haven't already
        been autowritten.

        The colors may or may not be showing after this function returns because
        it may be done asynchronously."""
