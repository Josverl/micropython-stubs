# MicroPython asyncio module
# MIT license; Copyright (c) 2019 Damien P. George

"""
Asynchronous I/O scheduler for writing concurrent code.

MicroPython module: https://docs.micropython.org/en/v1.21.0/library/asyncio.html

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
"""
from .core import *
from _typeshed import Incomplete

__version__ = (3, 0, 0)

_attrs = {
    "wait_for": "funcs",
    "wait_for_ms": "funcs",
    "gather": "funcs",
    "Event": "event",
    "ThreadSafeFlag": "event",
    "Lock": "lock",
    "open_connection": "stream",
    "start_server": "stream",
    "StreamReader": "stream",
    "StreamWriter": "stream",
}


# Lazy loader, effectively does:
#   global attr
#   from .mod import attr
def __getattr__(attr):
    mod = _attrs.get(attr, None)
    if mod is None:
        raise AttributeError(attr)
    value = getattr(__import__(mod, None, None, True, 1), attr)
    globals()[attr] = value
    return value
