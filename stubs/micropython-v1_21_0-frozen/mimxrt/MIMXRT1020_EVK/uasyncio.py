# This module just allows `import uasyncio` to work. It lazy-loads from
# `asyncio` without duplicating its globals dict.


from _typeshed import Incomplete as Incomplete
from typing import Any, Coroutine, List, Tuple


def __getattr__(attr):
    import asyncio

    return getattr(asyncio, attr)
