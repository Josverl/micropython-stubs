"""
ESP-NOW :doc:`asyncio` support.

MicroPython module: https://docs.micropython.org/en/v1.28.0/library/aioespnow.html

---
Module: '_espnow' on micropython-v1.28.0-esp32-ESP32_GENERIC_C3
"""

# MCU: {'variant': '', 'build': '', 'arch': 'rv32imc', 'port': 'esp32', 'board': 'ESP32_GENERIC_C3', 'board_id': 'ESP32_GENERIC_C3', 'mpy': 'v6.3', 'ver': '1.28.0', 'family': 'micropython', 'cpu': 'ESP32C3', 'version': '1.28.0'}
# Stubber: v1.28.0
from __future__ import annotations

from typing import Any, Callable, Dict, Final, Iterator, List, Literal, Optional, Tuple, Union, overload

from _mpy_shed import mp_available
from _typeshed import Incomplete
from typing_extensions import Awaitable, Buffer, TypeAlias, TypeVar

RATE_LORA_500K: Final[int] = 42
"""See  `espnow-long-range`."""
RATE_2M: Final[int] = 1
"""\
Unless using the two proprietary long range data rates, only the sender must
configure the data rate.
"""
RATE_24M: Final[int] = 9
"""\
Unless using the two proprietary long range data rates, only the sender must
configure the data rate.
"""
RATE_1M: Final[int] = 0
"""\
Unless using the two proprietary long range data rates, only the sender must
configure the data rate.
"""
RATE_54M: Final[int] = 12
"""\
Unless using the two proprietary long range data rates, only the sender must
configure the data rate.
"""
RATE_LORA_250K: Final[int] = 41
"""See  `espnow-long-range`."""
RATE_6M: Final[int] = 11
"""\
Unless using the two proprietary long range data rates, only the sender must
configure the data rate.
"""
RATE_5M: Final[int] = 2
"""\
Unless using the two proprietary long range data rates, only the sender must
configure the data rate.
"""
KEY_LEN: Final[int] = 16
"""\
The following constants correspond to different transmit data rates on ESP32
only. Lower data rates are generally more reliable over long distances:
"""
MAX_DATA_LEN: Final[int] = 250
"""\
The following constants correspond to different transmit data rates on ESP32
only. Lower data rates are generally more reliable over long distances:
"""
ADDR_LEN: Final[int] = 6
"""\
The following constants correspond to different transmit data rates on ESP32
only. Lower data rates are generally more reliable over long distances:
"""
RATE_12M: Final[int] = 10
"""\
Unless using the two proprietary long range data rates, only the sender must
configure the data rate.
"""
MAX_ENCRYPT_PEER_NUM: Final[int] = 6
"""\
The following constants correspond to different transmit data rates on ESP32
only. Lower data rates are generally more reliable over long distances:
"""
RATE_11M: Final[int] = 3
"""\
Unless using the two proprietary long range data rates, only the sender must
configure the data rate.
"""
MAX_TOTAL_PEER_NUM: Final[int] = 20
"""\
The following constants correspond to different transmit data rates on ESP32
only. Lower data rates are generally more reliable over long distances:
"""
_MACAddress: TypeAlias = bytes
_PeerInfo: TypeAlias = Tuple[_MACAddress, bytes, int, int, bool]

