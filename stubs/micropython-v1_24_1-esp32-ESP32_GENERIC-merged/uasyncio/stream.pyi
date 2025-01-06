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
Module: 'uasyncio.stream' on micropython-v1.24.1-esp32-ESP32_GENERIC
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

stream_awrite: Generator  ## = <generator>
open_connection: Generator  ## = <generator>
start_server: Generator  ## = <generator>

class StreamWriter:
    def write(self, *args, **kwargs) -> Incomplete: ...
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...

    awritestr: Generator  ## = <generator>
    wait_closed: Generator  ## = <generator>
    drain: Generator  ## = <generator>
    readexactly: Generator  ## = <generator>
    readinto: Generator  ## = <generator>
    read: Generator  ## = <generator>
    awrite: Generator  ## = <generator>
    readline: Generator  ## = <generator>
    aclose: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...

class Server:
    """
    This represents the server class returned from `start_server`.  It can be used
    in an ``async with`` statement to close the server upon exit.
    """

    def close(self) -> None:
        """
        Close the server.
        """
        ...
    wait_closed: Generator  ## = <generator>
    _serve: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None:
        """
        This represents the server class returned from `start_server`.  It can be used
        in an ``async with`` statement to close the server upon exit.
        """

class Stream:
    """
    This represents a TCP stream connection.  To minimise code this class implements
    both a reader and a writer, and both ``StreamReader`` and ``StreamWriter`` alias to
    this class.
    """

    def write(self, buf: AnyReadableBuf, /) -> None:
        """
        Accumulated *buf* to the output buffer.  The data is only flushed when
        `Stream.drain` is called.  It is recommended to call `Stream.drain` immediately
        after calling this function.
        """
        ...

    def get_extra_info(self, v: str, /) -> str:
        """
        Get extra information about the stream, given by *v*.  The valid values for *v* are:
        ``peername``.
        """
        ...

    def close(self) -> None:
        """
        Close the stream.
        """
        ...
    awritestr: Generator  ## = <generator>
    wait_closed: Generator  ## = <generator>
    drain: Generator  ## = <generator>
    readexactly: Generator  ## = <generator>
    readinto: Generator  ## = <generator>
    read: Generator  ## = <generator>
    awrite: Generator  ## = <generator>
    readline: Generator  ## = <generator>
    aclose: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None:
        """
        This represents a TCP stream connection.  To minimise code this class implements
        both a reader and a writer, and both ``StreamReader`` and ``StreamWriter`` alias to
        this class.
        """

class StreamReader:
    def write(self, *args, **kwargs) -> Incomplete: ...
    def get_extra_info(self, *args, **kwargs) -> Incomplete: ...
    def close(self, *args, **kwargs) -> Incomplete: ...

    awritestr: Generator  ## = <generator>
    wait_closed: Generator  ## = <generator>
    drain: Generator  ## = <generator>
    readexactly: Generator  ## = <generator>
    readinto: Generator  ## = <generator>
    read: Generator  ## = <generator>
    awrite: Generator  ## = <generator>
    readline: Generator  ## = <generator>
    aclose: Generator  ## = <generator>
    def __init__(self, *argv, **kwargs) -> None: ...
