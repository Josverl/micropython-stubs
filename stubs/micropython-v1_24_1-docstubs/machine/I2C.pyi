""" """

from __future__ import annotations
from _typeshed import Incomplete
from typing import Sequence, overload, List
from typing_extensions import TypeVar, TypeAlias, Awaitable
from _mpy_shed import AnyReadableBuf, AnyWritableBuf
from .Pin import Pin
from machine.Pin import Pin, PinLike

ID_T: TypeAlias = int | str

class I2C:
    """
    I2C is a two-wire protocol for communicating between devices.  At the physical
    level it consists of 2 wires: SCL and SDA, the clock and data lines respectively.

    I2C objects are created attached to a specific bus.  They can be initialised
    when created, or initialised later on.

    Printing the I2C object gives you information about its configuration.

    Both hardware and software I2C implementations exist via the
    :ref:`machine.I2C <machine.I2C>` and `machine.SoftI2C` classes.  Hardware I2C uses
    underlying hardware support of the system to perform the reads/writes and is
    usually efficient and fast but may have restrictions on which pins can be used.
    Software I2C is implemented by bit-banging and can be used on any pin but is not
    as efficient.  These classes have the same methods available and differ primarily
    in the way they are constructed.

    Example usage::

        from machine import I2C

        i2c = I2C(freq=400000)          # create I2C peripheral at frequency of 400kHz
                                        # depending on the port, extra parameters may be required
                                        # to select the peripheral and/or pins to use

        i2c.scan()                      # scan for peripherals, returning a list of 7-bit addresses

        i2c.writeto(42, b'123')         # write 3 bytes to peripheral with 7-bit address 42
        i2c.readfrom(42, 4)             # read 4 bytes from peripheral with 7-bit address 42

        i2c.readfrom_mem(42, 8, 3)      # read 3 bytes from memory of peripheral 42,
                                        #   starting at memory-address 8 in the peripheral
        i2c.writeto_mem(42, 2, b'\x10') # write 1 byte to memory of peripheral 42
                                        #   starting at address 2 in the peripheral
    """

    @overload
    def __init__(self, id: ID_T, /, *, freq: int = 400_000):
        """
        Construct and return a new I2C object using the following parameters:

           - *id* identifies a particular I2C peripheral.  Allowed values for
             depend on the particular port/board
           - *scl* should be a pin object specifying the pin to use for SCL.
           - *sda* should be a pin object specifying the pin to use for SDA.
           - *freq* should be an integer which sets the maximum frequency
             for SCL.

        Note that some ports/boards will have default values of *scl* and *sda*
        that can be changed in this constructor.  Others will have fixed values
        of *scl* and *sda* that cannot be changed.
        """

    @overload
    def __init__(self, id: ID_T, /, *, scl: PinLike, sda: PinLike, freq: int = 400_000):
        """
        Construct and return a new I2C object using the following parameters:

           - *id* identifies a particular I2C peripheral.  Allowed values for
             depend on the particular port/board
           - *scl* should be a pin object specifying the pin to use for SCL.
           - *sda* should be a pin object specifying the pin to use for SDA.
           - *freq* should be an integer which sets the maximum frequency
             for SCL.

        Note that some ports/boards will have default values of *scl* and *sda*
        that can be changed in this constructor.  Others will have fixed values
        of *scl* and *sda* that cannot be changed.
        """

    @overload
    def __init__(self, *, scl: PinLike, sda: PinLike, freq: int = 400_000) -> None:
        """
        Initialise the I2C bus with the given arguments:

           - *scl* is a pin object for the SCL line
           - *sda* is a pin object for the SDA line
           - *freq* is the SCL clock rate

         In the case of hardware I2C the actual clock frequency may be lower than the
         requested frequency. This is dependent on the platform hardware. The actual
         rate may be determined by printing the I2C object.
        """

    @overload
    def init(self, *, freq: int = 400_000) -> None:
        """
        Initialise the I2C bus with the given arguments:

           - *scl* is a pin object for the SCL line
           - *sda* is a pin object for the SDA line
           - *freq* is the SCL clock rate

         In the case of hardware I2C the actual clock frequency may be lower than the
         requested frequency. This is dependent on the platform hardware. The actual
         rate may be determined by printing the I2C object.
        """

    @overload
    def init(self, *, scl: PinLike, sda: PinLike, freq: int = 400_000) -> None:
        """
        Initialise the I2C bus with the given arguments:

           - *scl* is a pin object for the SCL line
           - *sda* is a pin object for the SDA line
           - *freq* is the SCL clock rate

         In the case of hardware I2C the actual clock frequency may be lower than the
         requested frequency. This is dependent on the platform hardware. The actual
         rate may be determined by printing the I2C object.
        """

    def deinit(self) -> None:
        """
        Turn off the I2C bus.

        Availability: WiPy.
        """
        ...

    def scan(self) -> List:
        """
        Scan all I2C addresses between 0x08 and 0x77 inclusive and return a list of
        those that respond.  A device responds if it pulls the SDA line low after
        its address (including a write bit) is sent on the bus.
        """
        ...

    def start(self) -> None:
        """
        Generate a START condition on the bus (SDA transitions to low while SCL is high).
        """
        ...

    def stop(self) -> None:
        """
        Generate a STOP condition on the bus (SDA transitions to high while SCL is high).
        """
        ...

    def readinto(self, buf: AnyWritableBuf, nack: bool = True, /) -> None:
        """
        Reads bytes from the bus and stores them into *buf*.  The number of bytes
        read is the length of *buf*.  An ACK will be sent on the bus after
        receiving all but the last byte.  After the last byte is received, if *nack*
        is true then a NACK will be sent, otherwise an ACK will be sent (and in this
        case the peripheral assumes more bytes are going to be read in a later call).
        """
        ...

    def write(self, buf: AnyReadableBuf, /) -> int:
        """
        Write the bytes from *buf* to the bus.  Checks that an ACK is received
        after each byte and stops transmitting the remaining bytes if a NACK is
        received.  The function returns the number of ACKs that were received.
        """
        ...

    def readfrom(self, addr: int, nbytes: int, stop: bool = True, /) -> bytes:
        """
        Read *nbytes* from the peripheral specified by *addr*.
        If *stop* is true then a STOP condition is generated at the end of the transfer.
        Returns a `bytes` object with the data read.
        """
        ...

    def readfrom_into(self, addr: int, buf: AnyWritableBuf, stop: bool = True, /) -> None:
        """
        Read into *buf* from the peripheral specified by *addr*.
        The number of bytes read will be the length of *buf*.
        If *stop* is true then a STOP condition is generated at the end of the transfer.

        The method returns ``None``.
        """
        ...

    def writeto(self, addr: int, buf: AnyReadableBuf, stop: bool = True, /) -> int:
        """
        Write the bytes from *buf* to the peripheral specified by *addr*.  If a
        NACK is received following the write of a byte from *buf* then the
        remaining bytes are not sent.  If *stop* is true then a STOP condition is
        generated at the end of the transfer, even if a NACK is received.
        The function returns the number of ACKs that were received.
        """
        ...

    def writevto(self, addr: int, vector: Sequence[AnyReadableBuf], stop: bool = True, /) -> int:
        """
        Write the bytes contained in *vector* to the peripheral specified by *addr*.
        *vector* should be a tuple or list of objects with the buffer protocol.
        The *addr* is sent once and then the bytes from each object in *vector*
        are written out sequentially.  The objects in *vector* may be zero bytes
        in length in which case they don't contribute to the output.

        If a NACK is received following the write of a byte from one of the
        objects in *vector* then the remaining bytes, and any remaining objects,
        are not sent.  If *stop* is true then a STOP condition is generated at
        the end of the transfer, even if a NACK is received.  The function
        returns the number of ACKs that were received.
        """
        ...

    def readfrom_mem(self, addr: int, memaddr: int, nbytes: int, /, *, addrsize: int = 8) -> bytes:
        """
        Read *nbytes* from the peripheral specified by *addr* starting from the memory
        address specified by *memaddr*.
        The argument *addrsize* specifies the address size in bits.
        Returns a `bytes` object with the data read.
        """
        ...

    def readfrom_mem_into(self, addr: int, memaddr: int, buf: AnyWritableBuf, /, *, addrsize: int = 8) -> None:
        """
        Read into *buf* from the peripheral specified by *addr* starting from the
        memory address specified by *memaddr*.  The number of bytes read is the
        length of *buf*.
        The argument *addrsize* specifies the address size in bits (on ESP8266
        this argument is not recognised and the address size is always 8 bits).

        The method returns ``None``.
        """
        ...

    def writeto_mem(self, addr: int, memaddr: int, buf: AnyReadableBuf, /, *, addrsize: int = 8) -> None:
        """
        Write *buf* to the peripheral specified by *addr* starting from the
        memory address specified by *memaddr*.
        The argument *addrsize* specifies the address size in bits (on ESP8266
        this argument is not recognised and the address size is always 8 bits).

        The method returns ``None``.
        """
        ...

class SoftI2C(I2C):
    """
    Construct a new software I2C object.  The parameters are:

       - *scl* should be a pin object specifying the pin to use for SCL.
       - *sda* should be a pin object specifying the pin to use for SDA.
       - *freq* should be an integer which sets the maximum frequency
         for SCL.
       - *timeout* is the maximum time in microseconds to wait for clock
         stretching (SCL held low by another device on the bus), after
         which an ``OSError(ETIMEDOUT)`` exception is raised.
    """

    def __init__(self, scl, sda, *, freq=400000, timeout=50000) -> None: ...
