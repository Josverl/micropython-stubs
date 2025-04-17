"""
Module: 'bluetooth' on micropython-v1.25.0-esp32-ESP32_GENERIC
"""

# MCU: {'version': '1.25.0', 'mpy': 'v6.3', 'port': 'esp32', 'board': 'ESP32_GENERIC', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': '1.25.0', 'cpu': 'ESP32'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Final
from _typeshed import Incomplete

FLAG_NOTIFY: Final[int] = 16
FLAG_READ: Final[int] = 2
FLAG_WRITE: Final[int] = 8
FLAG_INDICATE: Final[int] = 32
FLAG_WRITE_NO_RESPONSE: Final[int] = 4

class UUID:
    def __init__(self, *argv, **kwargs) -> None: ...

class BLE:
    def gattc_write(self, *args, **kwargs) -> Incomplete: ...
    def gatts_indicate(self, *args, **kwargs) -> Incomplete: ...
    def gattc_discover_services(self, *args, **kwargs) -> Incomplete: ...
    def gattc_read(self, *args, **kwargs) -> Incomplete: ...
    def gattc_exchange_mtu(self, *args, **kwargs) -> Incomplete: ...
    def gatts_set_buffer(self, *args, **kwargs) -> Incomplete: ...
    def gatts_write(self, *args, **kwargs) -> Incomplete: ...
    def gatts_notify(self, *args, **kwargs) -> Incomplete: ...
    def gatts_register_services(self, *args, **kwargs) -> Incomplete: ...
    def gatts_read(self, *args, **kwargs) -> Incomplete: ...
    def irq(self, *args, **kwargs) -> Incomplete: ...
    def gap_advertise(self, *args, **kwargs) -> Incomplete: ...
    def gap_connect(self, *args, **kwargs) -> Incomplete: ...
    def gattc_discover_descriptors(self, *args, **kwargs) -> Incomplete: ...
    def config(self, *args, **kwargs) -> Incomplete: ...
    def active(self, *args, **kwargs) -> Incomplete: ...
    def gap_scan(self, *args, **kwargs) -> Incomplete: ...
    def gattc_discover_characteristics(self, *args, **kwargs) -> Incomplete: ...
    def gap_disconnect(self, *args, **kwargs) -> Incomplete: ...
    def gap_passkey(self, *args, **kwargs) -> Incomplete: ...
    def gap_pair(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
