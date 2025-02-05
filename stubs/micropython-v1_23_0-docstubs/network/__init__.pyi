"""
Network configuration.

MicroPython module: https://docs.micropython.org/en/v1.23.0/library/network.html

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

# source version: v1.23.0
# origin module:: repos/micropython/docs/library/network.rst
from __future__ import annotations
from _typeshed import Incomplete
from typing import Any, List, Optional, Tuple
from typing_extensions import TypeVar, TypeAlias, Awaitable
from typing import Protocol
from network.WLAN import WLAN
from network.WLANWiPy import WLANWiPy
from network.WIZNET5K import WIZNET5K
from network.LAN import LAN

class AbstractNIC(Protocol):
    """
    Instantiate a network interface object. Parameters are network interface
    dependent. If there are more than one interface of the same type, the first
    parameter should be `id`.
    """

    def __init__(self, id=None, *args, **kwargs) -> None: ...
    def active(self, is_active: Optional[Any] = None) -> None:
        """
        Activate ("up") or deactivate ("down") the network interface, if
        a boolean argument is passed. Otherwise, query current state if
        no argument is provided. Most other methods require an active
        interface (behaviour of calling them on inactive interface is
        undefined).
        """
        ...

    def connect(self, service_id: Optional[Any] = None, key: Optional[Any] = None, *args, **kwargs) -> None:
        """
        Connect the interface to a network. This method is optional, and
        available only for interfaces which are not "always connected".
        If no parameters are given, connect to the default (or the only)
        service. If a single parameter is given, it is the primary identifier
        of a service to connect to. It may be accompanied by a key
        (password) required to access said service. There can be further
        arbitrary keyword-only parameters, depending on the networking medium
        type and/or particular device. Parameters can be used to: a)
        specify alternative service identifier types; b) provide additional
        connection parameters. For various medium types, there are different
        sets of predefined/recommended parameters, among them:

        * WiFi: *bssid* keyword to connect to a specific BSSID (MAC address)
        """
        ...

    def disconnect(self) -> None:
        """
        Disconnect from network.
        """
        ...

    def isconnected(self) -> bool:
        """
        Returns ``True`` if connected to network, otherwise returns ``False``.
        """
        ...

    def scan(self, *args, **kwargs) -> List[Tuple]:
        """
        Scan for the available network services/connections. Returns a
        list of tuples with discovered service parameters. For various
        network media, there are different variants of predefined/
        recommended tuple formats, among them:

        * WiFi: (ssid, bssid, channel, RSSI, security, hidden). There
          may be further fields, specific to a particular device.

        The function may accept additional keyword arguments to filter scan
        results (e.g. scan for a particular service, on a particular channel,
        for services of a particular set, etc.), and to affect scan
        duration and other parameters. Where possible, parameter names
        should match those in connect().
        """
        ...

    def status(self, param: Optional[Any] = None) -> Incomplete:
        """
        Query dynamic status information of the interface.  When called with no
        argument the return value describes the network link status.  Otherwise
        *param* should be a string naming the particular status parameter to
        retrieve.

        The return types and values are dependent on the network
        medium/technology.  Some of the parameters that may be supported are:

        * WiFi STA: use ``'rssi'`` to retrieve the RSSI of the AP signal
        * WiFi AP: use ``'stations'`` to retrieve a list of all the STAs
          connected to the AP.  The list contains tuples of the form
          (MAC, RSSI).
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

    def config(self, param) -> Incomplete:
        """
        Get or set general network interface parameters. These methods allow to work
        with additional parameters beyond standard IP configuration (as dealt with by
        `ifconfig()`). These include network-specific and hardware-specific
        parameters. For setting parameters, the keyword argument
        syntax should be used, and multiple parameters can be set at once. For
        querying, a parameter name should be quoted as a string, and only one
        parameter can be queried at a time::

         # Set WiFi access point name (formally known as SSID) and WiFi channel
         ap.config(ssid='My AP', channel=11)
         # Query params one by one
         print(ap.config('ssid'))
         print(ap.config('channel'))
        """
        ...
