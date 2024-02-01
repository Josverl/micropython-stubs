"""
Module: 'aioble.core' on micropython-v1.21.0-rp2-RPI_PICO_W
"""
# MCU: {'build': '', 'ver': 'v1.21.0', 'version': '1.21.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.13.8
from typing import Any
from _typeshed import Incomplete

log_level = 1  # type: int


def register_irq_handler(*args, **kwargs) -> Incomplete:
    ...


def log_error(*args, **kwargs) -> Incomplete:
    ...


def ble_irq(*args, **kwargs) -> Incomplete:
    ...


def ensure_active(*args, **kwargs) -> Incomplete:
    ...


def log_warn(*args, **kwargs) -> Incomplete:
    ...


def stop(*args, **kwargs) -> Incomplete:
    ...


def config(*args, **kwargs) -> Incomplete:
    ...


def log_info(*args, **kwargs) -> Incomplete:
    ...


ble: Incomplete  ## <class 'BLE'> = <BLE>


class GattError(Exception):
    ...
