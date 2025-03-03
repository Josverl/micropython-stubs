# Samples curtesy of Peter Hinch
# https://github.com/peterhinch/micropython-async/blob/master/v3/docs/TUTORIAL.md

import asyncio


async def bar1():
    count = 0
    while True:
        count += 1
        print(count)
        await asyncio.sleep(1)  # Pause 1s


asyncio.run(bar1())


# ==============================================================================

import asyncio
async def bar2(x):
    count = 0
    while True:
        count += 1
        print('Instance: {} count: {}'.format(x, count))
        await asyncio.sleep(1)  # Pause 1s

async def main():
    tasks = [None] * 3  # For CPython compaibility must store a reference see 2.2 Note
    for x in range(3):
        tasks[x] = asyncio.create_task(bar2(x))  
    await asyncio.sleep(10)

asyncio.run(main())

