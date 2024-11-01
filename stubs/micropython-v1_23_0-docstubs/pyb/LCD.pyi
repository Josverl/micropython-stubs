""" """

from __future__ import annotations
from _typeshed import Incomplete

class LCD:
    """
    Construct an LCD object in the given skin position.  ``skin_position`` can be 'X' or 'Y', and
    should match the position where the LCD pyskin is plugged in.
    """

    def __init__(self, skin_position) -> None: ...
    def command(self, instr_data, buf) -> None:
        """
        Send an arbitrary command to the LCD.  Pass 0 for ``instr_data`` to send an
        instruction, otherwise pass 1 to send data.  ``buf`` is a buffer with the
        instructions/data to send.
        """
        ...

    def contrast(self, value) -> None:
        """
        Set the contrast of the LCD.  Valid values are between 0 and 47.
        """
        ...

    def fill(self, colour) -> None:
        """
        Fill the screen with the given colour (0 or 1 for white or black).

        This method writes to the hidden buffer.  Use ``show()`` to show the buffer.
        """
        ...

    def get(self, x, y) -> int:
        """
        Get the pixel at the position ``(x, y)``.  Returns 0 or 1.

        This method reads from the visible buffer.
        """
        ...

    def light(self, value) -> None:
        """
        Turn the backlight on/off.  True or 1 turns it on, False or 0 turns it off.
        """
        ...

    def pixel(self, x, y, colour) -> None:
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

    def text(self, str, x, y, colour) -> None:
        """
        Draw the given text to the position ``(x, y)`` using the given colour (0 or 1).

        This method writes to the hidden buffer.  Use ``show()`` to show the buffer.
        """
        ...

    def write(self, str) -> None:
        """
        Write the string ``str`` to the screen.  It will appear immediately.
        """
        ...
