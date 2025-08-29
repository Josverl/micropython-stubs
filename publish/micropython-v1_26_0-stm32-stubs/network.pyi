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
Module: 'network' on micropython-v1.26.0-stm32-PYBV11-NETWORK
"""

# MCU: {'variant': 'NETWORK', 'build': '', 'arch': 'armv7emsp', 'port': 'stm32', 'board': 'PYBV11', 'board_id': 'PYBV11-NETWORK', 'mpy': 'v6.3', 'ver': '1.26.0', 'family': 'micropython', 'cpu': 'STM32F405RG', 'version': '1.26.0'}
# Stubber: v1.26.0
from __future__ import annotations
from typing import Optional, Protocol, Callable, List, Any, Tuple, overload, Final
from _typeshed import Incomplete
from typing_extensions import Awaitable, TypeAlias, TypeVar
from machine import Pin, SPI
from abc import abstractmethod

STA_IF: Final[int] = 0
AP_IF: Final[int] = 1

def route(*args, **kwargs) -> Incomplete: ...
def hostname(name: Optional[Any] = None) -> Incomplete:
    """
    Get or set the hostname that will identify this device on the network. It will
    be used by all interfaces.

    This hostname is used for:
     * Sending to the DHCP server in the client request. (If using DHCP)
     * Broadcasting via mDNS. (If enabled)

    If the *name* parameter is provided, the hostname will be set to this value.
    If the function is called without parameters, it returns the current
    hostname.

    A change in hostname is typically only applied during connection. For DHCP
    this is because the hostname is part of the DHCP client request, and the
    implementation of mDNS in most ports only initialises the hostname once
    during connection. For this reason, you must set the hostname before
    activating/connecting your network interfaces.

    The length of the hostname is limited to 32 characters.
    :term:`MicroPython ports <MicroPython port>` may choose to set a lower
    limit for memory reasons. If the given name does not fit, a `ValueError`
    is raised.

    The default hostname is typically the name of the board.
    """
    ...

def country(code: Optional[Any] = None) -> Incomplete:
    """
    Get or set the two-letter ISO 3166-1 Alpha-2 country code to be used for
    radio compliance.

    If the *code* parameter is provided, the country will be set to this value.
    If the function is called without parameters, it returns the current
    country.

    The default code ``"XX"`` represents the "worldwide" region.
    """
    ...

class WIZNET5K:
    """
    This class allows you to control WIZnet5x00 Ethernet adaptors based on
    the W5200 and W5500 chipsets.  The particular chipset that is supported
    by the firmware is selected at compile-time via the MICROPY_PY_WIZNET5K
    option.

    Example usage::

        import network
        nic = network.WIZNET5K(SPI(1), Pin.board.X5, Pin.board.X4)
        print(nic.ifconfig())

        # now use socket as usual
        ...

    For this example to work the WIZnet5x00 module must have the following connections:

        - MOSI connected to X8
        - MISO connected to X7
        - SCLK connected to X6
        - nSS connected to X5
        - nRESET connected to X4

    It is possible to use other SPI buses and other pins for nSS and nRESET.
    """

    def isconnected(self, *args, **kwargs) -> Incomplete: ...
    def status(self, *args, **kwargs) -> Incomplete: ...
    def regs(self) -> Any:
        """
        Dump the WIZnet5x00 registers.  Useful for debugging.
        """
        ...

    def active(self, *args, **kwargs) -> Incomplete: ...
    def ifconfig(self, *args, **kwargs) -> Incomplete: ...
    def config(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, spi: SPI, pin_cs: Pin, pin_rst: Pin, /) -> None:
        """
        Create a WIZNET5K driver object, initialise the WIZnet5x00 module using the given
        SPI bus and pins, and return the WIZNET5K object.

        Arguments are:

          - *spi* is an :ref:`SPI object <SPI>` which is the SPI bus that the WIZnet5x00 is
            connected to (the MOSI, MISO and SCLK pins).
          - *pin_cs* is a :ref:`Pin object <Pin>` which is connected to the WIZnet5x00 nSS pin.
          - *pin_rst* is a :ref:`Pin object <Pin>` which is connected to the WIZnet5x00 nRESET pin.

        All of these objects will be initialised by the driver, so there is no need to
        initialise them yourself.  For example, you can use::

          nic = network.WIZNET5K(SPI(1), Pin.board.X5, Pin.board.X4)
        """

class LAN:
    @overload
    def active(self, /) -> bool:
        """
        With a parameter, it sets the interface active if *state* is true, otherwise it
        sets it inactive.
        Without a parameter, it returns the state.
        """

    @overload
    def active(self, is_active: bool | int, /) -> None:
        """
        With a parameter, it sets the interface active if *state* is true, otherwise it
        sets it inactive.
        Without a parameter, it returns the state.
        """

class WLAN:
    @overload
    def active(self, /) -> bool:
        """
        Activate ("up") or deactivate ("down") network interface, if boolean
        argument is passed. Otherwise, query current state if no argument is
        provided. Most other methods require active interface.
        """

    @overload
    def active(self, is_active: bool | int, /) -> None:
        """
        Activate ("up") or deactivate ("down") network interface, if boolean
        argument is passed. Otherwise, query current state if no argument is
        provided. Most other methods require active interface.
        """

    @overload
    def status(self) -> int:
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

    @overload
    def status(self, param: str, /) -> int:
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

    @overload
    def ifconfig(self) -> tuple[str, str, str, str]:
        """
        Get/set IP-level network interface parameters: IP address, subnet mask,
        gateway and DNS server. When called with no arguments, this method returns
        a 4-tuple with the above information. To set the above values, pass a
        4-tuple with the required information.  For example::

         nic.ifconfig(('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
        """

    @overload
    def ifconfig(self, ip_mask_gateway_dns: tuple[str, str, str, str], /) -> None:
        """
        Get/set IP-level network interface parameters: IP address, subnet mask,
        gateway and DNS server. When called with no arguments, this method returns
        a 4-tuple with the above information. To set the above values, pass a
        4-tuple with the required information.  For example::

         nic.ifconfig(('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
        """

    @overload
    def config(self, param: str, /) -> Any:
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

    @overload
    def config(self, **kwargs: Any) -> None:
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

class WLANWiPy:
    @overload
    def __init__(self, id: int = 0, /):
        """
        Create a WLAN object, and optionally configure it. See `init()` for params of configuration.

        .. note::

        The ``WLAN`` constructor is special in the sense that if no arguments besides the id are given,
        it will return the already existing ``WLAN`` instance without re-configuring it. This is
        because ``WLAN`` is a system feature of the WiPy. If the already existing instance is not
        initialized it will do the same as the other constructors an will initialize it with default
        values.
        """

    @overload
    def __init__(
        self,
        id: int,
        /,
        *,
        mode: int,
        ssid: str,
        auth: tuple[str, str],
        channel: int,
        antenna: int,
    ):
        """
        Create a WLAN object, and optionally configure it. See `init()` for params of configuration.

        .. note::

        The ``WLAN`` constructor is special in the sense that if no arguments besides the id are given,
        it will return the already existing ``WLAN`` instance without re-configuring it. This is
        because ``WLAN`` is a system feature of the WiPy. If the already existing instance is not
        initialized it will do the same as the other constructors an will initialize it with default
        values.
        """

    @overload
    def mode(self) -> int:
        """
        Get or set the WLAN mode.
        """

    @overload
    def mode(self, mode: int, /) -> None:
        """
        Get or set the WLAN mode.
        """

    @overload
    def ssid(self) -> str:
        """
        Get or set the SSID when in AP mode.
        """

    @overload
    def ssid(self, ssid: str, /) -> None:
        """
        Get or set the SSID when in AP mode.
        """

    @overload
    def auth(self) -> int:
        """
        Get or set the authentication type when in AP mode.
        """

    @overload
    def auth(self, auth: int, /) -> None:
        """
        Get or set the authentication type when in AP mode.
        """

    @overload
    def channel(self) -> int:
        """
        Get or set the channel (only applicable in AP mode).
        """

    @overload
    def channel(self, channel: int, /) -> None:
        """
        Get or set the channel (only applicable in AP mode).
        """

    @overload
    def antenna(self) -> int:
        """
        Get or set the antenna type (external or internal).
        """

    @overload
    def antenna(self, antenna: int, /) -> None:
        """
        Get or set the antenna type (external or internal).
        """

    @overload
    def mac(self) -> bytes:
        """
        Get or set a 6-byte long bytes object with the MAC address.
        """

    @overload
    def mac(self, mac: bytes, /) -> None:
        """
        Get or set a 6-byte long bytes object with the MAC address.
        """

class AbstractNIC:
    @overload
    @abstractmethod
    def active(self, /) -> bool:
        """
        Activate ("up") or deactivate ("down") the network interface, if
        a boolean argument is passed. Otherwise, query current state if
        no argument is provided. Most other methods require an active
        interface (behaviour of calling them on inactive interface is
        undefined).
        """

    @overload
    @abstractmethod
    def active(self, is_active: bool | int, /) -> None:
        """
        Activate ("up") or deactivate ("down") the network interface, if
        a boolean argument is passed. Otherwise, query current state if
        no argument is provided. Most other methods require an active
        interface (behaviour of calling them on inactive interface is
        undefined).
        """

    @overload
    @abstractmethod
    def connect(self, key: str | None = None, /, **kwargs: Any) -> None:
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

    @overload
    @abstractmethod
    def connect(self, service_id: Any, key: str | None = None, /, **kwargs: Any) -> None:
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

    @overload
    @abstractmethod
    def status(self) -> Any:
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

    @overload
    @abstractmethod
    def status(self, param: str, /) -> Any:
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

    @overload
    @abstractmethod
    def ifconfig(self) -> tuple[str, str, str, str]:
        """
        ``Note:`` This function is deprecated, use `ipconfig()` instead.

        Get/set IP-level network interface parameters: IP address, subnet mask,
        gateway and DNS server. When called with no arguments, this method returns
        a 4-tuple with the above information. To set the above values, pass a
        4-tuple with the required information.  For example::

         nic.ifconfig(('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
        """

    @overload
    @abstractmethod
    def ifconfig(self, ip_mask_gateway_dns: tuple[str, str, str, str], /) -> None:
        """
        ``Note:`` This function is deprecated, use `ipconfig()` instead.

        Get/set IP-level network interface parameters: IP address, subnet mask,
        gateway and DNS server. When called with no arguments, this method returns
        a 4-tuple with the above information. To set the above values, pass a
        4-tuple with the required information.  For example::

         nic.ifconfig(('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
        """

    @overload
    @abstractmethod
    def config(self, param: str, /) -> Any:
        """
        Get or set general network interface parameters. These methods allow to work
        with additional parameters beyond standard IP configuration (as dealt with by
        `ipconfig()`). These include network-specific and hardware-specific
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

    @overload
    @abstractmethod
    def config(self, **kwargs: Any) -> None:
        """
        Get or set general network interface parameters. These methods allow to work
        with additional parameters beyond standard IP configuration (as dealt with by
        `ipconfig()`). These include network-specific and hardware-specific
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
