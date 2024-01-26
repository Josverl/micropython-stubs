# espnow module for MicroPython on ESP8266
# MIT license; Copyright (c) 2022 Glenn Moloney @glenn20

"""
ESP-NOW :doc:`asyncio` support.

MicroPython module: https://docs.micropython.org/en/v1.22.0/library/aioespnow.html
"""
from _espnow import *
from select import poll, POLLIN
from _typeshed import Incomplete
from typing import Iterator, List, Tuple, Union


class ESPNow(ESPNowBase, Iterator):
    """
    Returns the singleton ESPNow object. As this is a singleton, all calls to
    `espnow.ESPNow()` return a reference to the same object.

    .. note::
      Some methods are available only on the ESP32 due to code size
      restrictions on the ESP8266 and differences in the Espressif API.
    """

    # Static buffers for alloc free receipt of messages with ESPNow.irecv().
    _data = [bytearray(ADDR_LEN), bytearray(MAX_DATA_LEN)]
    _none_tuple = (None, None)

    def __init__(self) -> None:
        super().__init__()
        self._poll = poll()  # For any() method below...
        self._poll.register(self, POLLIN)

    def irecv(self, timeout_ms=None) -> Incomplete:
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
        n = self.recvinto(self._data, timeout_ms)
        return self._data if n else self._none_tuple

    def recv(self, timeout_ms=None) -> Union[List, Tuple[None, None]]:
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
        n = self.recvinto(self._data, timeout_ms)
        return [bytes(x) for x in self._data] if n else self._none_tuple

    def __iter__(self):
        return self

    def __next__(self):
        return self.irecv()  # Use alloc free irecv() method

    def any(self) -> Incomplete:  # For the ESP8266 which does not have ESPNow.any()
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
        try:
            next(self._poll.ipoll(0))
            return True
        except StopIteration:
            return False
