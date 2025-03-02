
- no _asyncio.pyi stubs to avoid conflict with stdlib re-use

- Generators 
    are not values - but are always callables, or coroutines
    so rewrite 
    `open_connection: Generator  ## = <generator>`
    to 
    `async def open_connection () -> Callable[..., Awaitable[Tuple[StreamReader, StreamWriter]]]`
    or similar 
