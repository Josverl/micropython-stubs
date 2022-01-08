"""
Module: 'esp' on micropython-v1.15-esp8266
"""
# MCU: {'ver': 'v1.15', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '1.15', 'name': 'micropython', 'mpy': 9733, 'version': '1.15', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
# Stubber: 1.5.0
from typing import Any

SLEEP_LIGHT = 1  # type: int
SLEEP_MODEM = 2  # type: int
SLEEP_NONE = 0  # type: int


def apa102_write(*args) -> Any:
    ...


def check_fw(*args) -> Any:
    ...


def deepsleep(*args) -> Any:
    ...


def dht_readinto(*args) -> Any:
    ...


def esf_free_bufs(*args) -> Any:
    ...


def flash_erase(*args) -> Any:
    ...


def flash_id(*args) -> Any:
    ...


def flash_read(*args) -> Any:
    ...


def flash_size(*args) -> Any:
    ...


def flash_user_start(*args) -> Any:
    ...


def flash_write(*args) -> Any:
    ...


def free(*args) -> Any:
    ...


def freemem(*args) -> Any:
    ...


def info(*args) -> Any:
    ...


def malloc(*args) -> Any:
    ...


def meminfo(*args) -> Any:
    ...


def neopixel_write(*args) -> Any:
    ...


def osdebug(*args) -> Any:
    ...


def set_native_code_location(*args) -> Any:
    ...


def sleep_type(*args) -> Any:
    ...
