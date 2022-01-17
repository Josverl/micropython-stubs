from .core import ble as ble, ensure_active as ensure_active, log_error as log_error, log_info as log_info, log_warn as log_warn, register_irq_handler as register_irq_handler
from .device import DeviceConnection as DeviceConnection, DeviceTimeout as DeviceTimeout
from typing import Any

_registered_characteristics: Any
_IRQ_GATTS_WRITE: Any
_IRQ_GATTS_READ_REQUEST: Any
_IRQ_GATTS_INDICATE_DONE: Any
_FLAG_READ: Any
_FLAG_WRITE_NO_RESPONSE: Any
_FLAG_WRITE: Any
_FLAG_NOTIFY: Any
_FLAG_INDICATE: Any
_FLAG_READ_ENCRYPTED: Any
_FLAG_READ_AUTHENTICATED: Any
_FLAG_READ_AUTHORIZED: Any
_FLAG_WRITE_ENCRYPTED: Any
_FLAG_WRITE_AUTHENTICATED: Any
_FLAG_WRITE_AUTHORIZED: Any
_FLAG_WRITE_CAPTURE: Any
_FLAG_DESC_READ: Any
_FLAG_DESC_WRITE: Any
_WRITE_CAPTURE_QUEUE_LIMIT: Any

def _server_irq(event, data): ...
def _server_shutdown() -> None: ...

class Service:
    uuid: Any
    characteristics: Any
    def __init__(self, uuid) -> None: ...
    def _tuple(self): ...

class BaseCharacteristic:
    _value_handle: Any
    _initial: Any
    def _register(self, value_handle) -> None: ...
    def _tuple(self): ...
    def read(self): ...
    def write(self, data, send_update: bool = ...) -> None: ...
    async def written(self, timeout_ms: Any | None = ...): ...
    def on_read(self, connection): ...
    def _remote_write(conn_handle, value_handle) -> None: ...
    def _remote_read(conn_handle, value_handle): ...

class Characteristic(BaseCharacteristic):
    descriptors: Any
    _write_event: Any
    _write_queue: Any
    _indicate_connection: Any
    _indicate_event: Any
    _indicate_status: Any
    uuid: Any
    flags: Any
    _value_handle: Any
    _initial: Any
    def __init__(self, service, uuid, read: bool = ..., write: bool = ..., write_no_response: bool = ..., notify: bool = ..., indicate: bool = ..., initial: Any | None = ..., capture: bool = ...) -> None: ...
    def notify(self, connection, data: Any | None = ...) -> None: ...
    async def indicate(self, connection, timeout_ms: int = ...) -> None: ...
    def _indicate_done(conn_handle, value_handle, status) -> None: ...

class BufferedCharacteristic(Characteristic):
    _max_len: Any
    _append: Any
    def __init__(self, service, uuid, max_len: int = ..., append: bool = ...) -> None: ...
    def _register(self, value_handle) -> None: ...

class Descriptor(BaseCharacteristic):
    _write_connection: Any
    _write_event: Any
    uuid: Any
    flags: Any
    _value_handle: Any
    _initial: Any
    def __init__(self, characteristic, uuid, read: bool = ..., write: bool = ..., initial: Any | None = ...) -> None: ...

def register_services(*services) -> None: ...
