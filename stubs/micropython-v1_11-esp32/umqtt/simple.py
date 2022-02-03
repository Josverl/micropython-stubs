"""
Module: 'umqtt.simple' on micropython-v1.11-esp32
"""
# MCU: {'ver': 'v1.11', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module with ESP32', 'release': '1.11.0', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.11.0'}
# Stubber: 1.5.4
from typing import Any


def hexlify(*args, **kwargs) -> Any:
    ...


class MQTTClient:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def connect(self, *args, **kwargs) -> Any:
        ...

    def disconnect(self, *args, **kwargs) -> Any:
        ...

    def publish(self, *args, **kwargs) -> Any:
        ...

    def wait_msg(self, *args, **kwargs) -> Any:
        ...

    def set_callback(self, *args, **kwargs) -> Any:
        ...

    def set_last_will(self, *args, **kwargs) -> Any:
        ...

    def ping(self, *args, **kwargs) -> Any:
        ...

    def subscribe(self, *args, **kwargs) -> Any:
        ...

    def check_msg(self, *args, **kwargs) -> Any:
        ...


class MQTTException(Exception):
    """"""
