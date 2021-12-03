from typing import Any

class Lock:
    acquire: Any
    def locked() -> None: ...
    def release() -> None: ...

core: Any
