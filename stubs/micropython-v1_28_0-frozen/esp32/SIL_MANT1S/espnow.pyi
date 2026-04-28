# Micropython v1.28.0 frozen stubs
"""
ESP-NOW :doc:`asyncio` support.

MicroPython module: https://docs.micropython.org/en/v1.28.0/library/aioespnow.html
"""

from __future__ import annotations
from _espnow import *
from _typeshed import Incomplete
from _mpy_shed import mp_available
from typing import Iterator, Literal, Optional, Tuple, Union, overload
from typing_extensions import Awaitable, Buffer, TypeAlias, TypeVar

MAX_DATA_LEN: Incomplete = 250
"""\
The following constants correspond to different transmit data rates on ESP32
only. Lower data rates are generally more reliable over long distances:
"""
KEY_LEN: Incomplete = 16
"""\
The following constants correspond to different transmit data rates on ESP32
only. Lower data rates are generally more reliable over long distances:
"""
ADDR_LEN: Incomplete = 6
"""\
The following constants correspond to different transmit data rates on ESP32
only. Lower data rates are generally more reliable over long distances:
"""
MAX_TOTAL_PEER_NUM: Incomplete = 20
"""\
The following constants correspond to different transmit data rates on ESP32
only. Lower data rates are generally more reliable over long distances:
"""
MAX_ENCRYPT_PEER_NUM: Incomplete = 6
"""\
The following constants correspond to different transmit data rates on ESP32
only. Lower data rates are generally more reliable over long distances:
"""
RATE_LORA_250K: Incomplete
"""See  `espnow-long-range`."""
RATE_LORA_500K: Incomplete
"""See  `espnow-long-range`."""
RATE_1M: Incomplete
"""\
Unless using the two proprietary long range data rates, only the sender must
configure the data rate.
"""
RATE_2M: Incomplete
"""\
Unless using the two proprietary long range data rates, only the sender must
configure the data rate.
"""
RATE_5M: Incomplete
"""\
Unless using the two proprietary long range data rates, only the sender must
configure the data rate.
"""
RATE_6M: Incomplete
"""\
Unless using the two proprietary long range data rates, only the sender must
configure the data rate.
"""
RATE_11M: Incomplete
"""\
Unless using the two proprietary long range data rates, only the sender must
configure the data rate.
"""
RATE_12M: Incomplete
"""\
Unless using the two proprietary long range data rates, only the sender must
configure the data rate.
"""
RATE_24M: Incomplete
"""\
Unless using the two proprietary long range data rates, only the sender must
configure the data rate.
"""
RATE_54M: Incomplete
"""\
Unless using the two proprietary long range data rates, only the sender must
configure the data rate.
"""
_MACAddress: TypeAlias = bytes
_PeerInfo: TypeAlias = Tuple[_MACAddress, bytes, int, int, bool]

