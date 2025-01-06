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
Module: 'uasyncio.event' on micropython-v1.24.1-esp32-ESP32_GENERIC
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

class ThreadSafeFlag:
    """
    class ThreadSafeFlag
    --------------------
    """

    def set(self) -> None:
        """
        Set the flag.  If there is a task waiting on the flag, it will be scheduled
        to run.
        """
        ...

    def ioctl(self, *args, **kwargs) -> Incomplete: ...
    def clear(self) -> None:
        """
        Clear the flag. This may be used to ensure that a possibly previously-set
        flag is clear before waiting for it.
        """
        ...
    wait: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None:
        """
        Create a new flag which can be used to synchronise a task with code running
        outside the asyncio loop, such as other threads, IRQs, or scheduler
        callbacks.  Flags start in the cleared state.
        """

class Event:
    """
    class Event
    -----------
    """

    def set(self) -> None:
        """
        Set the event.  Any tasks waiting on the event will be scheduled to run.

        Note: This must be called from within a task. It is not safe to call this
        from an IRQ, scheduler callback, or other thread. See `ThreadSafeFlag`.
        """
        ...

    def is_set(self) -> bool:
        """
        Returns ``True`` if the event is set, ``False`` otherwise.
        """
        ...

    def clear(self) -> None:
        """
        Clear the event.
        """
        ...
    wait: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None:
        """
        Create a new event which can be used to synchronise tasks.  Events start
        in the cleared state.
        """
