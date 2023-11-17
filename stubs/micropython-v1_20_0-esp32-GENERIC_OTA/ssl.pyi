from typing import Any

CERT_OPTIONAL: int
CERT_REQUIRED: int
CERT_NONE: int

def wrap_socket(*args, **kwargs) -> Any: ...
