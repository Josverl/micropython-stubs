""" """

from __future__ import annotations
from _typeshed import Incomplete

class SD:
    """
    Create a SD card object. See ``init()`` for parameters if initialization.
    """

    def __init__(self, id, *args, **kwargs) -> None: ...
    def init(self, id=0, pins=("GP10", "GP11", "GP15")) -> None:
        """
        Enable the SD card. In order to initialize the card, give it a 3-tuple:
        ``(clk_pin, cmd_pin, dat0_pin)``.
        """
        ...

    def deinit(self) -> None:
        """
        Disable the SD card.
        """
        ...
