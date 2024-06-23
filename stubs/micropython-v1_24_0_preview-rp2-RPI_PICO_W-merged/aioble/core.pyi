"""
Module: 'aioble.core' on micropython-v1.24.0-preview-rp2-RPI_PICO_W
"""

# MCU: {'build': 'preview.60.gcebc9b0ae', 'ver': '1.24.0-preview-preview.60.gcebc9b0ae', 'version': '1.24.0-preview', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.3', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.20.0
from __future__ import annotations
from _typeshed import Incomplete

_irq_handlers: list = []
_shutdown_handlers: list = []
log_level: int = 1

def ensure_active(*args, **kwargs) -> Incomplete: ...
def register_irq_handler(*args, **kwargs) -> Incomplete: ...
def log_warn(*args, **kwargs) -> Incomplete: ...
def log_error(*args, **kwargs) -> Incomplete: ...
def log_info(*args, **kwargs) -> Incomplete: ...
def config(*args, **kwargs) -> Incomplete: ...
def stop(*args, **kwargs) -> Incomplete: ...
def ble_irq(*args, **kwargs) -> Incomplete: ...

ble: Incomplete  ## <class 'BLE'> = <BLE>

class GattError(Exception): ...
