from typing import Any

class OrderedDict:
    def __init__(self, *argv, **kwargs) -> None: ...
    def clear(self, *args, **kwargs) -> Any: ...
    def copy(self, *args, **kwargs) -> Any: ...
    def get(self, *args, **kwargs) -> Any: ...
    def items(self, *args, **kwargs) -> Any: ...
    def keys(self, *args, **kwargs) -> Any: ...
    def pop(self, *args, **kwargs) -> Any: ...
    def popitem(self, *args, **kwargs) -> Any: ...
    def setdefault(self, *args, **kwargs) -> Any: ...
    def update(self, *args, **kwargs) -> Any: ...
    def values(self, *args, **kwargs) -> Any: ...
    @classmethod
    def fromkeys(cls, *args, **kwargs) -> Any: ...

class deque:
    def __init__(self, *argv, **kwargs) -> None: ...
    def append(self, *args, **kwargs) -> Any: ...
    def popleft(self, *args, **kwargs) -> Any: ...

def namedtuple(*args, **kwargs) -> Any: ...