from typing import Any

class Lock:
    acquire: Any
    def locked(self, *args) -> Any: ...
    def release(self, *args) -> Any: ...

core: Any
