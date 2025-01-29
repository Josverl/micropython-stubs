""" """

from __future__ import annotations
from _typeshed import Incomplete
from typing import overload, Any, Optional
from typing_extensions import TypeVar, TypeAlias, Awaitable
from _mpy_shed import AnyReadableBuf, AnyWritableBuf

class UART:
    """
    UART implements the standard UART/USART duplex serial communications protocol.  At
    the physical level it consists of 2 lines: RX and TX.  The unit of communication
    is a character (not to be confused with a string character) which can be 8 or 9
    bits wide.

    UART objects can be created and initialised using::

        from pyb import UART

        uart = UART(1, 9600)                         # init with given baudrate
        uart.init(9600, bits=8, parity=None, stop=1) # init with given parameters

    Bits can be 7, 8 or 9.  Parity can be None, 0 (even) or 1 (odd).  Stop can be 1 or 2.

    *Note:* with parity=None, only 8 and 9 bits are supported.  With parity enabled,
    only 7 and 8 bits are supported.

    A UART object acts like a `stream` object and reading and writing is done
    using the standard stream methods::

        uart.read(10)       # read 10 characters, returns a bytes object
        uart.read()         # read all available characters
        uart.readline()     # read a line
        uart.readinto(buf)  # read and store into the given buffer
        uart.write('abc')   # write the 3 characters

    Individual characters can be read/written using::

        uart.readchar()     # read 1 character and returns it as an integer
        uart.writechar(42)  # write 1 character

    To check if there is anything to be read, use::

        uart.any()          # returns the number of characters waiting


    *Note:* The stream functions ``read``, ``write``, etc. are new in MicroPython v1.3.4.
    Earlier versions use ``uart.send`` and ``uart.recv``.
    """

    RTS: Incomplete
    """to select the flow control type."""
    CTS: Incomplete
    """to select the flow control type."""
    @overload
    def __init__(self, bus: int | str, /):
        """
        Construct a UART object on the given bus.
        For Pyboard ``bus`` can be 1-4, 6, 'XA', 'XB', 'YA', or 'YB'.
        For Pyboard Lite ``bus`` can be 1, 2, 6, 'XB', or 'YA'.
        For Pyboard D ``bus`` can be 1-4, 'XA', 'YA' or 'YB'.
        With no additional parameters, the UART object is created but not
        initialised (it has the settings from the last initialisation of
        the bus, if any).  If extra arguments are given, the bus is initialised.
        See ``init`` for parameters of initialisation.

        The physical pins of the UART buses on Pyboard are:

          - ``UART(4)`` is on ``XA``: ``(TX, RX) = (X1, X2) = (PA0, PA1)``
          - ``UART(1)`` is on ``XB``: ``(TX, RX) = (X9, X10) = (PB6, PB7)``
          - ``UART(6)`` is on ``YA``: ``(TX, RX) = (Y1, Y2) = (PC6, PC7)``
          - ``UART(3)`` is on ``YB``: ``(TX, RX) = (Y9, Y10) = (PB10, PB11)``
          - ``UART(2)`` is on: ``(TX, RX) = (X3, X4) = (PA2, PA3)``

        The Pyboard Lite supports UART(1), UART(2) and UART(6) only, pins are:

          - ``UART(1)`` is on ``XB``: ``(TX, RX) = (X9, X10) = (PB6, PB7)``
          - ``UART(6)`` is on ``YA``: ``(TX, RX) = (Y1, Y2) = (PC6, PC7)``
          - ``UART(2)`` is on: ``(TX, RX) = (X1, X2) = (PA2, PA3)``

        The Pyboard D supports UART(1), UART(2), UART(3) and UART(4) only, pins are:

          - ``UART(4)`` is on ``XA``: ``(TX, RX) = (X1, X2) = (PA0, PA1)``
          - ``UART(1)`` is on ``YA``: ``(TX, RX) = (Y1, Y2) = (PA9, PA10)``
          - ``UART(3)`` is on ``YB``: ``(TX, RX) = (Y9, Y10) = (PB10, PB11)``
          - ``UART(2)`` is on: ``(TX, RX) = (X3, X4) = (PA2, PA3)``

        *Note:* Pyboard D has ``UART(1)`` on ``YA``, unlike Pyboard and Pyboard Lite that both
        have ``UART(1)`` on ``XB`` and ``UART(6)`` on ``YA``.
        """

    @overload
    def __init__(
        self,
        bus: int | str,
        baudrate: int,
        /,
        bits: int = 8,
        parity: int | None = None,
        stop: int = 1,
        *,
        timeout: int = 0,
        flow: int = 0,
        timeout_char: int = 0,
        read_buf_len: int = 64,
    ):
        """
        Construct a UART object on the given bus.
        For Pyboard ``bus`` can be 1-4, 6, 'XA', 'XB', 'YA', or 'YB'.
        For Pyboard Lite ``bus`` can be 1, 2, 6, 'XB', or 'YA'.
        For Pyboard D ``bus`` can be 1-4, 'XA', 'YA' or 'YB'.
        With no additional parameters, the UART object is created but not
        initialised (it has the settings from the last initialisation of
        the bus, if any).  If extra arguments are given, the bus is initialised.
        See ``init`` for parameters of initialisation.

        The physical pins of the UART buses on Pyboard are:

          - ``UART(4)`` is on ``XA``: ``(TX, RX) = (X1, X2) = (PA0, PA1)``
          - ``UART(1)`` is on ``XB``: ``(TX, RX) = (X9, X10) = (PB6, PB7)``
          - ``UART(6)`` is on ``YA``: ``(TX, RX) = (Y1, Y2) = (PC6, PC7)``
          - ``UART(3)`` is on ``YB``: ``(TX, RX) = (Y9, Y10) = (PB10, PB11)``
          - ``UART(2)`` is on: ``(TX, RX) = (X3, X4) = (PA2, PA3)``

        The Pyboard Lite supports UART(1), UART(2) and UART(6) only, pins are:

          - ``UART(1)`` is on ``XB``: ``(TX, RX) = (X9, X10) = (PB6, PB7)``
          - ``UART(6)`` is on ``YA``: ``(TX, RX) = (Y1, Y2) = (PC6, PC7)``
          - ``UART(2)`` is on: ``(TX, RX) = (X1, X2) = (PA2, PA3)``

        The Pyboard D supports UART(1), UART(2), UART(3) and UART(4) only, pins are:

          - ``UART(4)`` is on ``XA``: ``(TX, RX) = (X1, X2) = (PA0, PA1)``
          - ``UART(1)`` is on ``YA``: ``(TX, RX) = (Y1, Y2) = (PA9, PA10)``
          - ``UART(3)`` is on ``YB``: ``(TX, RX) = (Y9, Y10) = (PB10, PB11)``
          - ``UART(2)`` is on: ``(TX, RX) = (X3, X4) = (PA2, PA3)``

        *Note:* Pyboard D has ``UART(1)`` on ``YA``, unlike Pyboard and Pyboard Lite that both
        have ``UART(1)`` on ``XB`` and ``UART(6)`` on ``YA``.
        """

    def init(
        self,
        baudrate: int,
        /,
        bits: int = 8,
        parity: int | None = None,
        stop: int = 1,
        *,
        timeout: int = 0,
        flow: int = 0,
        timeout_char: int = 0,
        read_buf_len: int = 64,
    ):
        """
        Initialise the UART bus with the given parameters:

          - ``baudrate`` is the clock rate.
          - ``bits`` is the number of bits per character, 7, 8 or 9.
          - ``parity`` is the parity, ``None``, 0 (even) or 1 (odd).
          - ``stop`` is the number of stop bits, 1 or 2.
          - ``flow`` sets the flow control type. Can be 0, ``UART.RTS``, ``UART.CTS``
            or ``UART.RTS | UART.CTS``.
          - ``timeout`` is the timeout in milliseconds to wait for writing/reading the first character.
          - ``timeout_char`` is the timeout in milliseconds to wait between characters while writing or reading.
          - ``read_buf_len`` is the character length of the read buffer (0 to disable).

        This method will raise an exception if the baudrate could not be set within
        5% of the desired value.  The minimum baudrate is dictated by the frequency
        of the bus that the UART is on; UART(1) and UART(6) are APB2, the rest are on
        APB1.  The default bus frequencies give a minimum baudrate of 1300 for
        UART(1) and UART(6) and 650 for the others.  Use :func:`pyb.freq <pyb.freq>`
        to reduce the bus frequencies to get lower baudrates.

        *Note:* with parity=None, only 8 and 9 bits are supported.  With parity enabled,
        only 7 and 8 bits are supported.
        """
        ...

    def deinit(self) -> None:
        """
        Turn off the UART bus.
        """
        ...

    def any(self) -> int:
        """
        Returns the number of bytes waiting (may be 0).
        """
        ...

    @overload
    def read(self) -> bytes | None:
        """
        Read characters.  If ``nbytes`` is specified then read at most that many bytes.
        If ``nbytes`` are available in the buffer, returns immediately, otherwise returns
        when sufficient characters arrive or the timeout elapses.

        If ``nbytes`` is not given then the method reads as much data as possible.  It
        returns after the timeout has elapsed.

        *Note:* for 9 bit characters each character takes two bytes, ``nbytes`` must
        be even, and the number of characters is ``nbytes/2``.

        Return value: a bytes object containing the bytes read in.  Returns ``None``
        on timeout.
        """

    @overload
    def read(self, nbytes: int, /) -> bytes | None:
        """
        Read characters.  If ``nbytes`` is specified then read at most that many bytes.
        If ``nbytes`` are available in the buffer, returns immediately, otherwise returns
        when sufficient characters arrive or the timeout elapses.

        If ``nbytes`` is not given then the method reads as much data as possible.  It
        returns after the timeout has elapsed.

        *Note:* for 9 bit characters each character takes two bytes, ``nbytes`` must
        be even, and the number of characters is ``nbytes/2``.

        Return value: a bytes object containing the bytes read in.  Returns ``None``
        on timeout.
        """

    def readchar(self) -> int:
        """
        Receive a single character on the bus.

        Return value: The character read, as an integer.  Returns -1 on timeout.
        """
        ...

    @overload
    def readinto(self, buf: AnyWritableBuf, /) -> int | None:
        """
        Read bytes into the ``buf``.  If ``nbytes`` is specified then read at most
        that many bytes.  Otherwise, read at most ``len(buf)`` bytes.

        Return value: number of bytes read and stored into ``buf`` or ``None`` on
        timeout.
        """

    @overload
    def readinto(self, buf: AnyWritableBuf, nbytes: int, /) -> int | None:
        """
        Read bytes into the ``buf``.  If ``nbytes`` is specified then read at most
        that many bytes.  Otherwise, read at most ``len(buf)`` bytes.

        Return value: number of bytes read and stored into ``buf`` or ``None`` on
        timeout.
        """

    def readline(self) -> None:
        """
        Read a line, ending in a newline character. If such a line exists, return is
        immediate. If the timeout elapses, all available data is returned regardless
        of whether a newline exists.

        Return value: the line read or ``None`` on timeout if no data is available.
        """
        ...

    def write(self, buf: AnyWritableBuf, /) -> int:
        """
        Write the buffer of bytes to the bus.  If characters are 7 or 8 bits wide
        then each byte is one character.  If characters are 9 bits wide then two
        bytes are used for each character (little endian), and ``buf`` must contain
        an even number of bytes.

        Return value: number of bytes written. If a timeout occurs and no bytes
        were written returns ``None``.
        """
        ...

    def writechar(self, char: int, /) -> None:
        """
        Write a single character on the bus.  ``char`` is an integer to write.
        Return value: ``None``. See note below if CTS flow control is used.
        """
        ...

    def sendbreak(self) -> None:
        """
        Send a break condition on the bus.  This drives the bus low for a duration
        of 13 bits.
        Return value: ``None``.
        """
        ...
