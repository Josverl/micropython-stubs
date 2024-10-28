"""
Network configuration.

MicroPython module: https://docs.micropython.org/en/v1.25.0-preview/library/network.html

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
    s.send(b'GET / HTTP/1.1\r\nHost: micropython.org\r\n\r\n')
    data = s.recv(1000)
    s.close()
"""

# source version: v1.25.0-preview
# origin module:: repos/micropython/docs/library/network.rst
# + module: network.WLAN.rst
# + module: network.WLANWiPy.rst
# + module: network.WIZNET5K.rst
# + module: network.LAN.rst
# + module: network.PPP.rst
from __future__ import annotations
from typing import Any, List, Optional, Tuple
from _typeshed import Incomplete

class AbstractNIC:
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

    def ipconfig(self, param) -> Incomplete:
        """
        Get or set interface-specific IP-configuration interface parameters.
        Supported parameters are the following (availability of a particular
        parameter depends on the port and the specific network interface):

        * ``dhcp4`` (``True/False``) obtain an IPv4 address, gateway and dns
          server via DHCP. This method does not block and wait for an address
          to be obtained. To check if an address was obtained, use the read-only
          property ``has_dhcp4``.
        * ``gw4`` Get/set the IPv4 default-gateway.
        * ``dhcp6`` (``True/False``) obtain a DNS server via stateless DHCPv6.
          Obtaining IP Addresses via DHCPv6 is currently not implemented.
        * ``autoconf6`` (``True/False``) obtain a stateless IPv6 address via
          the network prefix shared in router advertisements. To check if a
          stateless address was obtained, use the read-only
          property ``has_autoconf6``.
        * ``addr4`` (e.g. ``192.168.0.4/24``) obtain the current IPv4 address
          and network mask as ``(ip, subnet)``-tuple, regardless of how this
          address was obtained. This method can be used to set a static IPv4
          address either as ``(ip, subnet)``-tuple or in CIDR-notation.
        * ``addr6`` (e.g. ``fe80::1234:5678``) obtain a list of current IPv6
          addresses as ``(ip, state, preferred_lifetime, valid_lifetime)``-tuple.
          This include link-local, slaac and static addresses.
          ``preferred_lifetime`` and ``valid_lifetime`` represent the remaining
          valid and preferred lifetime of each IPv6 address, in seconds.
          ``state`` indicates the current state of the address:

          * ``0x08`` - ``0x0f`` indicates the address is tentative, counting the
            number of probes sent.
          * ``0x10`` The address is deprecated (but still valid)
          * ``0x30`` The address is preferred (and valid)
          * ``0x40`` The address is duplicated and can not be used.

          This method can be used to set a static IPv6
          address, by setting this parameter to the address, like ``fe80::1234:5678``.
        """
        ...

    def ifconfig(self, configtuple: Optional[Any] = None) -> Tuple:
        """
        ``Note:`` This function is deprecated, use `ipconfig()` instead.

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
        ...

class WLAN:
    """
    Create a WLAN network interface object. Supported interfaces are
    ``network.STA_IF`` (station aka client, connects to upstream WiFi access
    points) and ``network.AP_IF`` (access point, allows other WiFi clients to
    connect). Availability of the methods below depends on interface type.
    For example, only STA interface may `WLAN.connect()` to an access point.
    """

    PM_PERFORMANCE: Incomplete
    """\
    WLAN.PM_POWERSAVE
    WLAN.PM_NONE
    
    Allowed values for the ``WLAN.config(pm=...)`` network interface parameter:
    
    * ``PM_PERFORMANCE``: enable WiFi power management to balance power
    savings and WiFi performance
    * ``PM_POWERSAVE``: enable WiFi power management with additional power
    savings and reduced WiFi performance
    * ``PM_NONE``: disable wifi power management
    """
    def __init__(self, interface_id) -> None: ...
    def active(self, is_active: Optional[Any] = None) -> None:
        """
        Activate ("up") or deactivate ("down") network interface, if boolean
        argument is passed. Otherwise, query current state if no argument is
        provided. Most other methods require active interface.
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

