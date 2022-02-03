from typing import Any

POLLERR: int
POLLHUP: int
POLLIN: int
POLLOUT: int

def poll(*args, **kwargs) -> Any: ...
def select(*args, **kwargs) -> Any: ...
