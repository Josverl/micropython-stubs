import asyncio


async def slow_task():
    await asyncio.sleep(10)
    return 42


async def main():
    try:
        result = await asyncio.wait_for_ms(slow_task(), 500)
    except asyncio.TimeoutError:
        pass  # expected: task timed out


asyncio.run(main())
