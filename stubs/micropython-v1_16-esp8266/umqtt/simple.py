"""
Module: 'umqtt.simple' on micropython-v1.16-esp8266
"""
# MCU: {'ver': 'v1.16', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '1.16', 'name': 'micropython', 'mpy': 9733, 'version': '1.16', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
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