class ESPNow(ESPNowBase, Iterator):
    """
    Returns the singleton ESPNow object. As this is a singleton, all calls to
    `espnow.ESPNow()` return a reference to the same object.

    .. note::
      Some methods are available only on the ESP32 due to code size
      restrictions on the ESP8266 and differences in the Espressif API.
    """

    _data: Incomplete
    _none_tuple: Incomplete
    def __init__(self) -> None: ...
    def irecv(self, timeout_ms=None) -> Tuple[_MACAddress | bytearray | None, bytearray | None]:
        """
        Works like `ESPNow.recv()` but will reuse internal bytearrays to store the
        return values: ``[mac, msg]``, so that no new memory is allocated on each
        call.

        Arguments:

            *timeout_ms*: (Optional) Timeout in milliseconds (see `ESPNow.recv()`).

        Returns:

          - As for `ESPNow.recv()`, except that ``msg`` is a bytearray, instead of
            a bytestring. On the ESP8266, ``mac`` will also be a bytearray.

        Raises:

          - See `ESPNow.recv()`.

        **Note:** You may also read messages by iterating over the ESPNow object,
        which will use the `irecv()` method for alloc-free reads, eg: ::

          import espnow
          e = espnow.ESPNow(); e.active(True)
          for mac, msg in e:
              print(mac, msg)
              if mac is None:   # mac, msg will equal (None, None) on timeout
                  break
        """
        ...
    def recv(self, timeout_ms=None) -> Tuple[_MACAddress | None, bytes | None]:
        """
        Wait for an incoming message and return the ``mac`` address of the peer and
        the message. **Note**: It is **not** necessary to register a peer (using
        `add_peer()<ESPNow.add_peer()>`) to receive a message from that peer.

        Arguments:

            - *timeout_ms*: (Optional): May have the following values.

              - ``0``: No timeout. Return immediately if no data is available;
              - ``> 0``: Specify a timeout value in milliseconds;
              - ``< 0``: Do not timeout, ie. wait forever for new messages; or
              - ``None`` (or not provided): Use the default timeout value set with
                `ESPNow.config()`.

        Returns:

          - ``(None, None)`` if timeout is reached before a message is received, or

          - ``[mac, msg]``: where:

            - ``mac`` is a bytestring containing the address of the device which
              sent the message, and
            - ``msg`` is a bytestring containing the message.

        Raises:

          - ``OSError(num, "ESP_ERR_ESPNOW_NOT_INIT")`` if not initialised.
          - ``OSError(num, "ESP_ERR_ESPNOW_IF")`` if the wifi interface is not
            `active()<network.WLAN.active>`.
          - ``ValueError()`` on invalid *timeout_ms* values.

        `ESPNow.recv()` will allocate new storage for the returned list and the
        ``peer`` and ``msg`` bytestrings. This can lead to memory fragmentation if
        the data rate is high. See `ESPNow.irecv()` for a memory-friendly
        alternative.
        """
        ...
    def irq(self, callback) -> None:
        """
        Set a callback function to be called *as soon as possible* after a message has
        been received from another ESPNow device. The callback function will be called
        with the `ESPNow` instance object as an argument. For more reliable operation,
        it is recommended to read out as many messages as are available when the
        callback is invoked and to set the read timeout to zero, eg: ::

              def recv_cb(e):
                  while True:  # Read out all messages waiting in the buffer
                      mac, msg = e.irecv(0)  # Don't wait if no messages left
                      if mac is None:
                          return
                      print(mac, msg)
              e.irq(recv_cb)

        The `irq()<ESPNow.irq()>` callback method is an alternative method for
        processing incoming messages, especially if the data rate is moderate
        and the device is *not too busy* but there are some caveats:

        - The scheduler stack *can* overflow and callbacks will be missed if
          packets are arriving at a sufficient rate or if other MicroPython components
          (eg, bluetooth, machine.Pin.irq(), machine.timer, i2s, ...) are exercising
          the scheduler stack. This method may be less reliable for dealing with
          bursts of messages, or high throughput or on a device which is busy dealing
          with other hardware operations.

        - For more information on *scheduled* function callbacks see:
          `micropython.schedule()<micropython.schedule>`.
        """
        ...
    #
    @mp_available()  # force merge
    def __iter__(self) -> ESPNow: ...
    @mp_available()  # force merge
    def __next__(self) -> Tuple[_MACAddress | None, bytes | None]: ...
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

class ESPNowBase:
    @overload
    def config(self, /, *, rxbuf: int = ..., timeout_ms: int = ..., rate: int = ...) -> None: ...
    @overload
    def config(self, param: Literal["rxbuf", "timeout_ms"], /) -> int: ...
    @overload
    def send(self, msg: Union[str, bytes, bytearray, Buffer], /) -> bool: ...
    @overload
    def send(
        self, peer_addr: Optional[Union[bytes, bytearray]], msg: Union[str, bytes, bytearray, Buffer], sync: bool = True, /
    ) -> bool: ...
