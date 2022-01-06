from typing import Any

Node = Any

class Lock:
    def locked() -> None: ...
    def release() -> None: ...
