""" """

from __future__ import annotations
from typing import Optional, Tuple
from _typeshed import Incomplete

class SPI:
    """
    Construct an SPI object on the given bus, *id*. Values of *id* depend
    on a particular port and its hardware. Values 0, 1, etc. are commonly used
    to select hardware SPI block #0, #1, etc.

    With no additional parameters, the SPI object is created but not
    initialised (it has the settings from the last initialisation of
    the bus, if any).  If extra arguments are given, the bus is initialised.
    See ``init`` for parameters of initialisation.
    """

    CONTROLLER: Incomplete
    """for initialising the SPI bus to controller; this is only used for the WiPy"""
    MSB: Incomplete
    """set the first bit to be the most significant bit"""
    LSB: Incomplete
    """set the first bit to be the least significant bit"""
    def __init__(self, id, *args, **kwargs) -> None: ...
    def init(
        self, baudrate=1000000, *, polarity=0, phase=0, bits=8, firstbit=MSB, sck=None, mosi=None, miso=None, pins: Optional[Tuple]
    ) -> None:
        """
        Initialise the SPI bus with the given parameters:

          - ``baudrate`` is the SCK clock rate.
          - ``polarity`` can be 0 or 1, and is the level the idle clock line sits at.
          - ``phase`` can be 0 or 1 to sample data on the first or second clock edge
            respectively.
          - ``bits`` is the width in bits of each transfer. Only 8 is guaranteed to be supported by all hardware.
          - ``firstbit`` can be ``SPI.MSB`` or ``SPI.LSB``.
          - ``sck``, ``mosi``, ``miso`` are pins (machine.Pin) objects to use for bus signals. For most
            hardware SPI blocks (as selected by ``id`` parameter to the constructor), pins are fixed
            and cannot be changed. In some cases, hardware blocks allow 2-3 alternative pin sets for
            a hardware SPI block. Arbitrary pin assignments are possible only for a bitbanging SPI driver
            (``id`` = -1).
          - ``pins`` - WiPy port doesn't ``sck``, ``mosi``, ``miso`` arguments, and instead allows to
            specify them as a tuple of ``pins`` parameter.

        In the case of hardware SPI the actual clock frequency may be lower than the
        requested baudrate. This is dependent on the platform hardware. The actual
        rate may be determined by printing the SPI object.
        """
        ...

    def deinit(self) -> None:
        """
        Turn off the SPI bus.
        """
        ...

    def read(self, nbytes, write=0x00) -> bytes:
        """
        Read a number of bytes specified by ``nbytes`` while continuously writing
        the single byte given by ``write``.
        Returns a ``bytes`` object with the data that was read.
        """
        ...

    def readinto(self, buf, write=0x00) -> int:
        """
        Read into the buffer specified by ``buf`` while continuously writing the
        single byte given by ``write``.
        Returns ``None``.

        Note: on WiPy this function returns the number of bytes read.
        """
        ...

    def write(self, buf) -> int:
        """
        Write the bytes contained in ``buf``.
        Returns ``None``.

        Note: on WiPy this function returns the number of bytes written.
        """
        ...

    def write_readinto(self, write_buf, read_buf) -> int:
        """
        Write the bytes from ``write_buf`` while reading into ``read_buf``.  The
        buffers can be the same or different, but both buffers must have the
        same length.
        Returns ``None``.

        Note: on WiPy this function returns the number of bytes written.
        """
        ...

class SoftSPI(SPI):
    """
    Construct a new software SPI object.  Additional parameters must be
    given, usually at least *sck*, *mosi* and *miso*, and these are used
    to initialise the bus.  See `SPI.init` for a description of the parameters.
    """

    MSB: Incomplete
    """set the first bit to be the most significant bit"""
    LSB: Incomplete
    """set the first bit to be the least significant bit"""
    def __init__(self, baudrate=500000, *, polarity=0, phase=0, bits=8, firstbit=MSB, sck=None, mosi=None, miso=None) -> None: ...
