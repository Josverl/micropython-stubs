""" """

from __future__ import annotations
from typing import Any, Optional, Tuple
from _typeshed import Incomplete

class WIZNET5K:
    """
    Create a WIZNET5K driver object, initialise the WIZnet5x00 module using the given
    SPI bus and pins, and return the WIZNET5K object.

    Arguments are:

      - *spi* is an :ref:`SPI object <pyb.SPI>` which is the SPI bus that the WIZnet5x00 is
        connected to (the MOSI, MISO and SCLK pins).
      - *pin_cs* is a :ref:`Pin object <pyb.Pin>` which is connected to the WIZnet5x00 nSS pin.
      - *pin_rst* is a :ref:`Pin object <pyb.Pin>` which is connected to the WIZnet5x00 nRESET pin.

    All of these objects will be initialised by the driver, so there is no need to
    initialise them yourself.  For example, you can use::

      nic = network.WIZNET5K(pyb.SPI(1), pyb.Pin.board.X5, pyb.Pin.board.X4)
    """

    def __init__(self, spi, pin_cs, pin_rst) -> None: ...
    def isconnected(self) -> bool:
        """
        Returns ``True`` if the physical Ethernet link is connected and up.
        Returns ``False`` otherwise.
        """
        ...

    def ifconfig(self, configtuple: Optional[Any] = None) -> Tuple:
        """
        Get/set IP address, subnet mask, gateway and DNS.

        When called with no arguments, this method returns a 4-tuple with the above information.

        To set the above values, pass a 4-tuple with the required information.  For example::

         nic.ifconfig(('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
        """
        ...

    def regs(self) -> Incomplete:
        """
        Dump the WIZnet5x00 registers.  Useful for debugging.
        """
        ...
