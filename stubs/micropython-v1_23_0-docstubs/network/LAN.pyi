""" """

from __future__ import annotations
from typing import Any, Optional, Tuple
from _typeshed import Incomplete

class LAN:
    """
    Create a LAN driver object, initialise the LAN module using the given
    PHY driver name, and return the LAN object.

    Arguments are:

      - *id* is the number of the Ethernet port, either 0 or 1.
      - *phy_type* is the name of the PHY driver. For most board the on-board PHY has to be used and
        is the default. Suitable values are port specific.
      - *phy_addr* specifies the address of the PHY interface. As with *phy_type*, the hardwired value has
        to be used for most boards and that value is the default.
      - *ref_clk_mode* specifies, whether the data clock is provided by the Ethernet controller or
        the PYH interface.
        The default value is the one that matches the board. If set to ``LAN.OUT`` or ``Pin.OUT``
        or ``True``, the clock is driven by the Ethernet controller, if set to ``LAN.IN``
        or ``Pin.IN`` or ``False``, the clock is driven by the PHY interface.

    For example, with the Seeed Arch Mix board you can  use::

      nic = LAN(0, phy_type=LAN.PHY_LAN8720, phy_addr=1, ref_clk_mode=Pin.IN)
    """

    def __init__(self, id, *, phy_type=0, phy_addr=0, ref_clk_mode=0) -> None: ...
    def active(self, state: Optional[Any] = None) -> Incomplete:
        """
        With a parameter, it sets the interface active if *state* is true, otherwise it
        sets it inactive.
        Without a parameter, it returns the state.
        """
        ...

    def isconnected(self) -> bool:
        """
        Returns ``True`` if the physical Ethernet link is connected and up.
        Returns ``False`` otherwise.
        """
        ...

    def status(self) -> Incomplete:
        """
        Returns the LAN status.
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

    def config(self, config_parameters) -> Incomplete:
        """
        Sets or gets parameters of the LAN interface. The only parameter that can be
        retrieved is the MAC address, using::

           mac = LAN.config("mac")

        The parameters that can be set are:

         - ``trace=n`` sets trace levels; suitable values are:

             - 2: trace TX
             - 4: trace RX
             - 8: full trace

         - ``low_power=bool`` sets or clears low power mode, valid values being ``False``
           or ``True``.
        """
        ...
