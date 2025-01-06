""" """

from __future__ import annotations

from array import array

from Accel import *
from ADC import *
from CAN import *
from DAC import *
from ExtInt import *
from Flash import *
from I2C import *
from LCD import *
from LED import *
from Pin import *
from RTC import *
from Servo import *
from SPI import *
from Switch import *
from Timer import *
from UART import *
from USB_HID import *
from USB_VCP import *

class LCD:
    """
    The LCD class is used to control the LCD on the LCD touch-sensor pyskin,
    LCD32MKv1.0.  The LCD is a 128x32 pixel monochrome screen, part NHD-C12832A1Z.

    The pyskin must be connected in either the X or Y positions, and then
    an LCD object is made using::

        lcd = pyb.LCD('X')      # if pyskin is in the X position
        lcd = pyb.LCD('Y')      # if pyskin is in the Y position

    Then you can use::

        lcd.light(True)                 # turn the backlight on
        lcd.write('Hello world!\n')     # print text to the screen

    This driver implements a double buffer for setting/getting pixels.
    For example, to make a bouncing dot, try::

        x = y = 0
        dx = dy = 1
        while True:
            # update the dot's position
            x += dx
            y += dy

            # make the dot bounce of the edges of the screen
            if x <= 0 or x >= 127: dx = -dx
            if y <= 0 or y >= 31: dy = -dy

            lcd.fill(0)                 # clear the buffer
            lcd.pixel(x, y, 1)          # draw the dot
            lcd.show()                  # show the buffer
            pyb.delay(50)               # pause for 50ms
    """

    def __init__(self, skin_position: str, /) -> None:
        """
        Construct an LCD object in the given skin position.  ``skin_position`` can be 'X' or 'Y', and
        should match the position where the LCD pyskin is plugged in.
        """

    def command(self, inst_data: int, buf: bytes, /) -> None:
        """
        Send an arbitrary command to the LCD.  Pass 0 for ``instr_data`` to send an
        instruction, otherwise pass 1 to send data.  ``buf`` is a buffer with the
        instructions/data to send.
        """
        ...

    def contrast(self, value: int, /) -> None:
        """
        Set the contrast of the LCD.  Valid values are between 0 and 47.
        """
        ...

    def fill(self, colour: int, /) -> None:
        """
        Fill the screen with the given colour (0 or 1 for white or black).

        This method writes to the hidden buffer.  Use ``show()`` to show the buffer.
        """
        ...

    def get(self, x: int, y: int, /) -> int:
        """
        Get the pixel at the position ``(x, y)``.  Returns 0 or 1.

        This method reads from the visible buffer.
        """
        ...

    def light(self, value: bool | int, /) -> None:
        """
        Turn the backlight on/off.  True or 1 turns it on, False or 0 turns it off.
        """
        ...

    def pixel(self, x: int, y: int, colour: int, /) -> None:
        """
        Set the pixel at ``(x, y)`` to the given colour (0 or 1).

        This method writes to the hidden buffer.  Use ``show()`` to show the buffer.
        """
        ...

    def show(self) -> None:
        """
        Show the hidden buffer on the screen.
        """
        ...

    def text(self, str: str, x: int, y: int, colour: int, /) -> None:
        """
        Draw the given text to the position ``(x, y)`` using the given colour (0 or 1).

        This method writes to the hidden buffer.  Use ``show()`` to show the buffer.
        """
        ...

    def write(self, str: str, /) -> None:
        """
        Write the string ``str`` to the screen.  It will appear immediately.
        """
        ...
