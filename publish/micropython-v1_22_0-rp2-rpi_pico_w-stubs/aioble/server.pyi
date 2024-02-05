from .core import (
    GattError as GattError,
    ble as ble,
    ensure_active as ensure_active,
    log_error as log_error,
    log_info as log_info,
    log_warn as log_warn,
    register_irq_handler as register_irq_handler,
)
from .device import DeviceConnection as DeviceConnection, DeviceTimeout as DeviceTimeout
from _typeshed import Incomplete

_registered_characteristics: Incomplete
_IRQ_GATTS_WRITE: Incomplete
_IRQ_GATTS_READ_REQUEST: Incomplete
_IRQ_GATTS_INDICATE_DONE: Incomplete
_FLAG_READ: Incomplete
_FLAG_WRITE_NO_RESPONSE: Incomplete
_FLAG_WRITE: Incomplete
_FLAG_NOTIFY: Incomplete
_FLAG_INDICATE: Incomplete
_FLAG_READ_ENCRYPTED: Incomplete
_FLAG_READ_AUTHENTICATED: Incomplete
_FLAG_READ_AUTHORIZED: Incomplete
_FLAG_WRITE_ENCRYPTED: Incomplete
_FLAG_WRITE_AUTHENTICATED: Incomplete
_FLAG_WRITE_AUTHORIZED: Incomplete
_FLAG_WRITE_CAPTURE: Incomplete
_WRITE_CAPTURE_QUEUE_LIMIT: Incomplete

def _server_irq(event, data): ...
def _server_shutdown() -> None: ...

class Service:
    uuid: Incomplete
    characteristics: Incomplete
    def __init__(self, uuid) -> None: ...
    def _tuple(self): ...

class BaseCharacteristic:
    _value_handle: Incomplete
    _initial: Incomplete
    def _register(self, value_handle) -> None: ...
    def read(self): ...
    def write(self, data, send_update: bool = ...) -> None: ...
    @staticmethod
    def _init_capture() -> None: ...
    @staticmethod
    async def _run_capture_task() -> None: ...
    _write_data: Incomplete
    async def written(self, timeout_ms: Incomplete | None = ...): ...
    def on_read(self, connection): ...
    def _remote_write(conn_handle, value_handle) -> None: ...
    def _remote_read(conn_handle, value_handle): ...

class Characteristic(BaseCharacteristic):
    descriptors: Incomplete
    _write_event: Incomplete
    _write_data: Incomplete
    _indicate_connection: Incomplete
    _indicate_event: Incomplete
    _indicate_status: Incomplete
    uuid: Incomplete
    flags: Incomplete
    _value_handle: Incomplete
    _initial: Incomplete
    def __init__(
        self,
        service,
        uuid,
        read: bool = ...,
        write: bool = ...,
        write_no_response: bool = ...,
        notify: bool = ...,
        indicate: bool = ...,
        initial: Incomplete | None = ...,
        capture: bool = ...,
    ) -> None: ...
    def _tuple(self): ...
    def notify(self, connection, data: Incomplete | None = ...) -> None: ...
    async def indicate(self, connection, data: Incomplete | None = ..., timeout_ms: int = ...) -> None: ...
    def _indicate_done(conn_handle, value_handle, status) -> None: ...

class BufferedCharacteristic(Characteristic):
    _max_len: Incomplete
    _append: Incomplete
    def __init__(self, *args, max_len: int = ..., append: bool = ..., **kwargs) -> None: ...
    def _register(self, value_handle) -> None: ...

class Descriptor(BaseCharacteristic):
    _write_event: Incomplete
    _write_data: Incomplete
    uuid: Incomplete
    flags: Incomplete
    _value_handle: Incomplete
    _initial: Incomplete
    def __init__(self, characteristic, uuid, read: bool = ..., write: bool = ..., initial: Incomplete | None = ...) -> None: ...
    def _tuple(self): ...

def register_services(*services) -> None: ...
