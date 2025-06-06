"""
Network configuration.

MicroPython module: https://docs.micropython.org/en/v1.26.0/library/network.html

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
    print(nic.ipconfig("addr4"))

    # now use socket as usual
    import socket
    addr = socket.getaddrinfo('micropython.org', 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(b'GET / HTTP/1.1
Host: micropython.org

')
    data = s.recv(1000)
    s.close()

---
Module: 'network' on micropython-v1.25.0-esp32-ESP32_GENERIC_S2
"""

# MCU: {'version': '1.25.0', 'mpy': 'v6.3', 'port': 'esp32', 'board': 'ESP32_GENERIC_S2', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': '1.25.0', 'cpu': 'ESP32S2'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Protocol, List, Any, Optional, Tuple, Final
from _typeshed import Incomplete
from typing_extensions import Awaitable, TypeAlias, TypeVar

PHY_KSZ8851SNL: Final[int] = 100
STAT_NO_AP_FOUND_W_COMPATIBLE_SECURITY: Final[int] = 210
PHY_KSZ8081: Final[int] = 6
PHY_RTL8201: Final[int] = 3
PHY_LAN8710: Final[int] = 0
PHY_LAN8720: Final[int] = 1
MODE_LR: Final[int] = 8
PHY_KSZ8041: Final[int] = 5
MODE_11N: Final[int] = 4
PHY_IP101: Final[int] = 2
PHY_DM9051: Final[int] = 101
PHY_DP83848: Final[int] = 4
STAT_IDLE: Final[int] = 1000
PHY_W5500: Final[int] = 102
STAT_HANDSHAKE_TIMEOUT: Final[int] = 204
STAT_NO_AP_FOUND_IN_RSSI_THRESHOLD: Final[int] = 212
STAT_NO_AP_FOUND: Final[int] = 201
STAT_NO_AP_FOUND_IN_AUTHMODE_THRESHOLD: Final[int] = 211
STAT_ASSOC_FAIL: Final[int] = 203
STAT_GOT_IP: Final[int] = 1010
STAT_WRONG_PASSWORD: Final[int] = 202
STAT_CONNECT_FAIL: Final[int] = 203
STAT_BEACON_TIMEOUT: Final[int] = 200
STAT_CONNECTING: Final[int] = 1001
AUTH_WPA2_PSK: Final[int] = 3
MODE_11G: Final[int] = 2
AUTH_WPA2_ENTERPRISE: Final[int] = 5
AUTH_WPA3_EXT_PSK: Final[int] = 11
AUTH_WPA2_WPA3_PSK: Final[int] = 7
AUTH_WPA3_ENT_192: Final[int] = 10
AUTH_MAX: Final[int] = 13
AUTH_WEP: Final[int] = 1
AP_IF: Final[int] = 1
AUTH_WAPI_PSK: Final[int] = 8
AUTH_OPEN: Final[int] = 0
AUTH_OWE: Final[int] = 9
ETH_STARTED: Final[int] = 1
AUTH_WPA3_EXT_PSK_MIXED_MODE: Final[int] = 12
ETH_INITIALIZED: Final[int] = 0
MODE_11B: Final[int] = 1
ETH_STOPPED: Final[int] = 2
STA_IF: Final[int] = 0
AUTH_WPA_PSK: Final[int] = 2
ETH_GOT_IP: Final[int] = 5
AUTH_WPA3_PSK: Final[int] = 6
ETH_DISCONNECTED: Final[int] = 4
AUTH_WPA_WPA2_PSK: Final[int] = 4
ETH_CONNECTED: Final[int] = 3

def country(*args, **kwargs) -> Incomplete: ...
def hostname(*args, **kwargs) -> Incomplete: ...
def ipconfig(*args, **kwargs) -> Incomplete: ...
def phy_mode(*args, **kwargs) -> Incomplete: ...

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
        the PHY interface.
        The default value is the one that matches the board. If set to ``LAN.OUT`` or ``Pin.OUT``
        or ``True``, the clock is driven by the Ethernet controller, if set to ``LAN.IN``
        or ``Pin.IN`` or ``False``, the clock is driven by the PHY interface.

    For example, with the Seeed Arch Mix board you can  use::

      nic = LAN(0, phy_type=LAN.PHY_LAN8720, phy_addr=1, ref_clk_mode=Pin.IN)

    ``Note:`` On esp32 port the constructor requires different arguments. See
              :ref:`esp32 port reference <esp32_network_lan>`.
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

