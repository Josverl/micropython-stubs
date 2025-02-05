# Samples curtesy of Peter Hinch
# https://github.com/peterhinch/micropython-async/blob/master/v3/docs/TUTORIAL.md

import asyncio

async def bar(n):
    count = 0
    for count in range(n):
        await asyncio.sleep_ms(200 * n)  # Pause by varying amounts # stubs-ignore: linter=="mypy"
    print('Instance {} stops with count = {}'.format(n, count))
    return count * count

async def main():
    tasks = (bar(2), bar(3), bar(4))

    print('Waiting for gather...')
    res = await asyncio.gather(*tasks)
    print(res)

asyncio.run(main())