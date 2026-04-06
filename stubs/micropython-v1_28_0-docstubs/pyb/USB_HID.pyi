""" """

from __future__ import annotations
from _typeshed import Incomplete
from typing_extensions import TypeVar, TypeAlias, Awaitable
from _mpy_shed import AnyReadableBuf, AnyWritableBuf
from collections.abc import Sequence
from typing import overload

class USB_HID:
    """
    The USB_HID class allows creation of an object representing the USB
    Human Interface Device (HID) interface.  It can be used to emulate
    a peripheral such as a mouse or keyboard.

    Before you can use this class, you need to use :meth:`pyb.usb_mode()` to set the USB mode to include the HID interface.
    """
    def __init__(self) -> None:
        """
        Create a new USB_HID object.
        """

    @overload
    def recv(self, data: int, /, *, timeout: int = 5000) -> bytes:
        """
        Receive data on the bus:

          - ``data`` can be an integer, which is the number of bytes to receive,
            or a mutable buffer, which will be filled with received bytes.
          - ``timeout`` is the timeout in milliseconds to wait for the receive.

        Return value: if ``data`` is an integer then a new buffer of the bytes received,
        otherwise the number of bytes read into ``data`` is returned.
        """

    @overload
    def recv(self, data: AnyWritableBuf, /, *, timeout: int = 5000) -> int:
        """
        Receive data on the bus:

          - ``data`` can be an integer, which is the number of bytes to receive,
            or a mutable buffer, which will be filled with received bytes.
          - ``timeout`` is the timeout in milliseconds to wait for the receive.

        Return value: if ``data`` is an integer then a new buffer of the bytes received,
        otherwise the number of bytes read into ``data`` is returned.
        """
    def send(self, data: Sequence[int]) -> None:
        """
        Send data over the USB HID interface:

          - ``data`` is the data to send (a tuple/list of integers, or a
            bytearray).
        """
        ...
