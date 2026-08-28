# Micropython v1.29.0 frozen stubs
from _typeshed import Incomplete
from micropython import const as const

from .core import ble as ble
from .core import ensure_active as ensure_active
from .core import log_error as log_error
from .core import log_info as log_info
from .core import log_warn as log_warn
from .core import register_irq_handler as register_irq_handler
from .device import Device as Device
from .device import DeviceConnection as DeviceConnection
from .device import DeviceTimeout as DeviceTimeout

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
    adv_data=None,
    resp_data=None,
    connectable: bool = True,
    limited_disc: bool = False,
    br_edr: bool = False,
    name=None,
    services=None,
    appearance: int = 0,
    manufacturer=None,
    timeout_ms=None,
): ...
