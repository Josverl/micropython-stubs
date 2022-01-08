from .core import ble as ble, ensure_active as ensure_active, log_error as log_error, log_info as log_info, log_warn as log_warn, register_irq_handler as register_irq_handler
from .device import Device as Device, DeviceConnection as DeviceConnection, DeviceTimeout as DeviceTimeout
from collections.abc import Generator
from typing import Any

_IRQ_SCAN_RESULT: Any
_IRQ_SCAN_DONE: Any
_IRQ_PERIPHERAL_CONNECT: Any
_IRQ_PERIPHERAL_DISCONNECT: Any
_ADV_IND: Any
_ADV_DIRECT_IND: Any
_ADV_SCAN_IND: Any
_ADV_NONCONN_IND: Any
_SCAN_RSP: Any
_ADV_TYPE_FLAGS: Any
_ADV_TYPE_NAME: Any
_ADV_TYPE_UUID16_INCOMPLETE: Any
_ADV_TYPE_UUID16_COMPLETE: Any
_ADV_TYPE_UUID32_INCOMPLETE: Any
_ADV_TYPE_UUID32_COMPLETE: Any
_ADV_TYPE_UUID128_INCOMPLETE: Any
_ADV_TYPE_UUID128_COMPLETE: Any
_ADV_TYPE_APPEARANCE: Any
_ADV_TYPE_MANUFACTURER: Any
_active_scanner: Any
_connecting: Any

def _central_irq(event, data) -> None: ...
def _central_shutdown() -> None: ...
async def _cancel_pending() -> None: ...
async def _connect(connection, timeout_ms) -> None: ...

class ScanResult:
    device: Any
    adv_data: Any
    resp_data: Any
    rssi: Any
    connectable: bool
    def __init__(self, device) -> None: ...
    def _update(self, adv_type, rssi, adv_data): ...
    def __str__(self): ...
    def _decode_field(self, *adv_type) -> Generator[Any, None, None]: ...
    def name(self): ...
    def services(self) -> Generator[Any, None, None]: ...
    def manufacturer(self, filter: Any | None = ...) -> Generator[Any, None, None]: ...

class scan:
    _queue: Any
    _event: Any
    _done: bool
    _results: Any
    _duration_ms: Any
    _interval_us: Any
    _window_us: Any
    _active: Any
    def __init__(self, duration_ms, interval_us: Any | None = ..., window_us: Any | None = ..., active: bool = ...) -> None: ...
    async def __aenter__(self): ...
    async def __aexit__(self, exc_type, exc_val, exc_traceback) -> None: ...
    def __aiter__(self): ...
    async def __anext__(self): ...
    async def cancel(self) -> None: ...
