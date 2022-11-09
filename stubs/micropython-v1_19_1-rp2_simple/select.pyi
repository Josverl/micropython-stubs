from typing import Any

POLLOUT: int
POLLIN: int
POLLHUP: int
POLLERR: int

def select(*args, **kwargs) -> Any: ...
def poll(*args, **kwargs) -> Any: ...
