from typing_extensions import reveal_type, assert_type

import asyncio

event = asyncio.Event()


async def blink_N(led, period_ms, n=1) -> int:
    for _ in range(n):
        led.on()
        await asyncio.sleep_ms(5)
        led.off()
        await asyncio.sleep_ms(period_ms)
    return n


async def test():
    await event.wait()
    tsk = asyncio.create_task(blink_N(0, 100, 5))

    reveal_type(tsk)  # This should be "Task or Task[int]"

    assert_type(tsk, asyncio.Task[int])  # This should be "Task or Task[int]"

    tsk.cancel()
