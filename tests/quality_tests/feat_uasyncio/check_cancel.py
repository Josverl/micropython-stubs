import asyncio

x = asyncio.Event()


async def test():
    await x.wait()
    z = asyncio.create_task(test())
    z.cancel()
