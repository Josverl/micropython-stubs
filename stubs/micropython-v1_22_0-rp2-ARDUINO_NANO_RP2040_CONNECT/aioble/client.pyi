from _typeshed import Incomplete as Incomplete

def register_irq_handler(*args, **kwargs) -> Incomplete: ...
def const(*args, **kwargs) -> Incomplete: ...

class DeviceConnection:
    def timeout(self, *args, **kwargs) -> Incomplete: ...
    def is_connected(self, *args, **kwargs) -> Incomplete: ...
    def services(self, *args, **kwargs) -> Incomplete: ...
    l2cap_connect: Incomplete
    l2cap_accept: Incomplete
    pair: Incomplete
    service: Incomplete
    disconnect: Incomplete
    device_task: Incomplete
    disconnected: Incomplete
    exchange_mtu: Incomplete
    def __init__(self, *argv, **kwargs) -> None: ...

class ClientService:
    def characteristics(self, *args, **kwargs) -> Incomplete: ...
    characteristic: Incomplete
    def __init__(self, *argv, **kwargs) -> None: ...

ble: Incomplete

class GattError(Exception): ...
