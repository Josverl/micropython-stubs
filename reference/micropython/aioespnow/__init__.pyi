"""
ESP-NOW asyncio support.

MicroPython module: https://docs.micropython.org/en/latest/library/espnow.html#aioespnow
"""

# source version: v1.28.0
# origin module:: repos/micropython/lib/micropython-lib/micropython/aioespnow/aioespnow.py
from __future__ import annotations

from typing import overload

from espnow import ESPNow

_MACAddress = bytes


class AIOESPNow(ESPNow):
    """
    Async wrapper around `espnow.ESPNow`.

    This class extends `ESPNow` with async methods and async iteration support.
    """

    async def arecv(self) -> tuple[_MACAddress | None, bytes | None]:
        """
        Asyncio support for `ESPNow.recv()`.
        """
        ...

    async def airecv(self) -> tuple[_MACAddress | bytearray | None, bytearray | None]:
        """
        Asyncio support for `ESPNow.irecv()`.
        """
        ...

    @overload
    async def asend(self, mac: _MACAddress, msg: str | bytes, sync: bool | None = True) -> bool:
        ...

    @overload
    async def asend(self, msg: str | bytes) -> bool:
        ...

    async def asend(self, mac: _MACAddress | str | bytes, msg: str | bytes | None = None, sync: bool | None = True) -> bool:
        """
        Asyncio support for `ESPNow.send()`.

        Port note: the one-argument shorthand (`asend(msg)`) maps to
        `send(None, msg, sync)` and is therefore ESP32-only, matching `espnow.send`.
        """
        ...

    def __aiter__(self) -> AIOESPNow:
        ...

    async def __anext__(self) -> tuple[_MACAddress | bytearray | None, bytearray | None]:
        ...
