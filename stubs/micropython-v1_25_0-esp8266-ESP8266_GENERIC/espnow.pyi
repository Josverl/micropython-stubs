"""
Module: 'espnow' on micropython-v1.25.0-esp8266-ESP8266_GENERIC
"""
# MCU: {'version': '1.25.0', 'mpy': 'v6.3', 'port': 'esp8266', 'board': 'ESP8266_GENERIC', 'family': 'micropython', 'build': '', 'arch': 'xtensa', 'ver': '1.25.0', 'cpu': 'ESP8266'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

MAX_ENCRYPT_PEER_NUM: Final[int] = 6
MAX_DATA_LEN: Final[int] = 250
MAX_TOTAL_PEER_NUM: Final[int] = 20
POLLIN: Final[int] = 1
ADDR_LEN: Final[int] = 6
KEY_LEN: Final[int] = 16
def poll(*args, **kwargs) -> Incomplete:
    ...


class ESPNow():
    _data: list = []
    _none_tuple: tuple = ()
    def irecv(self, *args, **kwargs) -> Incomplete:
        ...

    def recv(self, *args, **kwargs) -> Incomplete:
        ...

    def recvinto(self, *args, **kwargs) -> Incomplete:
        ...

    def set_pmk(self, *args, **kwargs) -> Incomplete:
        ...

    def send(self, *args, **kwargs) -> Incomplete:
        ...

    def del_peer(self, *args, **kwargs) -> Incomplete:
        ...

    def any(self, *args, **kwargs) -> Incomplete:
        ...

    def config(self, *args, **kwargs) -> Incomplete:
        ...

    def active(self, *args, **kwargs) -> Incomplete:
        ...

    def add_peer(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class ESPNowBase():
    def del_peer(self, *args, **kwargs) -> Incomplete:
        ...

    def config(self, *args, **kwargs) -> Incomplete:
        ...

    def recvinto(self, *args, **kwargs) -> Incomplete:
        ...

    def set_pmk(self, *args, **kwargs) -> Incomplete:
        ...

    def send(self, *args, **kwargs) -> Incomplete:
        ...

    def add_peer(self, *args, **kwargs) -> Incomplete:
        ...

    def active(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

