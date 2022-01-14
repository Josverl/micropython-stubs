from typing import Any

POLLERR: int
POLLHUP: int
POLLIN: int
POLLOUT: int

def poll(*args) -> Any: ...
def select(*args) -> Any: ...
