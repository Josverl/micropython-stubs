""" """

from __future__ import annotations

from typing import List

from _typeshed import Incomplete
from typing_extensions import Awaitable, TypeAlias, TypeVar

class PinCtrl:
    """
    Gets an object defining a specific pin configuration.

    - ``func`` may be a :ref:`zephyr.PinMux <zephyr.PinMux>` instance, or, depending on the PinMux capabilities a string or an integer corresponding to a PinMux.
    - ``mode`` is the same as :ref:`machine.Pin <machine.Pin>`'s mode, but supports only ``Pin.IN`` and ``Pin.OUT``.
    - ``pull`` is the same as :ref:`machine.Pin <machine.Pin>`'s pull.
    - ``drive`` is the pin's drive strength in microAmperes (uA), if supported.
    - ``schmitt`` set whether the schmitt trigger device on the pin is enabled.
    - ``slew`` is an integer that defines the pin's slew rate. It is platform-specific.
    """

    MUXES: List
    """If the platform supports it, this contains a list of all possible :ref:`zephyr.PinMux <zephyr.PinMux>` instances."""
    def __init__(self, func, mode=0, pull=None, drive=0, schmitt=False, slew=0) -> None: ...
    def pinmux(self) -> Incomplete:
        """
        Returns the :ref:`zephyr.PinMux <zephyr.PinMux>` instance used by this PinCtrl.
        """
        ...
