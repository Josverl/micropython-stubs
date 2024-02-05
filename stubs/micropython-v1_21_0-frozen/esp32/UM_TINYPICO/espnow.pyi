"""
ESP-NOW :doc:`asyncio` support.

MicroPython module: https://docs.micropython.org/en/v1.21.0/library/aioespnow.html
"""
from _espnow import *
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

    _data: Incomplete
    _none_tuple: Incomplete
    def __init__(self) -> None: ...
    def irecv(self, timeout_ms: Incomplete | None = ...) -> Incomplete:
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
    def recv(self, timeout_ms: Incomplete | None = ...) -> Union[List, Tuple[None, None]]:
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
    def __iter__(self): ...
    def __next__(self): ...
