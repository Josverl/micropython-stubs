"""
Network configuration.

MicroPython module: https://docs.micropython.org/en/v1.25.0/library/network.html

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
Module: 'network' on micropython-v1.25.0-esp8266-ESP8266_GENERIC-FLASH_2M_ROMFS
"""

# MCU: {'variant': 'FLASH_2M_ROMFS', 'build': '', 'arch': 'xtensa', 'port': 'esp8266', 'board': 'ESP8266_GENERIC', 'board_id': 'ESP8266_GENERIC-FLASH_2M_ROMFS', 'mpy': 'v6.3', 'ver': '1.25.0', 'family': 'micropython', 'cpu': 'ESP8266', 'version': '1.25.0'}
# Stubber: v1.25.0
from __future__ import annotations
from typing import Protocol, List, Any, Optional, Tuple, Final
from _typeshed import Incomplete
from typing_extensions import Awaitable, TypeAlias, TypeVar

STA_IF: Final[int] = 0
STAT_CONNECT_FAIL: Final[int] = 4
STAT_CONNECTING: Final[int] = 1
MODE_11N: Final[int] = 3
STAT_GOT_IP: Final[int] = 5
STAT_WRONG_PASSWORD: Final[int] = 2
STAT_NO_AP_FOUND: Final[int] = 3
STAT_IDLE: Final[int] = 0
MODE_11G: Final[int] = 2
AUTH_WEP: Final[int] = 1
AUTH_OPEN: Final[int] = 0
AP_IF: Final[int] = 1
AUTH_WPA2_PSK: Final[int] = 3
MODE_11B: Final[int] = 1
AUTH_WPA_WPA2_PSK: Final[int] = 4
AUTH_WPA_PSK: Final[int] = 2

def hostname(*args, **kwargs) -> Incomplete: ...
def ipconfig(*args, **kwargs) -> Incomplete: ...
def phy_mode(*args, **kwargs) -> Incomplete: ...
def country(*args, **kwargs) -> Incomplete: ...

class WLAN:
    """
    Create a WLAN network interface object. Supported interfaces are
    ``network.WLAN.IF_STA`` (station aka client, connects to upstream WiFi access
    points) and ``network.WLAN.IF_AP`` (access point, allows other WiFi clients to
    connect). Availability of the methods below depends on interface type.
    For example, only STA interface may `WLAN.connect()` to an access point.
    """

    SEC_WEP: Final[int] = 1
    SEC_OPEN: Final[int] = 0
    SEC_WPA_WPA2: Final[int] = 4
    SEC_WPA: Final[int] = 2
    SEC_WPA2: Final[int] = 3
    IF_STA: Final[int] = 0
    IF_AP: Final[int] = 1
    PM_POWERSAVE: Final[int] = 1
    PM_NONE: Final[int] = 0
    PM_PERFORMANCE: Final[int] = 2
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
