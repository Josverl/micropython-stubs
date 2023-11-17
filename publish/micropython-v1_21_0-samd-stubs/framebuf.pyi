"""
Frame buffer manipulation.

MicroPython module: https://docs.micropython.org/en/v1.21.0/library/framebuf.html

This module provides a general frame buffer which can be used to create
bitmap images, which can then be sent to a display.
"""
from _typeshed import Incomplete, Incomplete as Incomplete
from typing import Any, Optional

MONO_HMSB: int
MONO_HLSB: int
RGB565: int
MONO_VLSB: int
MVLSB: int
GS2_HMSB: int
GS8: int
GS4_HMSB: int

def FrameBuffer1(*args, **kwargs) -> Incomplete: ...

class FrameBuffer:
    """
    Construct a FrameBuffer object.  The parameters are:

        - *buffer* is an object with a buffer protocol which must be large
          enough to contain every pixel defined by the width, height and
          format of the FrameBuffer.
        - *width* is the width of the FrameBuffer in pixels
        - *height* is the height of the FrameBuffer in pixels
        - *format* specifies the type of pixel used in the FrameBuffer;
          permissible values are listed under Constants below. These set the
          number of bits used to encode a color value and the layout of these
          bits in *buffer*.
          Where a color value c is passed to a method, c is a small integer
          with an encoding that is dependent on the format of the FrameBuffer.
        - *stride* is the number of pixels between each horizontal line
          of pixels in the FrameBuffer. This defaults to *width* but may
          need adjustments when implementing a FrameBuffer within another
          larger FrameBuffer or screen. The *buffer* size must accommodate
          an increased step size.

    One must specify valid *buffer*, *width*, *height*, *format* and
    optionally *stride*.  Invalid *buffer* size or dimensions may lead to
    unexpected errors.
    """

    def poly(self, x, y, coords, c, f: Optional[Any] = None) -> Incomplete:
        """
        Given a list of coordinates, draw an arbitrary (convex or concave) closed
        polygon at the given x, y location using the given color.

        The *coords* must be specified as a :mod:`array` of integers, e.g.
        ``array('h', [x0, y0, x1, y1, ... xn, yn])``.

        The optional *f* parameter can be set to ``True`` to fill the polygon.
        Otherwise just a one pixel outline is drawn.
        """
        ...
    def vline(self, x, y, h, c) -> Incomplete: ...
    def pixel(self, x, y, c: Optional[Any] = None) -> Incomplete:
        """
        If *c* is not given, get the color value of the specified pixel.
        If *c* is given, set the specified pixel to the given color.
        """
        ...
    def text(self, s, x, y, c: Optional[Any] = None) -> None:
        """
        Write text to the FrameBuffer using the the coordinates as the upper-left
        corner of the text. The color of the text can be defined by the optional
        argument but is otherwise a default value of 1. All characters have
        dimensions of 8x8 pixels and there is currently no way to change the font.
        """
        ...
    def rect(self, x, y, w, h, c, f: Optional[Any] = None) -> None:
        """
        Draw a rectangle at the given location, size and color.

        The optional *f* parameter can be set to ``True`` to fill the rectangle.
        Otherwise just a one pixel outline is drawn.
        """
        ...
    def scroll(self, xstep, ystep) -> Incomplete:
        """
        Shift the contents of the FrameBuffer by the given vector. This may
        leave a footprint of the previous colors in the FrameBuffer.
        """
        ...
    def ellipse(self, x, y, xr, yr, c, f, m: Optional[Any] = None) -> None:
        """
        Draw an ellipse at the given location. Radii *xr* and *yr* define the
        geometry; equal values cause a circle to be drawn. The *c* parameter
        defines the color.

        The optional *f* parameter can be set to ``True`` to fill the ellipse.
        Otherwise just a one pixel outline is drawn.

        The optional *m* parameter enables drawing to be restricted to certain
        quadrants of the ellipse. The LS four bits determine which quadrants are
        to be drawn, with bit 0 specifying Q1, b1 Q2, b2 Q3 and b3 Q4. Quadrants
        are numbered counterclockwise with Q1 being top right.
        """
        ...
    def line(self, x1, y1, x2, y2, c) -> None:
        """
        Draw a line from a set of coordinates using the given color and
        a thickness of 1 pixel. The `line` method draws the line up to
        a second set of coordinates whereas the `hline` and `vline`
        methods draw horizontal and vertical lines respectively up to
        a given length.
        """
        ...
    def blit(self, fbuf, x, y, key=-1, palette=None) -> None:
        """
        Draw another FrameBuffer on top of the current one at the given coordinates.
        If *key* is specified then it should be a color integer and the
        corresponding color will be considered transparent: all pixels with that
        color value will not be drawn. (If the *palette* is specified then the *key*
        is compared to the value from *palette*, not to the value directly from
        *fbuf*.)

        The *palette* argument enables blitting between FrameBuffers with differing
        formats. Typical usage is to render a monochrome or grayscale glyph/icon to
        a color display. The *palette* is a FrameBuffer instance whose format is
        that of the current FrameBuffer. The *palette* height is one pixel and its
        pixel width is the number of colors in the source FrameBuffer. The *palette*
        for an N-bit source needs 2**N pixels; the *palette* for a monochrome source
        would have 2 pixels representing background and foreground colors. The
        application assigns a color to each pixel in the *palette*. The color of the
        current pixel will be that of that *palette* pixel whose x position is the
        color of the corresponding source pixel.
        """
        ...
    def hline(self, x, y, w, c) -> Incomplete: ...
    def fill(self, c) -> None:
        """
        Fill the entire FrameBuffer with the specified color.
        """
        ...
    def fill_rect(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, buffer, width, height, format, stride=-1, /) -> None: ...