class PPP:
    """
    Create a PPP driver object.

    Arguments are:

      - *stream* is any object that supports the stream protocol, but is most commonly a
        :class:`machine.UART` instance.  This stream object must have an ``irq()`` method
        and an ``IRQ_RXIDLE`` constant, for use by `PPP.connect`.
    """

    SEC_NONE: Incomplete
    """The type of connection security."""
    SEC_PAP: Incomplete
    """The type of connection security."""
    SEC_CHAP: Incomplete
    """The type of connection security."""
    def __init__(self, stream) -> None: ...
    def connect(self, security=SEC_NONE, user=None, key=None) -> Incomplete:
        """
        Initiate a PPP connection with the given parameters:

          - *security* is the type of security, either ``PPP.SEC_NONE``, ``PPP.SEC_PAP``,
            or ``PPP.SEC_CHAP``.
          - *user* is an optional user name to use with the security mode.
          - *key* is an optional password to use with the security mode.

        When this method is called the underlying stream has its interrupt configured to call
        `PPP.poll` via ``stream.irq(ppp.poll, stream.IRQ_RXIDLE)``.  This makes sure the
        stream is polled, and data passed up the PPP stack, wheverver data becomes available
        on the stream.

        The connection proceeds asynchronously, in the background.
        """
        ...

    def disconnect(self) -> Incomplete:
        """
        Terminate the connection.  This must be called to cleanly close the PPP connection.
        """
        ...

    def isconnected(self) -> bool:
        """
        Returns ``True`` if the PPP link is connected and up.
        Returns ``False`` otherwise.
        """
        ...

    def status(self) -> Incomplete:
        """
        Returns the PPP status.
        """
        ...

    def config(self, config_parameters) -> Incomplete:
        """
        Sets or gets parameters of the PPP interface. The only parameter that can be
        retrieved and set is the underlying stream, using::

           stream = PPP.config("stream")
           PPP.config(stream=stream)
        """
        ...

    def ipconfig(self, param) -> Incomplete:
        """
        See `AbstractNIC.ipconfig`.
        """
        ...

    def ifconfig(self, configtuple: Optional[Any] = None) -> Incomplete:
        """
        See `AbstractNIC.ifconfig`.
        """
        ...

    def poll(self) -> Incomplete:
        """
        Poll the underlying stream for data, and pass it up the PPP stack.
        This is called automatically if the stream is a UART with a RXIDLE interrupt,
        so it's not usually necessary to call it manually.
        """
        ...

