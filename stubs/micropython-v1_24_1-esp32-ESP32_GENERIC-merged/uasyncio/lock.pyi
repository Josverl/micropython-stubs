"""
Asynchronous I/O scheduler for writing concurrent code.

MicroPython module: https://docs.micropython.org/en/v1.24.1/library/asyncio.html

CPython module:
`asyncio `<https://docs.python.org/3.8/library/asyncio.html>

Example::

    import asyncio

    async def blink(led, period_ms):
        while True:
            led.on()
            await asyncio.sleep_ms(5)
            led.off()
            await asyncio.sleep_ms(period_ms)

    async def main(led1, led2):
        asyncio.create_task(blink(led1, 700))
        asyncio.create_task(blink(led2, 400))
        await asyncio.sleep_ms(10_000)

    # Running on a pyboard
    from pyb import LED
    asyncio.run(main(LED(1), LED(2)))

    # Running on a generic board
    from machine import Pin
    asyncio.run(main(Pin(1), Pin(2)))

Core functions
--------------

---
Module: 'uasyncio.lock' on micropython-v1.24.1-esp32-ESP32_GENERIC
"""

# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'esp32', 'board': 'ESP32_GENERIC', 'cpu': 'ESP32', 'mpy': 'v6.3', 'arch': 'xtensawin'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Callable, Coroutine, Dict, Generic, Iterable, List, Tuple, Generator
from _typeshed import Incomplete
from _mpy_shed import AnyReadableBuf
from abc import ABC
from typing_extensions import Awaitable, TypeAlias, TypeVar

_T = TypeVar("_T")
_C: TypeAlias = Coroutine[Any, None, _T] | Awaitable[_T]
StreamReader: TypeAlias = "Stream"
StreamWriter: TypeAlias = "Stream"

class Lock(Awaitable[None], ABC):
    """
    class Lock
    ----------
    """

    def locked(self) -> bool:
        """
        Returns ``True`` if the lock is locked, otherwise ``False``.
        """
        ...

    def release(self) -> None:
        """
        Release the lock.  If any tasks are waiting on the lock then the next one in the
        queue is scheduled to run and the lock remains locked.  Otherwise, no tasks are
        waiting an the lock becomes unlocked.
        """
        ...
    acquire: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None:
        """
        Create a new lock which can be used to coordinate tasks.  Locks start in
        the unlocked state.

        In addition to the methods below, locks can be used in an ``async with`` statement.
        """
