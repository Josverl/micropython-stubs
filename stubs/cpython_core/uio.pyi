import io
from typing import Any

class UioStream:
    _s: Any
    _is_bin: Any
    def __init__(self, s, is_bin) -> None: ...
    def write(self, data, off: Any | None = ..., sz: Any | None = ...) -> None: ...
    def __getattr__(self, attr): ...
    def __iter__(self): ...
    def __enter__(self): ...
    def __exit__(self, *args): ...

class StringIO(io.StringIO):
    def __iadd__(self, s): ...

class BytesIO(io.BytesIO):
    def __iadd__(self, s): ...

def open(name, mode: str = ..., *args, **kw): ...
