from typing import Optional, Any
from _typeshed import Incomplete as Incomplete

class sha256:
    """
    Create an SHA256 hasher object and optionally feed ``data`` into it.
    """

    def digest(self, *args, **kwargs) -> Any: ...
    def update(self, *args, **kwargs) -> Any: ...
    def __init__(self, data: Optional[Any] = ...) -> None: ...
