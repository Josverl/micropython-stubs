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
from micropython import const as const

_registered_characteristics: Incomplete
_IRQ_GATTS_WRITE: int
_IRQ_GATTS_READ_REQUEST: int
_IRQ_GATTS_INDICATE_DONE: int
_FLAG_READ: int
_FLAG_WRITE_NO_RESPONSE: int
_FLAG_WRITE: int
_FLAG_NOTIFY: int
_FLAG_INDICATE: int
_FLAG_READ_ENCRYPTED: int
_FLAG_READ_AUTHENTICATED: int
_FLAG_READ_AUTHORIZED: int
_FLAG_WRITE_ENCRYPTED: int
_FLAG_WRITE_AUTHENTICATED: int
_FLAG_WRITE_AUTHORIZED: int
_FLAG_WRITE_CAPTURE: int
_WRITE_CAPTURE_QUEUE_LIMIT: int

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
