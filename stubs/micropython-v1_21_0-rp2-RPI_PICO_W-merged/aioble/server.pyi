from _typeshed import Incomplete as Incomplete

def log_info(*args, **kwargs) -> Incomplete: ...
def register_irq_handler(*args, **kwargs) -> Incomplete: ...
def log_warn(*args, **kwargs) -> Incomplete: ...
def log_error(*args, **kwargs) -> Incomplete: ...
def const(*args, **kwargs) -> Incomplete: ...
def ensure_active(*args, **kwargs) -> Incomplete: ...
def register_services(*args, **kwargs) -> Incomplete: ...

class Descriptor:
    def write(self, *args, **kwargs) -> Incomplete: ...
    def on_read(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    written: Incomplete
    def __init__(self, *argv, **kwargs) -> None: ...

class DeviceConnection:
    def services(self, *args, **kwargs) -> Incomplete: ...
    def is_connected(self, *args, **kwargs) -> Incomplete: ...
    def timeout(self, *args, **kwargs) -> Incomplete: ...
    l2cap_accept: Incomplete
    exchange_mtu: Incomplete
    pair: Incomplete
    l2cap_connect: Incomplete
    service: Incomplete
    disconnect: Incomplete
    device_task: Incomplete
    disconnected: Incomplete
    def __init__(self, *argv, **kwargs) -> None: ...

ble: Incomplete

class DeviceTimeout:
    def __init__(self, *argv, **kwargs) -> None: ...

class BaseCharacteristic:
    def write(self, *args, **kwargs) -> Incomplete: ...
    def on_read(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    written: Incomplete
    def __init__(self, *argv, **kwargs) -> None: ...

class deque:
    def popleft(self, *args, **kwargs) -> Incomplete: ...
    def append(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class BufferedCharacteristic:
    def on_read(self, *args, **kwargs) -> Incomplete: ...
    def notify(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    indicate: Incomplete
    written: Incomplete
    def __init__(self, *argv, **kwargs) -> None: ...

class Characteristic:
    def on_read(self, *args, **kwargs) -> Incomplete: ...
    def notify(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def read(self, *args, **kwargs) -> Incomplete: ...
    indicate: Incomplete
    written: Incomplete
    def __init__(self, *argv, **kwargs) -> None: ...

class GattError(Exception): ...