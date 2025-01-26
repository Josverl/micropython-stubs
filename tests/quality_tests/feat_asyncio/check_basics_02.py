# Samples curtesy of Peter Hinch
# https://github.com/peterhinch/micropython-async/blob/master/v3/docs/TUTORIAL.md

import asyncio


async def bar(t):
    print("Bar started: waiting {}secs".format(t))
    await asyncio.sleep(t)
    print("Bar done")


async def main():
    await bar(1)  # Pauses here until bar is complete
    task = asyncio.create_task(bar(5))
    await asyncio.sleep(0)  # bar has now started
    print("Got here: bar running")  # Can run code here
    await task  # Now we wait for the bar task to complete
    print("All done")


asyncio.run(main())
