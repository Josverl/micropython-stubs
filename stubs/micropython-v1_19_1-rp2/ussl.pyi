from typing import Any

CERT_NONE: int
CERT_OPTIONAL: int
CERT_REQUIRED: int

def wrap_socket(*args, **kwargs) -> Any: ...
