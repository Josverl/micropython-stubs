""" """

from __future__ import annotations
from _typeshed import Incomplete
from typing_extensions import TypeVar, TypeAlias, Awaitable

class DAC:
    """
      Construct a new DAC object.

      ``id`` is a pin object (ESP32 and Renesas RA) or an index to a DAC resource (SAMD).

    .. note::
      On the ESP32, DAC functionality is available on pins 25 and 26. On the
      ESP32-S2, pins 17 and 18. See :ref:`ESP32 Quickref <esp32_quickref>`
      for more details.

    .. note::
      SAMD21 has one DAC resource, SAMD51 has two. See :ref:`SAMD Quickref <samd_quickref>`
      for more details.
    """
    def __init__(self, id) -> None: ...
    def write(self, value) -> Incomplete:
        """
        Output an analog voltage to the pin connected to the DAC.

        ``value`` is a representation of the desired output; a linear interpolation of
        0-3.3V, though the range differs depending on the port and micro, see below:

        +--------------+------+--------+
        | *Port/micro* | Bits | Range  |
        +==============+======+========+
        | ESP32        | 8    | 0-255  |
        +--------------+------+--------+
        | SAMD21       | 10   | 0-1023 |
        +--------------+------+--------+
        | SAMD51       | 12   | 0-4095 |
        +--------------+------+--------+
        | Renesas RA   | 12   | 0-4095 |
        +--------------+------+--------+
        """
        ...
