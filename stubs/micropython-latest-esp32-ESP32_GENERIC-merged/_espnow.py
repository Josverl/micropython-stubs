"""
ESP-NOW :doc:`asyncio` support.

MicroPython module: https://docs.micropython.org/en/latest/library/aioespnow.html

---
Module: '_espnow' on micropython-v1.21.0-esp32-Generic_ESP32_module_with_SPIRAM_with_ESP32
"""
# MCU: {'family': 'micropython', 'version': '1.21.0', 'build': '', 'ver': 'v1.21.0', 'port': 'esp32', 'board': 'Generic_ESP32_module_with_SPIRAM_with_ESP32', 'cpu': 'SPIRAM', 'mpy': 'v6.1', 'arch': 'xtensawin'}
# Stubber: v1.14.0
from _typeshed import Incomplete
from typing import Any, Dict, Iterator, List, Optional, Tuple, Union

MAX_DATA_LEN = 250  # type: int
MAX_TOTAL_PEER_NUM = 20  # type: int
MAX_ENCRYPT_PEER_NUM = 6  # type: int
ADDR_LEN = 6  # type: int
KEY_LEN = 16  # type: int


class ESPNowBase:
    def irq(self, *args, **kwargs) -> Incomplete:
        ...

    def mod_peer(self, *args, **kwargs) -> Incomplete:
        ...

    def get_peers(self, *args, **kwargs) -> Incomplete:
        ...

    def stats(self, *args, **kwargs) -> Incomplete:
        ...

    def set_pmk(self, *args, **kwargs) -> Incomplete:
        ...

    def peer_count(self, *args, **kwargs) -> Incomplete:
        ...

    def recvinto(self, *args, **kwargs) -> Incomplete:
        ...

    def send(self, *args, **kwargs) -> Incomplete:
        ...

    def active(self, *args, **kwargs) -> Incomplete:
        ...

    def any(self, *args, **kwargs) -> Incomplete:
        ...

    def get_peer(self, *args, **kwargs) -> Incomplete:
        ...

    def del_peer(self, *args, **kwargs) -> Incomplete:
        ...

    def add_peer(self, *args, **kwargs) -> Incomplete:
        ...

    def config(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
