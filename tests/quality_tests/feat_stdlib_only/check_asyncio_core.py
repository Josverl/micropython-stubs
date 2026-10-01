import asyncio
from typing_extensions import assert_type

assert_type(asyncio.core._io_queue, asyncio.core.IOQueue)
asyncio.core._io_queue.queue_read(object())
