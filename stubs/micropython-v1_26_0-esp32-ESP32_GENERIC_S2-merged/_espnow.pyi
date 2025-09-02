"""
Module: '_espnow' on micropython-v1.26.0-esp32-ESP32_GENERIC_S2
"""
# MCU: {'variant': '', 'build': '', 'arch': 'xtensawin', 'port': 'esp32', 'board': 'ESP32_GENERIC_S2', 'board_id': 'ESP32_GENERIC_S2', 'mpy': 'v6.3', 'ver': '1.26.0', 'family': 'micropython', 'cpu': 'ESP32S2', 'version': '1.26.0'}
# Stubber: v1.26.1
from __future__ import annotations
from typing import Final
from _typeshed import Incomplete

MAX_DATA_LEN: Final[int] = 250
MAX_TOTAL_PEER_NUM: Final[int] = 20
MAX_ENCRYPT_PEER_NUM: Final[int] = 6
ADDR_LEN: Final[int] = 6
KEY_LEN: Final[int] = 16

class ESPNowBase():
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

