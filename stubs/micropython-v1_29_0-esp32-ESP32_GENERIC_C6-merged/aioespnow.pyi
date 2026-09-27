"""
ESP-NOW asyncio support.

MicroPython module: https://docs.micropython.org/en/latest/library/espnow.html#aioespnow

---
Module: 'aioespnow' on micropython-v1.29.0-esp32-ESP32_GENERIC_C6
"""

# MCU: {'variant': '', 'build': '', 'arch': 'rv32imc', 'port': 'esp32', 'board': 'ESP32_GENERIC_C6', 'board_id': 'ESP32_GENERIC_C6', 'mpy': 'v6.3', 'ver': '1.29.0', 'family': 'micropython', 'cpu': 'ESP32-C6', 'version': '1.29.0'}
# Stubber: v1.28.6
from __future__ import annotations

from typing import Generator, TypeAlias, overload

from _mpy_shed import mp_available
from _typeshed import Incomplete
from espnow import ESPNow

_MACAddress: TypeAlias = bytes

class AIOESPNow(ESPNow):
    """
    Async wrapper around `espnow.ESPNow`.

    This class extends `ESPNow` with async methods and async iteration support.
    """

    _data: list = []
    _none_tuple: tuple = ()

    @overload
    async def asend(self, mac: _MACAddress, msg: str | bytes, sync: bool | None = True) -> bool: ...
    @overload
    async def asend(self, msg: str | bytes) -> bool: ...
    async def arecv(self) -> Generator:  ## = <generator>
        """
        Asyncio support for `ESPNow.recv()`.
        """
        ...
    async def airecv(self) -> Generator:  ## = <generator>
        """
        Asyncio support for `ESPNow.irecv()`.
        """
        ...
    def __init__(self, *argv, **kwargs) -> None: ...
    @mp_available()
    def __aiter__(self) -> AIOESPNow: ...
    @mp_available()
    async def __anext__(self) -> tuple[_MACAddress | bytearray | None, bytearray | None]: ...
