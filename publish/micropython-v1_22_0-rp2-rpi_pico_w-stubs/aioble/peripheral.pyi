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
from micropython import const as const

_IRQ_CENTRAL_CONNECT: int
_IRQ_CENTRAL_DISCONNECT: int
_ADV_TYPE_FLAGS: int
_ADV_TYPE_NAME: int
_ADV_TYPE_UUID16_COMPLETE: int
_ADV_TYPE_UUID32_COMPLETE: int
_ADV_TYPE_UUID128_COMPLETE: int
_ADV_TYPE_UUID16_MORE: int
_ADV_TYPE_UUID32_MORE: int
_ADV_TYPE_UUID128_MORE: int
_ADV_TYPE_APPEARANCE: int
_ADV_TYPE_MANUFACTURER: int
_ADV_PAYLOAD_MAX_LEN: int
_incoming_connection: Incomplete
_connect_event: Incomplete

def _peripheral_irq(event, data) -> None: ...
def _peripheral_shutdown() -> None: ...
def _append(adv_data, resp_data, adv_type, value): ...
async def advertise(
    interval_us,
    adv_data: Incomplete | None = ...,
    resp_data: Incomplete | None = ...,
    connectable: bool = ...,
    limited_disc: bool = ...,
    br_edr: bool = ...,
    name: Incomplete | None = ...,
    services: Incomplete | None = ...,
    appearance: int = ...,
    manufacturer: Incomplete | None = ...,
    timeout_ms: Incomplete | None = ...,
): ...
