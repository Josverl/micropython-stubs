# Simple, syntactically valid MicroPython-style snippet used to exercise
# the pyrefly type checker against the generated stubs.

import asyncio
import machine
import sys


async def blink(pin_no: int, delay_s: float) -> None:
    pin = machine.Pin(pin_no, machine.Pin.OUT)
    while True:
        pin.value(not pin.value())
        await asyncio.sleep(delay_s)


def add(a: int, b: int) -> int:
    return a + b


def main() -> None:
    print(add(1, 2))
    print(sys.implementation.name)
    asyncio.run(blink(2, 0.5))


if __name__ == "__main__":
    main()