class WLANWiPy:
    """
       Create a WLAN object, and optionally configure it. See `init()` for params of configuration.

    .. note::

       The ``WLAN`` constructor is special in the sense that if no arguments besides the id are given,
       it will return the already existing ``WLAN`` instance without re-configuring it. This is
       because ``WLAN`` is a system feature of the WiPy. If the already existing instance is not
       initialized it will do the same as the other constructors an will initialize it with default
       values.
    """

    STA: Incomplete
    AP: Incomplete
    """selects the WLAN mode"""
    WEP: Incomplete
    WPA: Incomplete
    WPA2: Incomplete
    """selects the network security"""
    INT_ANT: Incomplete
    EXT_ANT: Incomplete
    """selects the antenna type"""
    def __init__(self, id=0, *args, **kwargs) -> None: ...
    def init(self, mode, *, ssid, auth, channel, antenna) -> Incomplete:
        """
        Set or get the WiFi network processor configuration.

        Arguments are:

          - *mode* can be either ``WLAN.STA`` or ``WLAN.AP``.
          - *ssid* is a string with the ssid name. Only needed when mode is ``WLAN.AP``.
          - *auth* is a tuple with (sec, key). Security can be ``None``, ``WLAN.WEP``,
            ``WLAN.WPA`` or ``WLAN.WPA2``. The key is a string with the network password.
            If ``sec`` is ``WLAN.WEP`` the key must be a string representing hexadecimal
            values (e.g. 'ABC1DE45BF'). Only needed when mode is ``WLAN.AP``.
          - *channel* a number in the range 1-11. Only needed when mode is ``WLAN.AP``.
          - *antenna* selects between the internal and the external antenna. Can be either
            ``WLAN.INT_ANT`` or ``WLAN.EXT_ANT``.

        For example, you can do::

           # create and configure as an access point
           wlan.init(mode=WLAN.AP, ssid='wipy-wlan', auth=(WLAN.WPA2,'www.wipy.io'), channel=7, antenna=WLAN.INT_ANT)

        or::

           # configure as an station
           wlan.init(mode=WLAN.STA)
        """
        ...

    def connect(self, ssid, *, auth=None, bssid=None, timeout=None) -> None:
        """
        Connect to a WiFi access point using the given SSID, and other security
        parameters.

           - *auth* is a tuple with (sec, key). Security can be ``None``, ``WLAN.WEP``,
             ``WLAN.WPA`` or ``WLAN.WPA2``. The key is a string with the network password.
             If ``sec`` is ``WLAN.WEP`` the key must be a string representing hexadecimal
             values (e.g. 'ABC1DE45BF').
           - *bssid* is the MAC address of the AP to connect to. Useful when there are several
             APs with the same ssid.
           - *timeout* is the maximum time in milliseconds to wait for the connection to succeed.
        """
        ...

    def scan(self) -> List[Tuple]:
        """
        Performs a network scan and returns a list of named tuples with (ssid, bssid, sec, channel, rssi).
        Note that channel is always ``None`` since this info is not provided by the WiPy.
        """
        ...

    def disconnect(self) -> None:
        """
        Disconnect from the WiFi access point.
        """
        ...

    def isconnected(self) -> bool:
        """
        In case of STA mode, returns ``True`` if connected to a WiFi access point and has a valid IP address.
        In AP mode returns ``True`` when a station is connected, ``False`` otherwise.
        """
        ...

    def ipconfig(self, param) -> Incomplete:
        """
        See :meth:`AbstractNIC.ipconfig <AbstractNIC.ipconfig>`. Supported parameters are: ``dhcp4``, ``addr4``, ``gw4``.
        """
        ...

    def mode(self, mode: Optional[Any] = None) -> Incomplete:
        """
        Get or set the WLAN mode.
        """
        ...

    def ssid(self, ssid: Optional[Any] = None) -> Incomplete:
        """
        Get or set the SSID when in AP mode.
        """
        ...

    def auth(self, auth: Optional[Any] = None) -> Incomplete:
        """
        Get or set the authentication type when in AP mode.
        """
        ...

    def channel(self, channel: Optional[Any] = None) -> Incomplete:
        """
        Get or set the channel (only applicable in AP mode).
        """
        ...

    def antenna(self, antenna: Optional[Any] = None) -> Incomplete:
        """
        Get or set the antenna type (external or internal).
        """
        ...

    def mac(self, mac_addr: Optional[Any] = None) -> bytes:
        """
        Get or set a 6-byte long bytes object with the MAC address.
        """
        ...

    def irq(self, *, handler, wake) -> Incomplete:
        """
        Create a callback to be triggered when a WLAN event occurs during ``machine.SLEEP``
        mode. Events are triggered by socket activity or by WLAN connection/disconnection.

            - *handler* is the function that gets called when the IRQ is triggered.
            - *wake* must be ``machine.SLEEP``.

        Returns an IRQ object.
        """
        ...

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
    def regs(self) -> Incomplete:
        """
        Dump the WIZnet5x00 registers.  Useful for debugging.
        """
        ...

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
        Sets or gets parameters of the PPP interface. There are currently no parameter that
        can be set or retrieved.
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
