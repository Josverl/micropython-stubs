""" """

from __future__ import annotations
from _typeshed import Incomplete
from typing_extensions import TypeVar, TypeAlias, Awaitable

class WDT:
    """
    The WDT is used to restart the system when the application crashes and ends
    up into a non recoverable state. Once started it cannot be stopped or
    reconfigured in any way. After enabling, the application must "feed" the
    watchdog periodically to prevent it from expiring and resetting the system.

    Example usage::

        from machine import WDT
        wdt = WDT(timeout=2000)  # enable it with a timeout of 2s
        wdt.feed()

    Availability of this class: pyboard, WiPy, esp8266, esp32.
    """
    def __init__(self, *, id: int = 0, timeout: int = 5000) -> None:
        """
        Create a WDT object and start it. The timeout must be given in milliseconds.
        Once it is running the timeout cannot be changed and the WDT cannot be stopped either.

        Notes: On the esp32 the minimum timeout is 1 second. On the esp8266 a timeout
        cannot be specified, it is determined by the underlying system.
        """
    def feed(self) -> None:
        """
        Feed the WDT to prevent it from resetting the system. The application
        should place this call in a sensible place ensuring that the WDT is
        only fed after verifying that everything is functioning correctly.
        """
        ...
