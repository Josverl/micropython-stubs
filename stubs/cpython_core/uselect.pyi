from collections.abc import Generator
from typing import Any

POLLIN: Any
POLLOUT: Any

class poll:
    sel: Any
    def __init__(self) -> None: ...
    def register(self, stream, events, userdata: Any | None = ...): ...
    def ipoll(self, timeout: int = ...) -> Generator[Any, None, None]: ...
