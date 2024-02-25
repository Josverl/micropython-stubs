from .core import (
    ble as ble,
    ensure_active as ensure_active,
    log_error as log_error,
    log_info as log_info,
    log_warn as log_warn,
    register_irq_handler as register_irq_handler,
)
from .device import Device as Device, DeviceConnection as DeviceConnection, DeviceTimeout as DeviceTimeout
from _typeshed import Incomplete
from collections.abc import Generator
from micropython import const as const

_IRQ_SCAN_RESULT: int
_IRQ_SCAN_DONE: int
_IRQ_PERIPHERAL_CONNECT: int
_IRQ_PERIPHERAL_DISCONNECT: int
_ADV_IND: int
_ADV_DIRECT_IND: int
_ADV_SCAN_IND: int
_ADV_NONCONN_IND: int
_SCAN_RSP: int
_ADV_TYPE_FLAGS: int
_ADV_TYPE_NAME: int
_ADV_TYPE_SHORT_NAME: int
_ADV_TYPE_UUID16_INCOMPLETE: int
_ADV_TYPE_UUID16_COMPLETE: int
_ADV_TYPE_UUID32_INCOMPLETE: int
_ADV_TYPE_UUID32_COMPLETE: int
_ADV_TYPE_UUID128_INCOMPLETE: int
_ADV_TYPE_UUID128_COMPLETE: int
_ADV_TYPE_APPEARANCE: int
_ADV_TYPE_MANUFACTURER: int
_active_scanner: Incomplete
_connecting: Incomplete

def _central_irq(event, data) -> None: ...
def _central_shutdown() -> None: ...
async def _cancel_pending() -> None: ...
async def _connect(connection, timeout_ms) -> None: ...

class ScanResult:
    device: Incomplete
    adv_data: Incomplete
    resp_data: Incomplete
    rssi: Incomplete
    connectable: bool
    def __init__(self, device) -> None: ...
    def _update(self, adv_type, rssi, adv_data): ...
    def __str__(self) -> str: ...
    def _decode_field(self, *adv_type) -> Generator[Incomplete, None, None]: ...
    def name(self): ...
    def services(self) -> Generator[Incomplete, None, None]: ...
    def manufacturer(self, filter: Incomplete | None = ...) -> Generator[Incomplete, None, None]: ...

class scan:
    _queue: Incomplete
    _event: Incomplete
    _done: bool
    _results: Incomplete
    _duration_ms: Incomplete
    _interval_us: Incomplete
    _window_us: Incomplete
    _active: Incomplete
    def __init__(
        self, duration_ms, interval_us: Incomplete | None = ..., window_us: Incomplete | None = ..., active: bool = ...
    ) -> None: ...
    async def __aenter__(self): ...
    async def __aexit__(self, exc_type, exc_val, exc_traceback) -> None: ...
    def __aiter__(self): ...
    async def __anext__(self): ...
    async def cancel(self) -> None: ...
