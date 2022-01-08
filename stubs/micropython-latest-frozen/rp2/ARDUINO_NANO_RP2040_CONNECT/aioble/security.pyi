from .core import ble as ble, log_info as log_info, log_warn as log_warn, register_irq_handler as register_irq_handler
from .device import DeviceConnection as DeviceConnection
from typing import Any

_IRQ_ENCRYPTION_UPDATE: Any
_IRQ_GET_SECRET: Any
_IRQ_SET_SECRET: Any
_IRQ_PASSKEY_ACTION: Any
_IO_CAPABILITY_DISPLAY_ONLY: Any
_IO_CAPABILITY_DISPLAY_YESNO: Any
_IO_CAPABILITY_KEYBOARD_ONLY: Any
_IO_CAPABILITY_NO_INPUT_OUTPUT: Any
_IO_CAPABILITY_KEYBOARD_DISPLAY: Any
_PASSKEY_ACTION_INPUT: Any
_PASSKEY_ACTION_DISP: Any
_PASSKEY_ACTION_NUMCMP: Any
_DEFAULT_PATH: str
_secrets: Any
_modified: bool
_path: Any

def load_secrets(path: Any | None = ...) -> None: ...
def _save_secrets(arg: Any | None = ...) -> None: ...
def _security_irq(event, data): ...
def _security_shutdown() -> None: ...
async def pair(connection, bond: bool = ..., le_secure: bool = ..., mitm: bool = ..., io=..., timeout_ms: int = ...) -> None: ...
