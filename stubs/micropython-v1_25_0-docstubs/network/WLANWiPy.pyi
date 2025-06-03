""" """

from __future__ import annotations
from _typeshed import Incomplete
from typing import Callable, overload, Any, List, Tuple
from typing_extensions import TypeVar, TypeAlias, Awaitable

class WLANWiPy:
    """
    .. note::

        This class is a non-standard WLAN implementation for the WiPy.
        It is available simply as ``network.WLAN`` on the WiPy but is named in the
        documentation below as ``network.WLANWiPy`` to distinguish it from the
        more general :ref:`network.WLAN <network.WLAN>` class.

    This class provides a driver for the WiFi network processor in the WiPy. Example usage::

        import network
        import time
        # setup as a station
        wlan = network.WLAN(mode=WLAN.STA)
        wlan.connect('your-ssid', auth=(WLAN.WPA2, 'your-key'))
        while not wlan.isconnected():
            time.sleep_ms(50)
        print(wlan.ifconfig())

        # now use socket as usual
        ...
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

    def init(
        self,
        mode: int,
        /,
        *,
        ssid: str,
        auth: tuple[str, str],
        channel: int,
        antenna: int,
    ) -> bool:
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

    def connect(
        self,
        ssid: str,
        /,
        *,
        auth: tuple[str, str] | None = None,
        bssid: bytes | None = None,
        timeout: int | None = None,
    ) -> None:
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

    def irq(self, *, handler: Callable[[], None], wake: int) -> Any:
        """
        Create a callback to be triggered when a WLAN event occurs during ``machine.SLEEP``
        mode. Events are triggered by socket activity or by WLAN connection/disconnection.

            - *handler* is the function that gets called when the IRQ is triggered.
            - *wake* must be ``machine.SLEEP``.

        Returns an IRQ object.
        """
        ...
