from .core import ble as ble, ensure_active as ensure_active, log_error as log_error, log_info as log_info, log_warn as log_warn, register_irq_handler as register_irq_handler
from .device import Device as Device, DeviceConnection as DeviceConnection, DeviceTimeout as DeviceTimeout
from typing import Any

_IRQ_CENTRAL_CONNECT: Any
_IRQ_CENTRAL_DISCONNECT: Any
_ADV_TYPE_FLAGS: Any
_ADV_TYPE_NAME: Any
_ADV_TYPE_UUID16_COMPLETE: Any
_ADV_TYPE_UUID32_COMPLETE: Any
_ADV_TYPE_UUID128_COMPLETE: Any
_ADV_TYPE_UUID16_MORE: Any
_ADV_TYPE_UUID32_MORE: Any
_ADV_TYPE_UUID128_MORE: Any
_ADV_TYPE_APPEARANCE: Any
_ADV_TYPE_MANUFACTURER: Any
_ADV_PAYLOAD_MAX_LEN: Any
_incoming_connection: Any
_connect_event: Any

def _peripheral_irq(event, data) -> None: ...
def _peripheral_shutdown() -> None: ...
def _append(adv_data, resp_data, adv_type, value): ...
async def advertise(interval_us, adv_data: Any | None = ..., resp_data: Any | None = ..., connectable: bool = ..., limited_disc: bool = ..., br_edr: bool = ..., name: Any | None = ..., services: Any | None = ..., appearance: int = ..., manufacturer: Any | None = ..., timeout_ms: Any | None = ...): ...
