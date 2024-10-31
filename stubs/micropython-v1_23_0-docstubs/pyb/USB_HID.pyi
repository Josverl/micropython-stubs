""" """

from __future__ import annotations
from _typeshed import Incomplete

class USB_HID:
    """
    Create a new USB_HID object.
    """

    def __init__(self) -> None: ...
    def recv(self, data, *, timeout=5000) -> int:
        """
        Receive data on the bus:

          - ``data`` can be an integer, which is the number of bytes to receive,
            or a mutable buffer, which will be filled with received bytes.
          - ``timeout`` is the timeout in milliseconds to wait for the receive.

        Return value: if ``data`` is an integer then a new buffer of the bytes received,
        otherwise the number of bytes read into ``data`` is returned.
        """
        ...

    def send(self, data) -> None:
        """
        Send data over the USB HID interface:

          - ``data`` is the data to send (a tuple/list of integers, or a
            bytearray).
        """
        ...
