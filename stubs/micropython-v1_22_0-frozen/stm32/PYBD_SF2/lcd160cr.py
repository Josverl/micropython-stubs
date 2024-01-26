# Driver for official MicroPython LCD160CR display
# MIT license; Copyright (c) 2017 Damien P. George

"""
Control of LCD160CR display.

MicroPython module: https://docs.micropython.org/en/v1.22.0/library/lcd160cr.html

This module provides control of the MicroPython LCD160CR display.
"""
from micropython import const
from utime import sleep_ms
from ustruct import calcsize, pack_into
import uerrno, machine
from _typeshed import Incomplete
from typing import Tuple

# for set_orient
PORTRAIT = const(0)
LANDSCAPE = const(1)
PORTRAIT_UPSIDEDOWN = const(2)
LANDSCAPE_UPSIDEDOWN = const(3)

# for set_startup_deco; can be or'd
STARTUP_DECO_NONE = const(0)
STARTUP_DECO_MLOGO = const(1)
STARTUP_DECO_INFO = const(2)

_uart_baud_table = {
    2400: 0,
    4800: 1,
    9600: 2,
    19200: 3,
    38400: 4,
    57600: 5,
    115200: 6,
    230400: 7,
    460800: 8,
}


class LCD160CR:
    """
    Construct an LCD160CR object.  The parameters are:

        - *connect* is a string specifying the physical connection of the LCD
          display to the board; valid values are "X", "Y", "XY", "YX".
          Use "X" when the display is connected to a pyboard in the X-skin
          position, and "Y" when connected in the Y-skin position.  "XY"
          and "YX" are used when the display is connected to the right or
          left side of the pyboard, respectively.
        - *pwr* is a Pin object connected to the LCD's power/enabled pin.
        - *i2c* is an I2C object connected to the LCD's I2C interface.
        - *spi* is an SPI object connected to the LCD's SPI interface.
        - *i2c_addr* is the I2C address of the display.

    One must specify either a valid *connect* or all of *pwr*, *i2c* and *spi*.
    If a valid *connect* is given then any of *pwr*, *i2c* or *spi* which are
    not passed as parameters (i.e. they are ``None``) will be created based on the
    value of *connect*.  This allows to override the default interface to the
    display if needed.

    The default values are:

        - "X" is for the X-skin and uses:
          ``pwr=Pin("X4")``, ``i2c=I2C("X")``, ``spi=SPI("X")``
        - "Y" is for the Y-skin and uses:
          ``pwr=Pin("Y4")``, ``i2c=I2C("Y")``, ``spi=SPI("Y")``
        - "XY" is for the right-side and uses:
          ``pwr=Pin("X4")``, ``i2c=I2C("Y")``, ``spi=SPI("X")``
        - "YX" is for the left-side and uses:
          ``pwr=Pin("Y4")``, ``i2c=I2C("X")``, ``spi=SPI("Y")``

    See `this image <http://micropython.org/resources/LCD160CRv10-positions.jpg>`_
    for how the display can be connected to the pyboard.
    """

    def __init__(self, connect=None, *, pwr=None, i2c=None, spi=None, i2c_addr=98) -> None:
        if connect in ("X", "Y", "XY", "YX"):
            i = connect[-1]
            j = connect[0]
            y = j + "4"
        elif connect == "C":
            i = 2
            j = 2
            y = "A7"
        else:
            if pwr is None or i2c is None or spi is None:
                raise ValueError('must specify valid "connect" or all of "pwr", "i2c" and "spi"')

        if pwr is None:
            pwr = machine.Pin(y, machine.Pin.OUT)
        if i2c is None:
            i2c = machine.I2C(i, freq=1000000)
        if spi is None:
            spi = machine.SPI(j, baudrate=13500000, polarity=0, phase=0)

        if not pwr.value():
            pwr(1)
            sleep_ms(10)
        # else:
        # alread have power
        # lets be optimistic...

        # set connections
        self.pwr = pwr
        self.i2c = i2c
        self.spi = spi
        self.i2c_addr = i2c_addr

        # create temp buffers and memoryviews
        self.buf16 = bytearray(16)
        self.buf19 = bytearray(19)
        self.buf = [None] * 10
        for i in range(1, 10):
            self.buf[i] = memoryview(self.buf16)[0:i]
        self.buf1 = self.buf[1]
        self.array4 = [0, 0, 0, 0]

        # set default orientation and window
        self.set_orient(PORTRAIT)
        self._fcmd2b("<BBBBBB", 0x76, 0, 0, self.w, self.h)  # viewport 'v'
        self._fcmd2b("<BBBBBB", 0x79, 0, 0, self.w, self.h)  # window 'y'

    def _send(self, cmd):
        i = self.i2c.writeto(self.i2c_addr, cmd)
        if i == len(cmd):
            return
        cmd = memoryview(cmd)
        n = len(cmd)
        while True:
            i += self.i2c.writeto(self.i2c_addr, cmd[i:])
            if i == n:
                return
            sleep_ms(10)

    def _fcmd2(self, fmt, a0, a1=0, a2=0):
        buf = self.buf[calcsize(fmt)]
        pack_into(fmt, buf, 0, 2, a0, a1, a2)
        self._send(buf)

    def _fcmd2b(self, fmt, a0, a1, a2, a3, a4=0):
        buf = self.buf[calcsize(fmt)]
        pack_into(fmt, buf, 0, 2, a0, a1, a2, a3, a4)
        self._send(buf)

    def _waitfor(self, n, buf):
        t = 5000
        while t:
            self.i2c.readfrom_into(self.i2c_addr, self.buf1)
            if self.buf1[0] >= n:
                self.i2c.readfrom_into(self.i2c_addr, buf)
                return
            t -= 1
            sleep_ms(1)
        raise OSError(uerrno.ETIMEDOUT)

    def oflush(self, n=255):
        t = 5000
        while t:
            self.i2c.readfrom_into(self.i2c_addr + 1, self.buf1)
            r = self.buf1[0]
            if r >= n:
                return
            t -= 1
            machine.idle()
        raise OSError(uerrno.ETIMEDOUT)

    def iflush(self):
        t = 5000
        while t:
            self.i2c.readfrom_into(self.i2c_addr, self.buf16)
            if self.buf16[0] == 0:
                return
            t -= 1
            sleep_ms(1)
        raise OSError(uerrno.ETIMEDOUT)

    #### MISC METHODS ####

    @staticmethod
    @staticmethod
    def rgb(r, g, b) -> int:
        """
        Return a 16-bit integer representing the given rgb color values.  The
        16-bit value can be used to set the font color (see
        :meth:`LCD160CR.set_text_color`) pen color (see :meth:`LCD160CR.set_pen`)
        and draw individual pixels.
        """
        return ((b & 0xF8) << 8) | ((g & 0xFC) << 3) | (r >> 3)

    @staticmethod
    @staticmethod
    def clip_line(c, w, h) -> Incomplete:
        """
        Clip the given line data.  This is for internal use.
        """
        while True:
            ca = ce = 0
            if c[1] < 0:
                ca |= 8
            elif c[1] > h:
                ca |= 4
            if c[0] < 0:
                ca |= 1
            elif c[0] > w:
                ca |= 2
            if c[3] < 0:
                ce |= 8
            elif c[3] > h:
                ce |= 4
            if c[2] < 0:
                ce |= 1
            elif c[2] > w:
                ce |= 2
            if ca & ce:
                return False
            elif ca | ce:
                ca |= ce
                if ca & 1:
                    if c[2] < c[0]:
                        c[0], c[2] = c[2], c[0]
                        c[1], c[3] = c[3], c[1]
                    c[1] += ((-c[0]) * (c[3] - c[1])) // (c[2] - c[0])
                    c[0] = 0
                elif ca & 2:
                    if c[2] < c[0]:
                        c[0], c[2] = c[2], c[0]
                        c[1], c[3] = c[3], c[1]
                    c[3] += ((w - 1 - c[2]) * (c[3] - c[1])) // (c[2] - c[0])
                    c[2] = w - 1
                elif ca & 4:
                    if c[0] == c[2]:
                        if c[1] >= h:
                            c[1] = h - 1
                        if c[3] >= h:
                            c[3] = h - 1
                    else:
                        if c[3] < c[1]:
                            c[0], c[2] = c[2], c[0]
                            c[1], c[3] = c[3], c[1]
                        c[2] += ((h - 1 - c[3]) * (c[2] - c[0])) // (c[3] - c[1])
                        c[3] = h - 1
                else:
                    if c[0] == c[2]:
                        if c[1] < 0:
                            c[1] = 0
                        if c[3] < 0:
                            c[3] = 0
                    else:
                        if c[3] < c[1]:
                            c[0], c[2] = c[2], c[0]
                            c[1], c[3] = c[3], c[1]
                        c[0] += ((-c[1]) * (c[2] - c[0])) // (c[3] - c[1])
                        c[1] = 0
            else:
                return True

    #### SETUP COMMANDS ####

    def set_power(self, on) -> None:
        """
        Turn the display on or off, depending on the given value of *on*: 0 or ``False``
        will turn the display off, and 1 or ``True`` will turn it on.
        """
        self.pwr(on)
        sleep_ms(15)

    def set_orient(self, orient) -> None:
        """
        Set the orientation of the display.  The *orient* parameter can be one
        of `PORTRAIT`, `LANDSCAPE`, `PORTRAIT_UPSIDEDOWN`, `LANDSCAPE_UPSIDEDOWN`.
        """
        self._fcmd2("<BBB", 0x14, (orient & 3) + 4)
        # update width and height variables
        self.iflush()
        self._send(b"\x02g0")
        self._waitfor(4, self.buf[5])
        self.w = self.buf[5][1]
        self.h = self.buf[5][2]

    def set_brightness(self, value) -> None:
        """
        Set the brightness of the display, between 0 and 31.
        """
        self._fcmd2("<BBB", 0x16, value)

    def set_i2c_addr(self, addr) -> None:
        """
        Set the I2C address of the display.  The *addr* value must have the
        lower 2 bits cleared.
        """
        # 0x0e set i2c addr
        if addr & 3:
            raise ValueError("must specify mod 4 aligned address")
        self._fcmd2("<BBW", 0x0E, 0x433249 | (addr << 24))

    def set_uart_baudrate(self, baudrate) -> None:
        """
        Set the baudrate of the UART interface.
        """
        try:
            baudrate = _uart_baud_table[baudrate]
        except KeyError:
            raise ValueError("invalid baudrate")
        self._fcmd2("<BBB", 0x18, baudrate)

    def set_startup_deco(self, value) -> None:
        """
        Set the start-up decoration of the display.  The *value* parameter can be a
        logical or of `STARTUP_DECO_NONE`, `STARTUP_DECO_MLOGO`, `STARTUP_DECO_INFO`.
        """
        self._fcmd2("<BBB", 0x19, value)

    def save_to_flash(self) -> Incomplete:
        """
        Save the following parameters to flash so they persist on restart and power up:
        initial decoration, orientation, brightness, UART baud rate, I2C address.
        """
        self._send(b"\x02fn")

    #### PIXEL ACCESS ####

    def set_pixel(self, x, y, c) -> None:
        """
        Set the specified pixel to the given color.  The color should be a 16-bit
        integer and can be created by :meth:`LCD160CR.rgb`.
        """
        self._fcmd2b("<BBBBH", 0x41, x, y, c)

    def get_pixel(self, x, y) -> Incomplete:
        """
        Get the 16-bit value of the specified pixel.
        """
        self._fcmd2("<BBBB", 0x61, x, y)
        t = 1000
        while t:
            self.i2c.readfrom_into(self.i2c_addr, self.buf1)
            if self.buf1[0] >= 2:
                self.i2c.readfrom_into(self.i2c_addr, self.buf[3])
                return self.buf[3][1] | self.buf[3][2] << 8
            t -= 1
            sleep_ms(1)
        raise OSError(uerrno.ETIMEDOUT)

    def get_line(self, x, y, buf) -> Incomplete:
        """
        Low-level method to get a line of pixels into the given buffer.
        To read *n* pixels *buf* should be *2*n+1* bytes in length.  The first byte
        is a dummy byte and should be ignored, and subsequent bytes represent the
        pixels in the line starting at coordinate *(x, y)*.
        """
        l = len(buf) // 2
        self._fcmd2b("<BBBBB", 0x10, l, x, y)
        l *= 2
        t = 1000
        while t:
            self.i2c.readfrom_into(self.i2c_addr, self.buf1)
            if self.buf1[0] >= l:
                self.i2c.readfrom_into(self.i2c_addr, buf)
                return
            t -= 1
            sleep_ms(1)
        raise OSError(uerrno.ETIMEDOUT)

    def screen_dump(self, buf, x=0, y=0, w=None, h=None) -> Incomplete:
        """
        Dump the contents of the screen to the given buffer.  The parameters *x* and *y*
        specify the starting coordinate, and *w* and *h* the size of the region.  If *w*
        or *h* are ``None`` then they will take on their maximum values, set by the size
        of the screen minus the given *x* and *y* values.  *buf* should be large enough
        to hold ``2*w*h`` bytes.  If it's smaller then only the initial horizontal lines
        will be stored.
        """
        if w is None:
            w = self.w - x
        if h is None:
            h = self.h - y
        if w <= 127:
            line = bytearray(2 * w + 1)
            line2 = None
        else:
            # split line if more than 254 bytes needed
            buflen = (w + 1) // 2
            line = bytearray(2 * buflen + 1)
            line2 = memoryview(line)[: 2 * (w - buflen) + 1]
        for i in range(min(len(buf) // (2 * w), h)):
            ix = i * w * 2
            self.get_line(x, y + i, line)
            buf[ix : ix + len(line) - 1] = memoryview(line)[1:]
            ix += len(line) - 1
            if line2:
                self.get_line(x + buflen, y + i, line2)
                buf[ix : ix + len(line2) - 1] = memoryview(line2)[1:]
                ix += len(line2) - 1

    def screen_load(self, buf) -> None:
        """
        Load the entire screen from the given buffer.
        """
        l = self.w * self.h * 2 + 2
        self._fcmd2b("<BBHBBB", 0x70, l, 16, self.w, self.h)
        n = 0
        ar = memoryview(buf)
        while n < len(buf):
            if len(buf) - n >= 0x200:
                self._send(ar[n : n + 0x200])
                n += 0x200
            else:
                self._send(ar[n:])
                while n < self.w * self.h * 2:
                    self._send(b"\x00")
                    n += 1

    #### TEXT COMMANDS ####

    def set_pos(self, x, y) -> None:
        """
        Set the position for text output using :meth:`LCD160CR.write`.  The position
        is the upper-left corner of the text.
        """
        self._fcmd2("<BBBB", 0x58, x, y)

    def set_text_color(self, fg, bg) -> None:
        """
        Set the foreground and background color of the text.
        """
        self._fcmd2("<BBHH", 0x63, fg, bg)

    def set_font(self, font, scale=0, bold=0, trans=0, scroll=0) -> None:
        """
        Set the font for the text.  Subsequent calls to `write` will use the newly
        configured font.  The parameters are:

            - *font* is the font family to use, valid values are 0, 1, 2, 3.
            - *scale* is a scaling value for each character pixel, where the pixels
              are drawn as a square with side length equal to *scale + 1*.  The value
              can be between 0 and 63.
            - *bold* controls the number of pixels to overdraw each character pixel,
              making a bold effect.  The lower 2 bits of *bold* are the number of
              pixels to overdraw in the horizontal direction, and the next 2 bits are
              for the vertical direction.  For example, a *bold* value of 5 will
              overdraw 1 pixel in both the horizontal and vertical directions.
            - *trans* can be either 0 or 1 and if set to 1 the characters will be
              drawn with a transparent background.
            - *scroll* can be either 0 or 1 and if set to 1 the display will do a
              soft scroll if the text moves to the next line.
        """
        self._fcmd2(
            "<BBBB",
            0x46,
            (scroll << 7) | (trans << 6) | ((font & 3) << 4) | (bold & 0xF),
            scale & 0xFF,
        )

    def write(self, s) -> None:
        """
        Write text to the display, using the current position, color and font.
        As text is written the position is automatically incremented.  The
        display supports basic VT100 control codes such as newline and backspace.
        """
        # TODO: eventually check for room in LCD input queue
        self._send(s)

    #### PRIMITIVE DRAWING COMMANDS ####

    def set_pen(self, line, fill) -> None:
        """
        Set the line and fill color for primitive shapes.
        """
        self._fcmd2("<BBHH", 0x50, line, fill)

    def erase(self) -> Incomplete:
        """
        Erase the entire display to the pen fill color.
        """
        self._send(b"\x02\x45")

    def dot(self, x, y) -> None:
        """
        Draw a single pixel at the given location using the pen line color.
        """
        if 0 <= x < self.w and 0 <= y < self.h:
            self._fcmd2("<BBBB", 0x4B, x, y)

    def rect(self, x, y, w, h, cmd=0x72) -> Incomplete:
        if x + w <= 0 or y + h <= 0 or x >= self.w or y >= self.h:
            return
        elif x < 0 or y < 0:
            left = top = True
            if x < 0:
                left = False
                w += x
                x = 0
            if y < 0:
                top = False
                h += y
                y = 0
            if cmd == 0x51 or cmd == 0x72:
                # draw interior
                self._fcmd2b("<BBBBBB", 0x51, x, y, min(w, 255), min(h, 255))
            if cmd == 0x57 or cmd == 0x72:
                # draw outline
                if left:
                    self._fcmd2b("<BBBBBB", 0x57, x, y, 1, min(h, 255))
                if top:
                    self._fcmd2b("<BBBBBB", 0x57, x, y, min(w, 255), 1)
                if x + w < self.w:
                    self._fcmd2b("<BBBBBB", 0x57, x + w, y, 1, min(h, 255))
                if y + h < self.h:
                    self._fcmd2b("<BBBBBB", 0x57, x, y + h, min(w, 255), 1)
        else:
            self._fcmd2b("<BBBBBB", cmd, x, y, min(w, 255), min(h, 255))

    def rect_outline(self, x, y, w, h) -> Incomplete:
        self.rect(x, y, w, h, 0x57)

    def rect_interior(self, x, y, w, h) -> None:
        """
        Draw a rectangle at the given location and size using the pen line
        color for the outline, and the pen fill color for the interior.
        The `rect` method draws the outline and interior, while the other methods
        just draw one or the other.
        """
        self.rect(x, y, w, h, 0x51)

    def line(self, x1, y1, x2, y2) -> None:
        """
        Draw a line between the given coordinates using the pen line color.
        """
        ar4 = self.array4
        ar4[0] = x1
        ar4[1] = y1
        ar4[2] = x2
        ar4[3] = y2
        if self.clip_line(ar4, self.w, self.h):
            self._fcmd2b("<BBBBBB", 0x4C, ar4[0], ar4[1], ar4[2], ar4[3])

    def dot_no_clip(self, x, y) -> Incomplete:
        self._fcmd2("<BBBB", 0x4B, x, y)

    def rect_no_clip(self, x, y, w, h) -> Incomplete:
        self._fcmd2b("<BBBBBB", 0x72, x, y, w, h)

    def rect_outline_no_clip(self, x, y, w, h) -> Incomplete:
        self._fcmd2b("<BBBBBB", 0x57, x, y, w, h)

    def rect_interior_no_clip(self, x, y, w, h) -> Incomplete:
        self._fcmd2b("<BBBBBB", 0x51, x, y, w, h)

    def line_no_clip(self, x1, y1, x2, y2) -> Incomplete:
        """
        These methods are as above but don't do any clipping on the input
        coordinates.  They are faster than the clipping versions and can be
        used when you know that the coordinates are within the display.
        """
        self._fcmd2b("<BBBBBB", 0x4C, x1, y1, x2, y2)

    def poly_dot(self, data) -> None:
        """
        Draw a sequence of dots using the pen line color.
        The *data* should be a buffer of bytes, with each successive pair of
        bytes corresponding to coordinate pairs (x, y).
        """
        if len(data) & 1:
            raise ValueError("must specify even number of bytes")
        self._fcmd2("<BBB", 0x71, len(data) // 2)
        self._send(data)

    def poly_line(self, data) -> Incomplete:
        """
        Similar to :meth:`LCD160CR.poly_dot` but draws lines between the dots.
        """
        if len(data) & 1:
            raise ValueError("must specify even number of bytes")
        self._fcmd2("<BBB", 0x78, len(data) // 2)
        self._send(data)

    #### TOUCH COMMANDS ####

    def touch_config(self, calib=False, save=False, irq=None) -> None:
        """
        Configure the touch panel:

            - If *calib* is ``True`` then the call will trigger a touch calibration of
              the resistive touch sensor.  This requires the user to touch various
              parts of the screen.
            - If *save* is ``True`` then the touch parameters will be saved to NVRAM
              to persist across reset/power up.
            - If *irq* is ``True`` then the display will be configured to pull the IRQ
              line low when a touch force is detected.  If *irq* is ``False`` then this
              feature is disabled.  If *irq* is ``None`` (the default value) then no
              change is made to this setting.
        """
        self._fcmd2("<BBBB", 0x7A, (irq is not None) << 2 | save << 1 | calib, bool(irq) << 7)

    def is_touched(self) -> bool:
        """
        Returns a boolean: ``True`` if there is currently a touch force on the screen,
        ``False`` otherwise.
        """
        self._send(b"\x02T")
        b = self.buf[4]
        self._waitfor(3, b)
        return b[1] >> 7 != 0

    def get_touch(self) -> Tuple:
        """
        Returns a 3-tuple of: *(active, x, y)*.  If there is currently a touch force
        on the screen then *active* is 1, otherwise it is 0.  The *x* and *y* values
        indicate the position of the current or most recent touch.
        """
        self._send(b"\x02T")  # implicit LCD output flush
        b = self.buf[4]
        self._waitfor(3, b)
        return b[1] >> 7, b[2], b[3]

    #### ADVANCED COMMANDS ####

    def set_spi_win(self, x, y, w, h) -> None:
        """
        Set the window that SPI data is written to.
        """
        pack_into("<BBBHHHHHHHH", self.buf19, 0, 2, 0x55, 10, x, y, x + w - 1, y + h - 1, 0, 0, 0, 0xFFFF)
        self._send(self.buf19)

    def fast_spi(self, flush=True) -> SPI:
        """
        Ready the display to accept RGB pixel data on the SPI bus, resetting the location
        of the first byte to go to the top-left corner of the window set by
        :meth:`LCD160CR.set_spi_win`.
        The method returns an SPI object which can be used to write the pixel data.

        Pixels should be sent as 16-bit RGB values in the 5-6-5 format.  The destination
        counter will increase as data is sent, and data can be sent in arbitrary sized
        chunks.  Once the destination counter reaches the end of the window specified by
        :meth:`LCD160CR.set_spi_win` it will wrap around to the top-left corner of that window.
        """
        self._send(b"\x02\x12")
        if flush:
            self.oflush()
        return self.spi

    def show_framebuf(self, buf) -> None:
        """
        Show the given buffer on the display.  *buf* should be an array of bytes containing
        the 16-bit RGB values for the pixels, and they will be written to the area
        specified by :meth:`LCD160CR.set_spi_win`, starting from the top-left corner.

        The `framebuf <framebuf.html>`_ module can be used to construct frame buffers
        and provides drawing primitives. Using a frame buffer will improve
        performance of animations when compared to drawing directly to the screen.
        """
        self.fast_spi().write(buf)

    def set_scroll(self, on) -> None:
        """
        Turn scrolling on or off.  This controls globally whether any window regions will
        scroll.
        """
        self._fcmd2("<BBB", 0x15, on)

    def set_scroll_win(self, win, x=-1, y=0, w=0, h=0, vec=0, pat=0, fill=0x07E0, color=0) -> None:
        """
        Configure a window region for scrolling:

            - *win* is the window id to configure.  There are 0..7 standard windows for
              general purpose use.  Window 8 is the text scroll window (the ticker).
            - *x*, *y*, *w*, *h* specify the location of the window in the display.
            - *vec* specifies the direction and speed of scroll: it is a 16-bit value
              of the form ``0bF.ddSSSSSSSSSSSS``.  *dd* is 0, 1, 2, 3 for +x, +y, -x,
              -y scrolling. *F* sets the speed format, with 0 meaning that the window
              is shifted *S % 256* pixel every frame, and 1 meaning that the window
              is shifted 1 pixel every *S* frames.
            - *pat* is a 16-bit pattern mask for the background.
            - *fill* is the fill color.
            - *color* is the extra color, either of the text or pattern foreground.
        """
        pack_into("<BBBHHHHHHHH", self.buf19, 0, 2, 0x55, win, x, y, w, h, vec, pat, fill, color)
        self._send(self.buf19)

    def set_scroll_win_param(self, win, param, value) -> Incomplete:
        """
        Set a single parameter of a scrolling window region:

            - *win* is the window id, 0..8.
            - *param* is the parameter number to configure, 0..7, and corresponds
              to the parameters in the `set_scroll_win` method.
            - *value* is the value to set.
        """
        self._fcmd2b("<BBBBH", 0x75, win, param, value)

    def set_scroll_buf(self, s) -> None:
        """
        Set the string for scrolling in window 8.  The parameter *s* must be a string
        with length 32 or less.
        """
        l = len(s)
        if l > 32:
            raise ValueError("length must be 32 or less")
        self._fcmd2("<BBB", 0x11, l)
        self._send(s)

    def jpeg_start(self, l) -> Incomplete:
        if l > 0xFFFF:
            raise ValueError("length must be 65535 or less")
        self.oflush()
        self._fcmd2("<BBH", 0x6A, l)

    def jpeg_data(self, buf) -> None:
        """
        Display a JPEG with the data split across multiple buffers.  There must be
        a single call to `jpeg_start` to begin with, specifying the total number of
        bytes in the JPEG.  Then this number of bytes must be transferred to the
        display using one or more calls to the `jpeg_data` command.
        """
        self._send(buf)

    def jpeg(self, buf) -> None:
        """
        Display a JPEG.  *buf* should contain the entire JPEG data. JPEG data should
        not include EXIF information. The following encodings are supported: Baseline
        DCT, Huffman coding, 8 bits per sample, 3 color components, YCbCr4:2:2.
        The origin of the JPEG is set by :meth:`LCD160CR.set_pos`.
        """
        self.jpeg_start(len(buf))
        self.jpeg_data(buf)

    def feed_wdt(self) -> Incomplete:
        """
        The first call to this method will start the display's internal watchdog
        timer.  Subsequent calls will feed the watchdog.  The timeout is roughly 30
        seconds.
        """
        self._send(b"\x02\x17")

    def reset(self) -> None:
        """
        Reset the display.
        """
        self._send(b"\x02Y\xef\xbe\xad\xde")
        sleep_ms(15)
