"""
network configuration. See: https://docs.micropython.org/en/v1.19.1/library/network.html

This module provides network drivers and routing configuration. To use this
module, a MicroPython variant/build with network capabilities must be installed.
Network drivers for specific hardware are available within this module and are
used to configure hardware network interface(s). Network services provided
by configured interfaces are then available for use via the :mod:`socket`
module.

For example::

    # connect/ show IP config a specific network interface
    # see below for examples of specific drivers
    import network
    import time
    nic = network.Driver(...)
    if not nic.isconnected():
        nic.connect()
        print("Waiting for connection...")
        while not nic.isconnected():
            time.sleep(1)
    print(nic.ifconfig())

    # now use socket as usual
    import socket
    addr = socket.getaddrinfo('micropython.org', 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(b'GET / HTTP/1.1\r\nHost: micropython.org\r\n\r\n')
    data = s.recv(1000)
    s.close()
"""
from typing import List, Optional, Tuple, Union, Any

STAT_WRONG_PASSWORD: int
PHY_IP101: int
PHY_LAN8720: int
PHY_RTL8201: int
PHY_DP83848: int
MODE_11B: int
MODE_11G: int
MODE_11N: int
STA_IF: int
STAT_HANDSHAKE_TIMEOUT: int
STAT_IDLE: int
STAT_NO_AP_FOUND: int
STAT_GOT_IP: int
STAT_ASSOC_FAIL: int
STAT_BEACON_TIMEOUT: int
STAT_CONNECTING: int
AUTH_WPA3_PSK: int
AUTH_WPA2_ENTERPRISE: int
AUTH_WPA2_PSK: int
AUTH_WPA2_WPA3_PSK: int
AUTH_WEP: int
AP_IF: int
AUTH_MAX: int
AUTH_OPEN: int
ETH_STOPPED: int
ETH_INITIALIZED: int
ETH_GOT_IP: int
ETH_STARTED: int
AUTH_WPA_PSK: int
AUTH_WPA_WPA2_PSK: int
ETH_DISCONNECTED: int
ETH_CONNECTED: int

class WLAN:
    """
    Create a WLAN network interface object. Supported interfaces are
    ``network.STA_IF`` (station aka client, connects to upstream WiFi access
    points) and ``network.AP_IF`` (access point, allows other WiFi clients to
    connect). Availability of the methods below depends on interface type.
    For example, only STA interface may `WLAN.connect()` to an access point.
    """

    def __init__(self, interface_id) -> None: ...
    def active(self, is_active: Optional[Any] = None) -> None:
        """
        Activate ("up") or deactivate ("down") network interface, if boolean
        argument is passed. Otherwise, query current state if no argument is
        provided. Most other methods require active interface.
        """
        ...
    def connect(self, ssid=None, password=None, *, bssid=None) -> None:
        """
        Connect to the specified wireless network, using the specified password.
        If *bssid* is given then the connection will be restricted to the
        access-point with that MAC address (the *ssid* must also be specified
        in this case).
        """
        ...
    def disconnect(self) -> None:
        """
        Disconnect from the currently connected wireless network.
        """
        ...
    def scan(self) -> List[Tuple]:
        """
        Scan for the available wireless networks.
        Hidden networks -- where the SSID is not broadcast -- will also be scanned
        if the WLAN interface allows it.

        Scanning is only possible on STA interface. Returns list of tuples with
        the information about WiFi access points:

            (ssid, bssid, channel, RSSI, authmode, hidden)

        *bssid* is hardware address of an access point, in binary form, returned as
        bytes object. You can use `binascii.hexlify()` to convert it to ASCII form.

        There are five values for authmode:

            * 0 -- open
            * 1 -- WEP
            * 2 -- WPA-PSK
            * 3 -- WPA2-PSK
            * 4 -- WPA/WPA2-PSK

        and two for hidden:

            * 0 -- visible
            * 1 -- hidden
        """
        ...
    def status(self, param: Optional[Any] = None) -> Any:
        """
        Return the current status of the wireless connection.

        When called with no argument the return value describes the network link status.
        The possible statuses are defined as constants:

            * ``STAT_IDLE`` -- no connection and no activity,
            * ``STAT_CONNECTING`` -- connecting in progress,
            * ``STAT_WRONG_PASSWORD`` -- failed due to incorrect password,
            * ``STAT_NO_AP_FOUND`` -- failed because no access point replied,
            * ``STAT_CONNECT_FAIL`` -- failed due to other problems,
            * ``STAT_GOT_IP`` -- connection successful.

        When called with one argument *param* should be a string naming the status
        parameter to retrieve.  Supported parameters in WiFI STA mode are: ``'rssi'``.
        """
        ...
    def isconnected(self) -> bool:
        """
        In case of STA mode, returns ``True`` if connected to a WiFi access
        point and has a valid IP address.  In AP mode returns ``True`` when a
        station is connected. Returns ``False`` otherwise.
        """
        ...
    def ifconfig(self, configtuple: Optional[Any] = None) -> Tuple:
        """
        Get/set IP-level network interface parameters: IP address, subnet mask,
        gateway and DNS server. When called with no arguments, this method returns
        a 4-tuple with the above information. To set the above values, pass a
        4-tuple with the required information.  For example::

         nic.ifconfig(('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
        """
        ...
    def config(self, *args, **kwargs) -> Any:
        """
        Get or set general network interface parameters. These methods allow to work
        with additional parameters beyond standard IP configuration (as dealt with by
        `WLAN.ifconfig()`). These include network-specific and hardware-specific
        parameters. For setting parameters, keyword argument syntax should be used,
        multiple parameters can be set at once. For querying, parameters name should
        be quoted as a string, and only one parameter can be queries at time::

         # Set WiFi access point name (formally known as ESSID) and WiFi channel
         ap.config(essid='My AP', channel=11)
         # Query params one by one
         print(ap.config('essid'))
         print(ap.config('channel'))

        Following are commonly supported parameters (availability of a specific parameter
        depends on network technology type, driver, and :term:`MicroPython port`).

        =============  ===========
        Parameter      Description
        =============  ===========
        mac            MAC address (bytes)
        essid          WiFi access point name (string)
        channel        WiFi channel (integer)
        hidden         Whether ESSID is hidden (boolean)
        authmode       Authentication mode supported (enumeration, see module constants)
        password       Access password (string)
        dhcp_hostname  The DHCP hostname to use
        reconnects     Number of reconnect attempts to make (integer, 0=none, -1=unlimited)
        txpower        Maximum transmit power in dBm (integer or float)
        =============  ===========
        """
        ...

def phy_mode(*args, **kwargs) -> Any: ...
def PPP(*args, **kwargs) -> Any: ...

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
      - *phy_clock* specifies, whether the data clock is provided by the Ethernet controller or the PYH interface.
        The default value is the one that matches the board. If set to ``True``, the clock is driven by the
        Ethernet controller, otherwise by the PHY interface.

    For example, with the Seeed Arch Mix board you can  use::

      nic = LAN(0, phy_type=LAN.PHY_LAN8720, phy_addr=2, phy_clock=False)
    """

    def __init__(self, id, *, phy_type=0, phy_addr=0, phy_clock=0) -> None: ...
    def active(self, state: Optional[Any] = None) -> Any:
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
    def status(self) -> Any:
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
    def config(self, config_parameters) -> Any:
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
