"""
Module: 'aioble.core' on micropython-v1.19.1-rp2
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'sysname': 'rp2', 'platform': 'rp2', 'version': '1.19.1', 'release': '1.19.1', 'port': 'rp2', 'family': 'micropython', 'name': 'micropython', 'machine': 'Arduino Nano RP2040 Connect with RP2040', 'nodename': 'rp2'}
# Stubber: 1.9.11
from typing import Any

log_level = 1  # type: int


def log_error(*args, **kwargs) -> Any:
    ...


def ble_irq(*args, **kwargs) -> Any:
    ...


def ensure_active(*args, **kwargs) -> Any:
    ...


def register_irq_handler(*args, **kwargs) -> Any:
    ...


def log_warn(*args, **kwargs) -> Any:
    ...


def stop(*args, **kwargs) -> Any:
    ...


def config(*args, **kwargs) -> Any:
    ...


def log_info(*args, **kwargs) -> Any:
    ...


ble: Any  ## <class 'BLE'> = <BLE>


class GattError(Exception):
    ...
