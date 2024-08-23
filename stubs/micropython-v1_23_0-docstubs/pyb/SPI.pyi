""" """

from __future__ import annotations
from _typeshed import Incomplete

class SPI:
    """
    Construct an SPI object on the given bus.  ``bus`` can be 1 or 2, or
    'X' or 'Y'. With no additional parameters, the SPI object is created but
    not initialised (it has the settings from the last initialisation of
    the bus, if any).  If extra arguments are given, the bus is initialised.
    See ``init`` for parameters of initialisation.

    The physical pins of the SPI buses are:

      - ``SPI(1)`` is on the X position: ``(NSS, SCK, MISO, MOSI) = (X5, X6, X7, X8) = (PA4, PA5, PA6, PA7)``
      - ``SPI(2)`` is on the Y position: ``(NSS, SCK, MISO, MOSI) = (Y5, Y6, Y7, Y8) = (PB12, PB13, PB14, PB15)``

    At the moment, the NSS pin is not used by the SPI driver and is free
    for other use.
    """

    CONTROLLER: Incomplete
    PERIPHERAL: Incomplete
    """for initialising the SPI bus to controller or peripheral mode"""
    LSB: Incomplete
    MSB: Incomplete
    """set the first bit to be the least or most significant bit"""
    def __init__(
        self, bus, mode, baudrate=328125, *, prescaler=-1, polarity=1, phase=0, bits=8, firstbit=MSB, ti=False, crc=None
    ) -> None: ...
    def deinit(self) -> None:
        """
        Turn off the SPI bus.
        """
        ...

    def init(self, mode, baudrate=328125, *, prescaler=-1, polarity=1, phase=0, bits=8, firstbit=MSB, ti=False, crc=None) -> None:
        """
        Initialise the SPI bus with the given parameters:

          - ``mode`` must be either ``SPI.CONTROLLER`` or ``SPI.PERIPHERAL``.
          - ``baudrate`` is the SCK clock rate (only sensible for a controller).
          - ``prescaler`` is the prescaler to use to derive SCK from the APB bus frequency;
            use of ``prescaler`` overrides ``baudrate``.
          - ``polarity`` can be 0 or 1, and is the level the idle clock line sits at.
          - ``phase`` can be 0 or 1 to sample data on the first or second clock edge
            respectively.
          - ``bits`` can be 8 or 16, and is the number of bits in each transferred word.
          - ``firstbit`` can be ``SPI.MSB`` or ``SPI.LSB``.
          - ``ti`` True indicates Texas Instruments, as opposed to Motorola, signal conventions.
          - ``crc`` can be None for no CRC, or a polynomial specifier.

        Note that the SPI clock frequency will not always be the requested baudrate.
        The hardware only supports baudrates that are the APB bus frequency
        (see :meth:`pyb.freq`) divided by a prescaler, which can be 2, 4, 8, 16, 32,
        64, 128 or 256.  SPI(1) is on AHB2, and SPI(2) is on AHB1.  For precise
        control over the SPI clock frequency, specify ``prescaler`` instead of
        ``baudrate``.

        Printing the SPI object will show you the computed baudrate and the chosen
        prescaler.
        """
        ...

    def recv(self, recv, *, timeout=5000) -> bytes:
        """
        Receive data on the bus:

          - ``recv`` can be an integer, which is the number of bytes to receive,
            or a mutable buffer, which will be filled with received bytes.
          - ``timeout`` is the timeout in milliseconds to wait for the receive.

        Return value: if ``recv`` is an integer then a new buffer of the bytes received,
        otherwise the same buffer that was passed in to ``recv``.
        """
        ...

    def send(self, send, *, timeout=5000) -> None:
        """
        Send data on the bus:

          - ``send`` is the data to send (an integer to send, or a buffer object).
          - ``timeout`` is the timeout in milliseconds to wait for the send.

        Return value: ``None``.
        """
        ...

    def send_recv(self, send, recv=None, *, timeout=5000) -> bytes:
        """
        Send and receive data on the bus at the same time:

          - ``send`` is the data to send (an integer to send, or a buffer object).
          - ``recv`` is a mutable buffer which will be filled with received bytes.
            It can be the same as ``send``, or omitted.  If omitted, a new buffer will
            be created.
          - ``timeout`` is the timeout in milliseconds to wait for the receive.

        Return value: the buffer with the received bytes.
        """
        ...
