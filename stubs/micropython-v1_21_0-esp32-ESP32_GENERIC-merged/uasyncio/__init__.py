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

---
Module: 'uasyncio.__init__' on micropython-v1.21.0-esp32-Generic_ESP32_module_with_SPIRAM_with_ESP32
"""

# MCU: {'family': 'micropython', 'version': '1.21.0', 'build': '', 'ver': 'v1.21.0', 'port': 'esp32', 'board': 'Generic_ESP32_module_with_SPIRAM_with_ESP32', 'cpu': 'SPIRAM', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.14.0
from _typeshed import Incomplete
from typing import Any, Coroutine, List, Tuple


def ticks_add(*args, **kwargs) -> Incomplete: ...
def create_task(coro) -> Task:
    """
    Create a new task from the given coroutine and schedule it to run.

    Returns the corresponding `Task` object.
    """
    ...


def wait_for_ms(awaitable, timeout) -> Coroutine[Incomplete, Any, Any]:
    """
    Similar to `wait_for` but *timeout* is an integer in milliseconds.

    This is a coroutine, and a MicroPython extension.
    """
    ...


def ticks_diff(*args, **kwargs) -> Incomplete: ...
def run_until_complete(*args, **kwargs) -> Incomplete: ...
def new_event_loop() -> Incomplete:
    """
    Reset the event loop and return it.

    Note: since MicroPython only has a single event loop this function just
    resets the loop's state, it does not create a new one.
    """
    ...


def current_task() -> Task:
    """
    Return the `Task` object associated with the currently running task.
    """
    ...


def get_event_loop() -> Incomplete:
    """
    Return the event loop used to schedule and run tasks.  See `Loop`.
    """
    ...


def ticks(*args, **kwargs) -> Incomplete: ...
def sleep(t) -> Coroutine[Incomplete, Any, Any]:
    """
    Sleep for *t* seconds (can be a float).

    This is a coroutine.
    """
    ...


def run(coro) -> Incomplete:
    """
    Create a new task from the given coroutine and run it until it completes.

    Returns the value returned by *coro*.
    """
    ...


def sleep_ms(t) -> Coroutine[Incomplete, Any, Any]:
    """
    Sleep for *t* milliseconds.

    This is a coroutine, and a MicroPython extension.
    """
    ...


class TimeoutError(Exception): ...
