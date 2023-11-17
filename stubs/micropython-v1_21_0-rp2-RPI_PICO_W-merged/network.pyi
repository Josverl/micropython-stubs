"""
Network configuration.

MicroPython module: https://docs.micropython.org/en/v1.21.0/library/network.html

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
from _typeshed import Incomplete, Incomplete as Incomplete
from typing import Any, List, Optional, Tuple, Union

STA_IF: int
STAT_IDLE: int
STAT_NO_AP_FOUND: int
STAT_WRONG_PASSWORD: int
STAT_GOT_IP: int
AP_IF: int
STAT_CONNECTING: int
STAT_CONNECT_FAIL: int

def route(*args, **kwargs) -> Incomplete: ...
def hostname(*args, **kwargs) -> Incomplete: ...
def country(*args, **kwargs) -> Incomplete: ...

class WLAN:
    """
    Create a WLAN network interface object. Supported interfaces are
    ``network.STA_IF`` (station aka client, connects to upstream WiFi access
    points) and ``network.AP_IF`` (access point, allows other WiFi clients to
    connect). Availability of the methods below depends on interface type.
    For example, only STA interface may `WLAN.connect()` to an access point.
    """

    PM_PERFORMANCE: int
    PM_POWERSAVE: int
    PM_NONE: int
    def isconnected(self) -> bool:
        """
        In case of STA mode, returns ``True`` if connected to a WiFi access
        point and has a valid IP address.  In AP mode returns ``True`` when a
        station is connected. Returns ``False`` otherwise.
        """
        ...
    def ioctl(self, *args, **kwargs) -> Incomplete: ...
    def ifconfig(self, configtuple: Optional[Any] = None) -> Tuple:
        """
        Get/set IP-level network interface parameters: IP address, subnet mask,
        gateway and DNS server. When called with no arguments, this method returns
        a 4-tuple with the above information. To set the above values, pass a
        4-tuple with the required information.  For example::

         nic.ifconfig(('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
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
    def send_ethernet(self, *args, **kwargs) -> Incomplete: ...
    def status(self, param: Optional[Any] = None) -> Incomplete:
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
    def config(self, *args, **kwargs) -> Incomplete:
        """
        Get or set general network interface parameters. These methods allow to work
        with additional parameters beyond standard IP configuration (as dealt with by
        `WLAN.ifconfig()`). These include network-specific and hardware-specific
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
        channel        WiFi channel (integer)
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
    def active(self, is_active: Optional[Any] = None) -> None:
        """
        Activate ("up") or deactivate ("down") network interface, if boolean
        argument is passed. Otherwise, query current state if no argument is
        provided. Most other methods require active interface.
        """
        ...
    def disconnect(self) -> None:
        """
        Disconnect from the currently connected wireless network.
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
    def deinit(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, interface_id) -> None: ...
