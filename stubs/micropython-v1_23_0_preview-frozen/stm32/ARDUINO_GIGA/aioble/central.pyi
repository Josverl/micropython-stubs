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

_IRQ_SCAN_RESULT: Incomplete
_IRQ_SCAN_DONE: Incomplete
_IRQ_PERIPHERAL_CONNECT: Incomplete
_IRQ_PERIPHERAL_DISCONNECT: Incomplete
_ADV_IND: Incomplete
_ADV_DIRECT_IND: Incomplete
_ADV_SCAN_IND: Incomplete
_ADV_NONCONN_IND: Incomplete
_SCAN_RSP: Incomplete
_ADV_TYPE_FLAGS: Incomplete
_ADV_TYPE_NAME: Incomplete
_ADV_TYPE_SHORT_NAME: Incomplete
_ADV_TYPE_UUID16_INCOMPLETE: Incomplete
_ADV_TYPE_UUID16_COMPLETE: Incomplete
_ADV_TYPE_UUID32_INCOMPLETE: Incomplete
_ADV_TYPE_UUID32_COMPLETE: Incomplete
_ADV_TYPE_UUID128_INCOMPLETE: Incomplete
_ADV_TYPE_UUID128_COMPLETE: Incomplete
_ADV_TYPE_APPEARANCE: Incomplete
_ADV_TYPE_MANUFACTURER: Incomplete
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
