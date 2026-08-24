""" """

from __future__ import annotations

from typing import Any, Optional

from _typeshed import Incomplete
from typing_extensions import Awaitable, TypeAlias, TypeVar

class USBD_NCM:
    """
    Create and return a USBD_NCM object.  This initialises the NCM network
    interface if it has not already been initialised.  Only one instance
    exists (singleton).
    """
    def __init__(self) -> None: ...
    def active(self, is_active: Optional[Any] = None) -> bool:
        """
        Activate or deactivate the network interface.  Without argument returns
        current state as a bool.

        The interface is brought up automatically before USB enumeration, so this
        returns ``True`` from boot.
        """
        ...
    def isconnected(self) -> bool:
        """
        Returns ``True`` if the USB host has configured the NCM interface,
        ``False`` otherwise.

        When USB is disconnected, this returns ``False`` and network traffic
        stops. The interface remains registered with lwIP and can resume when
        the host reconnects and re-enumerates the device.
        """
        ...
    def status(self) -> int:
        """
        Returns the link status as an integer: ``1`` if the interface is up,
        ``0`` otherwise.
        """
        ...
    def ipconfig(self, param) -> Incomplete:
        """
        See `AbstractNIC.ipconfig`.
        """
        ...
    def ifconfig(self, configtuple: Optional[Any] = None) -> Incomplete:
        """
        See `AbstractNIC.ifconfig`.
        """
        ...
