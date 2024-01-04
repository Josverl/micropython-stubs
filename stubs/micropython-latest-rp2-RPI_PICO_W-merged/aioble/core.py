"""
Module: 'aioble.core' on micropython-v1.22.0-rp2-RPI_PICO_W
"""
# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.2', 'arch': 'armv6m'}
# Stubber: v1.16.2
from _typeshed import Incomplete

log_level = 1  # type: int


def log_error(*args, **kwargs) -> Incomplete:
    ...


def ensure_active(*args, **kwargs) -> Incomplete:
    ...


def register_irq_handler(*args, **kwargs) -> Incomplete:
    ...


def log_info(*args, **kwargs) -> Incomplete:
    ...


def log_warn(*args, **kwargs) -> Incomplete:
    ...


def config(*args, **kwargs) -> Incomplete:
    ...


def stop(*args, **kwargs) -> Incomplete:
    ...


def ble_irq(*args, **kwargs) -> Incomplete:
    ...


ble: Incomplete  ## <class 'BLE'> = <BLE>


class GattError(Exception):
    ...
