from _typeshed import Incomplete as Incomplete

CERT_REQUIRED: int
PROTOCOL_TLS_CLIENT: int
PROTOCOL_TLS_SERVER: int
CERT_OPTIONAL: int
CERT_NONE: int

def wrap_socket(*args, **kwargs) -> Incomplete: ...

class SSLContext:
    def wrap_socket(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
