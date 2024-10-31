""" """

from __future__ import annotations
from typing import Any, List, Optional, Tuple, Union
from _typeshed import Incomplete

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

    def ifconfig(self, if_id=0, config: Union[str, Tuple] = "dhcp") -> Tuple:
        """
        With no parameters given returns a 4-tuple of *(ip, subnet_mask, gateway, DNS_server)*.

        if ``'dhcp'`` is passed as a parameter then the DHCP client is enabled and the IP params
        are negotiated with the AP.

        If the 4-tuple config is given then a static IP is configured. For instance::

           wlan.ifconfig(config=('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
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
