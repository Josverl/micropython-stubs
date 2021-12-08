from asyncio import *
from typing import Any

OrgTask = Task

class Task(OrgTask):
    _must_cancel: bool
    _fut_waiter: Any
    def _step(self, value: Any | None = ..., exc: Any | None = ...) -> None: ...
OrgStreamWriter = StreamWriter

class StreamWriter(OrgStreamWriter):
    def awrite(self, data) -> None: ...
    def aclose(self) -> None: ...
