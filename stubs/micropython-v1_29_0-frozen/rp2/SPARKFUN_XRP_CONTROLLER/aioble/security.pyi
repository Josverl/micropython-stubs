# Micropython v1.29.0 frozen stubs
from _typeshed import Incomplete
from micropython import const as const

from .core import ble as ble
from .core import log_info as log_info
from .core import log_warn as log_warn
from .core import register_irq_handler as register_irq_handler
from .device import DeviceConnection as DeviceConnection

_IRQ_ENCRYPTION_UPDATE: int
_IRQ_GET_SECRET: int
_IRQ_SET_SECRET: int
_IRQ_PASSKEY_ACTION: int
_IO_CAPABILITY_DISPLAY_ONLY: int
_IO_CAPABILITY_DISPLAY_YESNO: int
_IO_CAPABILITY_KEYBOARD_ONLY: int
_IO_CAPABILITY_NO_INPUT_OUTPUT: int
_IO_CAPABILITY_KEYBOARD_DISPLAY: int
_PASSKEY_ACTION_INPUT: int
_PASSKEY_ACTION_DISP: int
_PASSKEY_ACTION_NUMCMP: int
_DEFAULT_PATH: str
_secrets: Incomplete
_modified: bool
_path: Incomplete

def load_secrets(path=None) -> None: ...
def _save_secrets(arg=None) -> None: ...
def _security_irq(event, data): ...
def _security_shutdown() -> None: ...
async def pair(connection, bond: bool = True, le_secure: bool = True, mitm: bool = False, io=..., timeout_ms: int = 20000) -> None: ...