class ESPNowBase:
    def irq(self, *args, **kwargs) -> Incomplete: ...
    def mod_peer(self, *args, **kwargs) -> Incomplete: ...
    def get_peers(self, *args, **kwargs) -> Incomplete: ...
    def stats(self, *args, **kwargs) -> Incomplete: ...
    def set_pmk(self, *args, **kwargs) -> Incomplete: ...
    def peer_count(self, *args, **kwargs) -> Incomplete: ...
    def recvinto(self, *args, **kwargs) -> Incomplete: ...
    @overload
    def send(self, msg: Union[str, bytes, bytearray, Buffer], /) -> bool: ...
    @overload
    def send(
        self, peer_addr: Optional[Union[bytes, bytearray]], msg: Union[str, bytes, bytearray, Buffer], sync: bool = True, /
    ) -> bool: ...
    def active(self, *args, **kwargs) -> Incomplete: ...
    def any(self, *args, **kwargs) -> Incomplete: ...
    def get_peer(self, *args, **kwargs) -> Incomplete: ...
    def del_peer(self, *args, **kwargs) -> Incomplete: ...
    def add_peer(self, *args, **kwargs) -> Incomplete: ...
    @overload
    def config(self, /, *, rxbuf: int = ..., timeout_ms: int = ..., rate: int = ...) -> None: ...
    @overload
    def config(self, param: Literal["rxbuf", "timeout_ms"], /) -> int: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class ESPNow:
    @overload
    def config(self, /, *, rxbuf: int = ..., timeout_ms: int = ..., rate: int = ...) -> None: ...
    @overload
    def config(self, param: str, /) -> int:
        """
        Set or get configuration values of the ESPNow interface. To set values, use
        the keyword syntax, and one or more parameters can be set at a time. To get
        a value the parameter name should be quoted as a string, and just one
        parameter is queried at a time.

        **Note:** *Getting* parameters is not supported on the ESP8266.

        Options:

            *rxbuf*: (default=526) Get/set the size in bytes of the internal
            buffer used to store incoming ESPNow packet data. The default size is
            selected to fit two max-sized ESPNow packets (250 bytes) with associated
            mac_address (6 bytes), a message byte count (1 byte) and RSSI data plus
            buffer overhead. Increase this if you expect to receive a lot of large
            packets or expect bursty incoming traffic.

            **Note:** The recv buffer is allocated by `ESPNow.active()`. Changing
            this value will have no effect until the next call of
            `ESPNow.active(True)<ESPNow.active()>`.

            *timeout_ms*: (default=300,000) Default timeout (in milliseconds)
            for receiving ESPNow messages. If *timeout_ms* is less than zero, then
            wait forever. The timeout can also be provided as arg to
            `recv()`/`irecv()`/`recvinto()`.

            *rate*: (ESP32 only) Set the transmission data rate for ESPNow packets.
            The default setting is `espnow.RATE_1M`. It's recommended to use one of
            the other ``espnow.RATE_nnn`` constants to set this, but it's also
            possible to pass an integer corresponding to the `enum wifi_phy_rate_t
            <https://docs.espressif.com/projects/esp-idf/en/v5.5.1/esp32/
            api-reference/network/esp_wifi.html#_CPPv415wifi_phy_rate_t>`_. This
            parameter is actually *write-only* due to ESP-IDF not providing any
            means for querying the radio interface's rate parameter.
            See also `espnow-long-range`. This API currently doesn't work on ESP32-C6.

        Returns:

            ``None`` or the value of the parameter being queried.

        Raises:

            - ``OSError(num, "ESP_ERR_ESPNOW_NOT_INIT")`` if not initialised.
            - ``ValueError()`` on invalid configuration options or values.
        """
        ...

    # Port note: on ESP8266 this form requires `mac` and supports only
    # positional peer settings in `add_peer`; `sync` is still available.
    @overload
    def send(
        self,
        mac: _MACAddress,
        msg: str | bytes,
        sync: bool = True,
    ) -> bool:
        """
        Send the data contained in ``msg`` to the peer with given network ``mac``
        address. In the second form, ``mac=None`` and ``sync=True``. The peer must
        be registered with `ESPNow.add_peer()<ESPNow.add_peer()>` before the
        message can be sent.

        Arguments:

          - *mac*: byte string exactly ``espnow.ADDR_LEN`` (6 bytes) long or
            ``None``. If *mac* is ``None`` (ESP32 only) the message will be sent
            to all registered peers, except any broadcast or multicast MAC
            addresses.

          - *msg*: string or byte-string up to ``espnow.MAX_DATA_LEN`` (250)
            bytes long.

          - *sync*:

            - ``True``: (default) send ``msg`` to the peer(s) and wait for a
              response (or not).

            - ``False`` send ``msg`` and return immediately. Responses from the
              peers will be discarded.

        Returns:

          ``True`` if ``sync=False`` or if ``sync=True`` and *all* peers respond,
          else ``False``.

        Raises:

          - ``OSError(num, "ESP_ERR_ESPNOW_NOT_INIT")`` if not initialised.
          - ``OSError(num, "ESP_ERR_ESPNOW_NOT_FOUND")`` if peer is not registered.
          - ``OSError(num, "ESP_ERR_ESPNOW_IF")`` the wifi interface is not
            `active()<network.WLAN.active>`.
          - ``OSError(num, "ESP_ERR_ESPNOW_NO_MEM")`` internal ESP-NOW buffers are
            full.
          - ``ValueError()`` on invalid values for the parameters.

        **Note**: A peer will respond with success if its wifi interface is
        `active()<network.WLAN.active>` and set to the same channel as the sender,
        regardless of whether it has initialised it's ESP-NOW system or is
        actively listening for ESP-NOW traffic (see the Espressif ESP-NOW docs).
        """

    # Port note: this broadcast-style shorthand exists only on ESP32.
    @overload
    def send(
        self,
        msg: str | bytes,
    ) -> bool:
        """
        Send the data contained in ``msg`` to the peer with given network ``mac``
        address. In the second form, ``mac=None`` and ``sync=True``. The peer must
        be registered with `ESPNow.add_peer()<ESPNow.add_peer()>` before the
        message can be sent.

        Arguments:

          - *mac*: byte string exactly ``espnow.ADDR_LEN`` (6 bytes) long or
            ``None``. If *mac* is ``None`` (ESP32 only) the message will be sent
            to all registered peers, except any broadcast or multicast MAC
            addresses.

          - *msg*: string or byte-string up to ``espnow.MAX_DATA_LEN`` (250)
            bytes long.

          - *sync*:

            - ``True``: (default) send ``msg`` to the peer(s) and wait for a
              response (or not).

            - ``False`` send ``msg`` and return immediately. Responses from the
              peers will be discarded.

        Returns:

          ``True`` if ``sync=False`` or if ``sync=True`` and *all* peers respond,
          else ``False``.

        Raises:

          - ``OSError(num, "ESP_ERR_ESPNOW_NOT_INIT")`` if not initialised.
          - ``OSError(num, "ESP_ERR_ESPNOW_NOT_FOUND")`` if peer is not registered.
          - ``OSError(num, "ESP_ERR_ESPNOW_IF")`` the wifi interface is not
            `active()<network.WLAN.active>`.
          - ``OSError(num, "ESP_ERR_ESPNOW_NO_MEM")`` internal ESP-NOW buffers are
            full.
          - ``ValueError()`` on invalid values for the parameters.

        **Note**: A peer will respond with success if its wifi interface is
        `active()<network.WLAN.active>` and set to the same channel as the sender,
        regardless of whether it has initialised it's ESP-NOW system or is
        actively listening for ESP-NOW traffic (see the Espressif ESP-NOW docs).
        """
        ...

    @overload
    def add_peer(
        self,
        mac: _MACAddress,
        lmk: bytes | bytearray | str | None = None,
        channel: int | None = None,
    ) -> None:
        """
        Add/register the provided *mac* address as a peer. Additional parameters may
        also be specified as positional or keyword arguments (any parameter set to
        ``None`` will be set to it's default value):

        Arguments:

            - *mac*: The MAC address of the peer (as a 6-byte byte-string).

            - *lmk*: The Local Master Key (LMK) key used to encrypt data
              transfers with this peer (unless the *encrypt* parameter is set to
              ``False``). Must be:

              - a byte-string or bytearray or string of length ``espnow.KEY_LEN``
                (16 bytes), or

              - any non ``True`` python value (default= ``b''``), signifying an
                *empty* key which will disable encryption.

            - *channel*: The wifi channel (2.4GHz) to communicate with this peer.
              Must be an integer from 0 to 14. If channel is set to 0 the current
              channel of the wifi device will be used, if channel is set to another
              value then this must match the channel currently configured on the
              interface (see :func:`WLAN.config`). (default=0)

            - *ifidx*: (ESP32 only) Index of the wifi interface which will be
              used to send data to this peer. Must be an integer set to
              ``network.WLAN.IF_STA`` (=0) or ``network.WLAN.IF_AP`` (=1).
              (default=0/``network.WLAN.IF_STA``). See `ESPNow and Wifi Operation`_
              below for more information.

            - *encrypt*: (ESP32 only) If set to ``True`` data exchanged with
              this peer will be encrypted with the PMK and LMK. (default =
              ``True`` if *lmk* is set to a valid key, else ``False``)

            **ESP8266**: Keyword args may not be used on the ESP8266.

            **Note:** The maximum number of peers which may be registered is 20
            (`espnow.MAX_TOTAL_PEER_NUM`), with a maximum of 6
            (`espnow.MAX_ENCRYPT_PEER_NUM`) of those peers with encryption enabled
            (see `ESP_NOW_MAX_ENCRYPT_PEER_NUM <https://docs.espressif.com/
            projects/esp-idf/en/latest/esp32/api-reference/network/
            esp_now.html#c.ESP_NOW_MAX_ENCRYPT_PEER_NUM>`_ in the Espressif API
            docs).

        Raises:

            - ``OSError(num, "ESP_ERR_ESPNOW_NOT_INIT")`` if not initialised.
            - ``OSError(num, "ESP_ERR_ESPNOW_EXIST")`` if *mac* is already
              registered.
            - ``OSError(num, "ESP_ERR_ESPNOW_FULL")`` if too many peers are
              already registered.
            - ``OSError(num, "ESP_ERR_ESPNOW_CHAN")`` if a channel value was
              set that doesn't match the channel currently configured for this
              interface.
            - ``ValueError()`` on invalid keyword args or values.
        """
        ...

    @overload
    def add_peer(
        self,
        mac: _MACAddress,
        lmk: Optional[bytes | bytearray | str] = None,
        channel: Optional[int] = None,
        ifidx: Optional[int] = None,
        encrypt: Optional[bool] = True,
    ) -> None:
        """
        Add/register the provided *mac* address as a peer. Additional parameters may
        also be specified as positional or keyword arguments (any parameter set to
        ``None`` will be set to it's default value):

        Arguments:

            - *mac*: The MAC address of the peer (as a 6-byte byte-string).

            - *lmk*: The Local Master Key (LMK) key used to encrypt data
              transfers with this peer (unless the *encrypt* parameter is set to
              ``False``). Must be:

              - a byte-string or bytearray or string of length ``espnow.KEY_LEN``
                (16 bytes), or

              - any non ``True`` python value (default= ``b''``), signifying an
                *empty* key which will disable encryption.

            - *channel*: The wifi channel (2.4GHz) to communicate with this peer.
              Must be an integer from 0 to 14. If channel is set to 0 the current
              channel of the wifi device will be used, if channel is set to another
              value then this must match the channel currently configured on the
              interface (see :func:`WLAN.config`). (default=0)

            - *ifidx*: (ESP32 only) Index of the wifi interface which will be
              used to send data to this peer. Must be an integer set to
              ``network.WLAN.IF_STA`` (=0) or ``network.WLAN.IF_AP`` (=1).
              (default=0/``network.WLAN.IF_STA``). See `ESPNow and Wifi Operation`_
              below for more information.

            - *encrypt*: (ESP32 only) If set to ``True`` data exchanged with
              this peer will be encrypted with the PMK and LMK. (default =
              ``True`` if *lmk* is set to a valid key, else ``False``)

            **ESP8266**: Keyword args may not be used on the ESP8266.

            **Note:** The maximum number of peers which may be registered is 20
            (`espnow.MAX_TOTAL_PEER_NUM`), with a maximum of 6
            (`espnow.MAX_ENCRYPT_PEER_NUM`) of those peers with encryption enabled
            (see `ESP_NOW_MAX_ENCRYPT_PEER_NUM <https://docs.espressif.com/
            projects/esp-idf/en/latest/esp32/api-reference/network/
            esp_now.html#c.ESP_NOW_MAX_ENCRYPT_PEER_NUM>`_ in the Espressif API
            docs).

        Raises:

            - ``OSError(num, "ESP_ERR_ESPNOW_NOT_INIT")`` if not initialised.
            - ``OSError(num, "ESP_ERR_ESPNOW_EXIST")`` if *mac* is already
              registered.
            - ``OSError(num, "ESP_ERR_ESPNOW_FULL")`` if too many peers are
              already registered.
            - ``OSError(num, "ESP_ERR_ESPNOW_CHAN")`` if a channel value was
              set that doesn't match the channel currently configured for this
              interface.
            - ``ValueError()`` on invalid keyword args or values.
        """
        ...

class ESPNow:
    #
    @mp_available()  # force merge
    def __iter__(self) -> ESPNow: ...
    @mp_available()  # force merge
    def __next__(self) -> Tuple[_MACAddress | None, bytes | None]: ...
