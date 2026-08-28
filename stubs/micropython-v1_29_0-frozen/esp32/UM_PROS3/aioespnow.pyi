# Micropython v1.29.0 frozen stubs
"""
ESP-NOW asyncio support.

MicroPython module: https://docs.micropython.org/en/latest/library/espnow.html#aioespnow
"""

from __future__ import annotations

from collections.abc import Generator
from typing import TypeAlias, overload

import espnow
from _mpy_shed import mp_available
from _typeshed import Incomplete
from espnow import ESPNow

_MACAddress: TypeAlias = bytes

class AIOESPNow(ESPNow):
    """
    Async wrapper around `espnow.ESPNow`.

    This class extends `ESPNow` with async methods and async iteration support.
    """
    async def arecv(self) -> Generator[Incomplete, None, Incomplete]:
        """
        Asyncio support for `ESPNow.recv()`.
        """
        ...
    async def airecv(self) -> Generator[Incomplete, None, Incomplete]:
        """
        Asyncio support for `ESPNow.irecv()`.
        """
        ...

    @overload
    async def asend(self, mac: _MACAddress, msg: str | bytes, sync: bool | None = True) -> bool: ...
    @overload
    async def asend(self, msg: str | bytes) -> bool: ...
    @mp_available()
    def __aiter__(self) -> AIOESPNow: ...
    @mp_available()
    async def __anext__(self) -> tuple[_MACAddress | bytearray | None, bytearray | None]: ...
