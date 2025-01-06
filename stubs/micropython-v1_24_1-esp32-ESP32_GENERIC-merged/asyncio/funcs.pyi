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
Module: 'asyncio.funcs' on micropython-v1.24.1-esp32-ESP32_GENERIC
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

def wait_for_ms(awaitable: Awaitable[_T], timeout: int, /) -> Coroutine[Incomplete, Any, Any]:
    """
    Similar to `wait_for` but *timeout* is an integer in milliseconds.

    This is a coroutine, and a MicroPython extension.
    """
    ...

gather: Generator  ## = <generator>
wait_for: Generator  ## = <generator>

class _Remove:
    def remove(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

_run: Generator  ## = <generator>
