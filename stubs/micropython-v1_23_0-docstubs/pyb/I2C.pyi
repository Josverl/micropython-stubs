""" """

from __future__ import annotations
from typing import List
from _typeshed import Incomplete

class I2C:
    """
    Construct an I2C object on the given bus.  ``bus`` can be 1 or 2, 'X' or
    'Y'. With no additional parameters, the I2C object is created but not
    initialised (it has the settings from the last initialisation of
    the bus, if any).  If extra arguments are given, the bus is initialised.
    See ``init`` for parameters of initialisation.

    The physical pins of the I2C buses on Pyboards V1.0 and V1.1 are:

      - ``I2C(1)`` is on the X position: ``(SCL, SDA) = (X9, X10) = (PB6, PB7)``
      - ``I2C(2)`` is on the Y position: ``(SCL, SDA) = (Y9, Y10) = (PB10, PB11)``

    On the Pyboard Lite:

      - ``I2C(1)`` is on the X position: ``(SCL, SDA) = (X9, X10) = (PB6, PB7)``
      - ``I2C(3)`` is on the Y position: ``(SCL, SDA) = (Y9, Y10) = (PA8, PB8)``

    Calling the constructor with 'X' or 'Y' enables portability between Pyboard
    types.
    """

    CONTROLLER: Incomplete
    """for initialising the bus to controller mode"""
    PERIPHERAL: Incomplete
    """for initialising the bus to peripheral mode"""
    def __init__(
        self, bus, mode, baudrate=328125, *, prescaler=-1, polarity=1, phase=0, bits=8, firstbit=MSB, ti=False, crc=None
    ) -> None: ...
    def deinit(self) -> None:
        """
        Turn off the I2C bus.
        """
        ...

    def init(self, mode, *, addr=0x12, baudrate=400000, gencall=False, dma=False) -> None:
        """
        Initialise the I2C bus with the given parameters:

           - ``mode`` must be either ``I2C.CONTROLLER`` or ``I2C.PERIPHERAL``
           - ``addr`` is the 7-bit address (only sensible for a peripheral)
           - ``baudrate`` is the SCL clock rate (only sensible for a controller)
           - ``gencall`` is whether to support general call mode
           - ``dma`` is whether to allow the use of DMA for the I2C transfers (note
             that DMA transfers have more precise timing but currently do not handle bus
             errors properly)

         The actual clock frequency may be lower than the requested frequency.
         This is dependent on the platform hardware. The actual rate may be determined
         by printing the I2C object.
        """
        ...

    def is_ready(self, addr) -> Incomplete:
        """
        Check if an I2C device responds to the given address.  Only valid when in controller mode.
        """
        ...

    def mem_read(self, data, addr, memaddr, *, timeout=5000, addr_size=8) -> Incomplete:
        """
        Read from the memory of an I2C device:

          - ``data`` can be an integer (number of bytes to read) or a buffer to read into
          - ``addr`` is the I2C device address
          - ``memaddr`` is the memory location within the I2C device
          - ``timeout`` is the timeout in milliseconds to wait for the read
          - ``addr_size`` selects width of memaddr: 8 or 16 bits

        Returns the read data.
        This is only valid in controller mode.
        """
        ...

    def mem_write(self, data, addr, memaddr, *, timeout=5000, addr_size=8) -> None:
        """
        Write to the memory of an I2C device:

          - ``data`` can be an integer or a buffer to write from
          - ``addr`` is the I2C device address
          - ``memaddr`` is the memory location within the I2C device
          - ``timeout`` is the timeout in milliseconds to wait for the write
          - ``addr_size`` selects width of memaddr: 8 or 16 bits

        Returns ``None``.
        This is only valid in controller mode.
        """
        ...

    def recv(self, recv, addr=0x00, *, timeout=5000) -> bytes:
        """
        Receive data on the bus:

          - ``recv`` can be an integer, which is the number of bytes to receive,
            or a mutable buffer, which will be filled with received bytes
          - ``addr`` is the address to receive from (only required in controller mode)
          - ``timeout`` is the timeout in milliseconds to wait for the receive

        Return value: if ``recv`` is an integer then a new buffer of the bytes received,
        otherwise the same buffer that was passed in to ``recv``.
        """
        ...

    def send(self, send, addr=0x00, *, timeout=5000) -> None:
        """
        Send data on the bus:

          - ``send`` is the data to send (an integer to send, or a buffer object)
          - ``addr`` is the address to send to (only required in controller mode)
          - ``timeout`` is the timeout in milliseconds to wait for the send

        Return value: ``None``.
        """
        ...

    def scan(self) -> List:
        """
        Scan all I2C addresses from 0x01 to 0x7f and return a list of those that respond.
        Only valid when in controller mode.
        """
        ...
