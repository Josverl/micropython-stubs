"""
Module: 'umqtt.robust' on micropython-v1.26.0-esp32-ESP32_GENERIC_S2
"""
# MCU: {'variant': '', 'build': '', 'arch': 'xtensawin', 'port': 'esp32', 'board': 'ESP32_GENERIC_S2', 'board_id': 'ESP32_GENERIC_S2', 'mpy': 'v6.3', 'ver': '1.26.0', 'family': 'micropython', 'cpu': 'ESP32S2', 'version': '1.26.0'}
# Stubber: v1.26.1
from __future__ import annotations
from typing import Final
from _typeshed import Incomplete


class MQTTClient():
    DELAY: Final[int] = 2
    DEBUG: Final[bool] = False
    def subscribe(self, *args, **kwargs) -> Incomplete:
        ...

    def set_callback(self, *args, **kwargs) -> Incomplete:
        ...

    def set_last_will(self, *args, **kwargs) -> Incomplete:
        ...

    def delay(self, *args, **kwargs) -> Incomplete:
        ...

    def ping(self, *args, **kwargs) -> Incomplete:
        ...

    def disconnect(self, *args, **kwargs) -> Incomplete:
        ...

    def connect(self, *args, **kwargs) -> Incomplete:
        ...

    def _send_str(self, *args, **kwargs) -> Incomplete:
        ...

    def log(self, *args, **kwargs) -> Incomplete:
        ...

    def _recv_len(self, *args, **kwargs) -> Incomplete:
        ...

    def wait_msg(self, *args, **kwargs) -> Incomplete:
        ...

    def check_msg(self, *args, **kwargs) -> Incomplete:
        ...

    def reconnect(self, *args, **kwargs) -> Incomplete:
        ...

    def publish(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

