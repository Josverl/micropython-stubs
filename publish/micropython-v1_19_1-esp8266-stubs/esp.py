"""
Module: 'esp' on micropython-v1.19.1-esp8266
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp8266', 'port': 'esp8266', 'machine': 'ESP module (1M) with ESP8266', 'release': '1.19.1', 'nodename': 'esp8266', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp8266', 'version': '1.19.1'}
# Stubber: 1.5.6
from typing import Any

SLEEP_LIGHT = 1  # type: int
SLEEP_MODEM = 2  # type: int
SLEEP_NONE = 0  # type: int


def apa102_write(*args, **kwargs) -> Any:
    ...


def check_fw(*args, **kwargs) -> Any:
    ...


def deepsleep(*args, **kwargs) -> Any:
    ...


def dht_readinto(*args, **kwargs) -> Any:
    ...


def esf_free_bufs(*args, **kwargs) -> Any:
    ...


def flash_erase(*args, **kwargs) -> Any:
    ...


def flash_id(*args, **kwargs) -> Any:
    ...


def flash_read(*args, **kwargs) -> Any:
    ...


def flash_size(*args, **kwargs) -> Any:
    ...


def flash_user_start(*args, **kwargs) -> Any:
    ...


def flash_write(*args, **kwargs) -> Any:
    ...


def free(*args, **kwargs) -> Any:
    ...


def freemem(*args, **kwargs) -> Any:
    ...


def malloc(*args, **kwargs) -> Any:
    ...


def meminfo(*args, **kwargs) -> Any:
    ...


def osdebug(*args, **kwargs) -> Any:
    ...


def set_native_code_location(*args, **kwargs) -> Any:
    ...


def sleep_type(*args, **kwargs) -> Any:
    ...
