from typing import Any

def register_irq_handler(*args, **kwargs) -> Any: ...
def const(*args, **kwargs) -> Any: ...

class ClientDiscover:
    def __init__(self, *argv, **kwargs) -> None: ...

class ClientService:
    def characteristics(self, *args, **kwargs) -> Any: ...
    characteristic: Any
    def __init__(self, *argv, **kwargs) -> None: ...

class ClientCharacteristic:
    def descriptors(self, *args, **kwargs) -> Any: ...
    indicated: Any
    notified: Any
    subscribe: Any
    read: Any
    descriptor: Any
    write: Any
    def __init__(self, *argv, **kwargs) -> None: ...

class BaseClientCharacteristic:
    write: Any
    read: Any
    def __init__(self, *argv, **kwargs) -> None: ...

class ClientDescriptor:
    write: Any
    read: Any
    def __init__(self, *argv, **kwargs) -> None: ...

class GattError(Exception): ...
