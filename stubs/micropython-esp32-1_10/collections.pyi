from typing import Any

class OrderedDict:
    def clear(self, *args) -> Any: ...
    def copy(self, *args) -> Any: ...
    @classmethod
    def fromkeys(cls, *args) -> Any: ...
    def get(self, *args) -> Any: ...
    def items(self, *args) -> Any: ...
    def keys(self, *args) -> Any: ...
    def pop(self, *args) -> Any: ...
    def popitem(self, *args) -> Any: ...
    def setdefault(self, *args) -> Any: ...
    def update(self, *args) -> Any: ...
    def values(self, *args) -> Any: ...

class deque:
    def append(self, *args) -> Any: ...
    def popleft(self, *args) -> Any: ...

def namedtuple(*args) -> Any: ...
