"""
Module: 'umqtt.simple' on micropython-v1.13-266-esp32
"""
# MCU: {'ver': 'v1.13-266', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.13.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.13.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '266', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.5.0
from typing import Any


def hexlify(*args) -> Any:
    ...


class MQTTException(Exception):
    """"""


class MQTTClient:
    """"""

    def __init__(self, *args) -> None:
        ...

    def connect(self, *args) -> Any:
        ...

    def disconnect(self, *args) -> Any:
        ...

    def set_callback(self, *args) -> Any:
        ...

    def set_last_will(self, *args) -> Any:
        ...

    def ping(self, *args) -> Any:
        ...

    def publish(self, *args) -> Any:
        ...

    def subscribe(self, *args) -> Any:
        ...

    def wait_msg(self, *args) -> Any:
        ...

    def check_msg(self, *args) -> Any:
        ...
