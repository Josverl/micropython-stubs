""" """

from __future__ import annotations

from typing import Any, Optional

from _typeshed import Incomplete
from typing_extensions import Awaitable, TypeAlias, TypeVar

class Display:
    """
    Gets an object for accessing a Display identified by ``id``.

    ``id`` can be an integer (``0``, ``1``...) or a string (``"ssd1306@3c"``) identifying a display node by its position or by its node identifiers.
    """
    def __init__(self, id) -> None: ...
    def write(self, buf, x, y, size_x, size_y) -> None:
        """
        Write a buffer-protocol object in the Display's Pixel Format to the display.

        Optionally x and y position, x size, and y size can be specified.
        """
        ...
    def rgb(self, r, g, b) -> Incomplete:
        """
        Convert a RGB color to the Display's Pixel Format.
        """
        ...
    def capabilities(self) -> Incomplete:
        """
        Retrieve a tuple describing the display in the format:

        ``(X Size, Y Size, Supported PFs, Current PF, Current Orientation, Misc Characteristics, Current PF as framebuf format)``
        """
        ...
    def format(self, format: Optional[Any] = None) -> Incomplete:
        """
        Get and set the Pixel Format of the Display.
        """
        ...
    def blanking(self, value) -> None:
        """
        Enable or disable blanking.
        """
        ...
    def clear(self) -> None:
        """
        Clear the Display.
        """
        ...
    def set_brightness(self, value) -> None:
        """
        Set the Display's brightness from ``0`` to ``255``.
        """
        ...
    def set_contrast(self, value) -> None:
        """
        Set the Display's contrast from ``0`` to ``255``.
        """
        ...
    def orientation(self, orientation: Optional[Any] = None) -> Incomplete:
        """
        Get and set the Orientation of the Display.
        """
        ...
    def as_framebuf(self) -> Incomplete:
        """
        If :mod:`framebuf` is enabled, generate a :class:`framebuf.FrameBuffer` instance augmented with a ``show()`` function that directly maps to the display with the currently configured settings.
        """
        ...
