"""
Module: 'umqtt.robust' on micropython-v1.24.1-esp8266-ESP8266_GENERIC
"""

# MCU: {'variant': '', 'build': '', 'arch': 'xtensa', 'port': 'esp8266', 'board': 'ESP8266_GENERIC', 'board_id': 'ESP8266_GENERIC', 'mpy': 'v6.3', 'ver': '1.24.1', 'family': 'micropython', 'cpu': 'ESP8266', 'version': '1.24.1'}
# Stubber: v1.25.0
from __future__ import annotations
from typing import Final
from _typeshed import Incomplete

class MQTTClient:
    DELAY: Final[int] = 2
    DEBUG: Final[bool] = False
    def subscribe(self, *args, **kwargs) -> Incomplete: ...
    def set_callback(self, *args, **kwargs) -> Incomplete: ...
    def set_last_will(self, *args, **kwargs) -> Incomplete: ...
    def delay(self, *args, **kwargs) -> Incomplete: ...
    def ping(self, *args, **kwargs) -> Incomplete: ...
    def disconnect(self, *args, **kwargs) -> Incomplete: ...
    def connect(self, *args, **kwargs) -> Incomplete: ...
    def _send_str(self, *args, **kwargs) -> Incomplete: ...
    def log(self, *args, **kwargs) -> Incomplete: ...
    def _recv_len(self, *args, **kwargs) -> Incomplete: ...
    def wait_msg(self, *args, **kwargs) -> Incomplete: ...
    def check_msg(self, *args, **kwargs) -> Incomplete: ...
    def reconnect(self, *args, **kwargs) -> Incomplete: ...
    def publish(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
