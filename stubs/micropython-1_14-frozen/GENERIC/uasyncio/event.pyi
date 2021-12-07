from . import core as core
from typing import Any

class Event:
    state: bool
    waiting: Any
    def __init__(self) -> None: ...
    def is_set(self): ...
    def set(self) -> None: ...
    def clear(self) -> None: ...
    async def wait(self): ...
