from typing import Optional, Any
from _typeshed import Incomplete as Incomplete

class sha1:
    """
    Create an SHA1 hasher object and optionally feed ``data`` into it.
    """

    def __init__(self, data: Optional[Any] = ...) -> None: ...
    def update(self, *args, **kwargs) -> Any: ...
    def digest(self, *args, **kwargs) -> Any: ...

class sha256:
    """
    Create an SHA256 hasher object and optionally feed ``data`` into it.
    """

    def __init__(self, data: Optional[Any] = ...) -> None: ...
    def update(self, *args, **kwargs) -> Any: ...
    def digest(self, *args, **kwargs) -> Any: ...
