"""
ESP-NOW :doc:`asyncio` support.

MicroPython module: https://docs.micropython.org/en/v1.24.0/library/aioespnow.html
"""

from __future__ import annotations
from _espnow import *
from _typeshed import Incomplete
from typing import Iterator, List, Tuple, Union, overload
from typing_extensions import Awaitable, TypeAlias, TypeVar

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
    _poll: Incomplete
    def __init__(self) -> None: ...
    def irecv(self, timeout_ms: Incomplete | None = None) -> Tuple[_MACAddress | bytearray | None, bytearray | None]:
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

    def recv(self, timeout_ms: Incomplete | None = None) -> Union[List, Tuple[None, None]]:
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

    @overload  # force merge
    def __iter__(self) -> ESPNow: ...
    #
    @overload  # force merge
    def __iter__(self) -> ESPNow: ...
    @overload  # force merge
    def __next__(self) -> Tuple[_MACAddress | None, bytes | None]: ...
    @overload  # force merge
    def __next__(self) -> Tuple[_MACAddress | None, bytes | None]: ...
    def any(self) -> bool:
        """
        Check if data is available to be read with `ESPNow.recv()`.

        For more sophisticated querying of available characters use `select.poll()`::

          import select
          import espnow

          e = espnow.ESPNow()
          poll = select.poll()
          poll.register(e, select.POLLIN)
          poll.poll(timeout)

        Returns:

           ``True`` if data is available to be read, else ``False``.
        """
        ...

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
