""" """

from __future__ import annotations
from _typeshed import Incomplete
from typing_extensions import TypeVar, TypeAlias, Awaitable
from .Pin import Pin

class SDCard:
    """
                  cs=None, cmd=None, data=None, freq=20000000)

    This class provides access to SD or MMC storage cards using either
    a dedicated SD/MMC interface hardware or through an SPI channel.
    The class implements the block protocol defined by :class:`vfs.AbstractBlockDev`.
    This allows the mounting of an SD card to be as simple as::

      vfs.mount(machine.SDCard(), "/sd")

    The constructor takes the following parameters:

     - *slot* selects which of the available interfaces to use. Leaving this
       unset will select the default interface.

     - *width* selects the bus width for the SD/MMC interface. This many data
       pins must be connected to the SD card.

     - *cd* can be used to specify a card-detect pin.

     - *wp* can be used to specify a write-protect pin.

     - *sck* can be used to specify an SPI clock pin.

     - *miso* can be used to specify an SPI miso pin.

     - *mosi* can be used to specify an SPI mosi pin.

     - *cs* can be used to specify an SPI chip select pin.

    The following additional parameters are only present on ESP32 port:

     - *cmd* can be used to specify the SD CMD pin (ESP32-S3 only).

     - *data* can be used to specify a list or tuple of SD data bus pins
       (ESP32-S3 only).

     - *freq* selects the SD/MMC interface frequency in Hz.
    """
