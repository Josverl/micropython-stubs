from .core import ble as ble, log_info as log_info, log_warn as log_warn, register_irq_handler as register_irq_handler
from .device import DeviceConnection as DeviceConnection
from _typeshed import Incomplete
from micropython import const as const

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

def load_secrets(path: Incomplete | None = ...) -> None: ...
def _save_secrets(arg: Incomplete | None = ...) -> None: ...
def _security_irq(event, data): ...
def _security_shutdown() -> None: ...
async def pair(connection, bond: bool = ..., le_secure: bool = ..., mitm: bool = ..., io=..., timeout_ms: int = ...) -> None: ...