class WLAN:
    """
    Create a WLAN network interface object. Supported interfaces are
    ``network.WLAN.IF_STA`` (station aka client, connects to upstream WiFi access
    points) and ``network.WLAN.IF_AP`` (access point, allows other WiFi clients to
    connect). Availability of the methods below depends on interface type.
    For example, only STA interface may `WLAN.connect()` to an access point.
    """

    SEC_WPA2_WPA3: Final[int] = 7
    SEC_WPA2_ENT: Final[int] = 5
    SEC_WPA2: Final[int] = 3
    SEC_WPA: Final[int] = 2
    SEC_WPA_WPA2: Final[int] = 4
    SEC_WPA3: Final[int] = 6
    SEC_WPA3_EXT_PSK_MIXED_MODE: Final[int] = 12
    SEC_WPA3_EXT_PSK: Final[int] = 11
    SEC_WPA3_ENT_192: Final[int] = 10
    PM_PERFORMANCE: Final[int] = 1
    PM_NONE: Final[int] = 0
    IF_STA: Final[int] = 0
    IF_AP: Final[int] = 1
    SEC_WEP: Final[int] = 1
    PM_POWERSAVE: Final[int] = 2
    SEC_WAPI: Final[int] = 8
    SEC_OWE: Final[int] = 9
    SEC_OPEN: Final[int] = 0
    def ifconfig(self, configtuple: Optional[Any] = None) -> Tuple:
        """
        Get/set IP-level network interface parameters: IP address, subnet mask,
        gateway and DNS server. When called with no arguments, this method returns
        a 4-tuple with the above information. To set the above values, pass a
        4-tuple with the required information.  For example::

         nic.ifconfig(('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
        """
        ...

    def ipconfig(self, *args, **kwargs) -> Incomplete: ...
    def isconnected(self) -> bool:
        """
        In case of STA mode, returns ``True`` if connected to a WiFi access
        point and has a valid IP address.  In AP mode returns ``True`` when a
        station is connected. Returns ``False`` otherwise.
        """
        ...

    def scan(self) -> List[Tuple]:
        """
        Scan for the available wireless networks.
        Hidden networks -- where the SSID is not broadcast -- will also be scanned
        if the WLAN interface allows it.

        Scanning is only possible on STA interface. Returns list of tuples with
        the information about WiFi access points:

            (ssid, bssid, channel, RSSI, security, hidden)

        *bssid* is hardware address of an access point, in binary form, returned as
        bytes object. You can use `binascii.hexlify()` to convert it to ASCII form.

        There are five values for security:

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

    def status(self, param: Optional[Any] = None) -> List[int]:
        """
        Return the current status of the wireless connection.

        When called with no argument the return value describes the network link status.
        The possible statuses are defined as constants in the :mod:`network` module:

            * ``STAT_IDLE`` -- no connection and no activity,
            * ``STAT_CONNECTING`` -- connecting in progress,
            * ``STAT_WRONG_PASSWORD`` -- failed due to incorrect password,
            * ``STAT_NO_AP_FOUND`` -- failed because no access point replied,
            * ``STAT_CONNECT_FAIL`` -- failed due to other problems,
            * ``STAT_GOT_IP`` -- connection successful.

        When called with one argument *param* should be a string naming the status
        parameter to retrieve, and different parameters are supported depending on the
        mode the WiFi is in.

        In STA mode, passing ``'rssi'`` returns a signal strength indicator value, whose
        format varies depending on the port (this is available on all ports that support
        WiFi network interfaces, except for CC3200).

        In AP mode, passing ``'stations'`` returns a list of connected WiFi stations
        (this is available on all ports that support WiFi network interfaces, except for
        CC3200).  The format of the station information entries varies across ports,
        providing either the raw BSSID of the connected station, the IP address of the
        connected station, or both.
        """
        ...

    def disconnect(self) -> None:
        """
        Disconnect from the currently connected wireless network.
        """
        ...

    def active(self, is_active: Optional[Any] = None) -> None:
        """
        Activate ("up") or deactivate ("down") network interface, if boolean
        argument is passed. Otherwise, query current state if no argument is
        provided. Most other methods require active interface.
        """
        ...

    def config(self, *args, **kwargs) -> Incomplete:
        """
        Get or set general network interface parameters. These methods allow to work
        with additional parameters beyond standard IP configuration (as dealt with by
        `AbstractNIC.ipconfig()`). These include network-specific and hardware-specific
        parameters. For setting parameters, keyword argument syntax should be used,
        multiple parameters can be set at once. For querying, parameters name should
        be quoted as a string, and only one parameter can be queries at time::

         # Set WiFi access point name (formally known as SSID) and WiFi channel
         ap.config(ssid='My AP', channel=11)
         # Query params one by one
         print(ap.config('ssid'))
         print(ap.config('channel'))

        Following are commonly supported parameters (availability of a specific parameter
        depends on network technology type, driver, and :term:`MicroPython port`).

        =============  ===========
        Parameter      Description
        =============  ===========
        mac            MAC address (bytes)
        ssid           WiFi access point name (string)
        channel        WiFi channel (integer). Depending on the port this may only be supported on the AP interface.
        hidden         Whether SSID is hidden (boolean)
        security       Security protocol supported (enumeration, see module constants)
        key            Access key (string)
        hostname       The hostname that will be sent to DHCP (STA interfaces) and mDNS (if supported, both STA and AP). (Deprecated, use :func:`network.hostname` instead)
        reconnects     Number of reconnect attempts to make (integer, 0=none, -1=unlimited)
        txpower        Maximum transmit power in dBm (integer or float)
        pm             WiFi Power Management setting (see below for allowed values)
        =============  ===========
        """
        ...

    def connect(self, ssid=None, key=None, *, bssid=None) -> None:
        """
        Connect to the specified wireless network, using the specified key.
        If *bssid* is given then the connection will be restricted to the
        access-point with that MAC address (the *ssid* must also be specified
        in this case).
        """
        ...

    def __init__(self, interface_id) -> None: ...
