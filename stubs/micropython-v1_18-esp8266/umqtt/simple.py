"""
Module: 'umqtt.simple' on micropython-v1.18-esp8266
"""
# MCU: {'ver': 'v1.18', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '1.18', 'name': 'micropython', 'mpy': 9733, 'version': '1.18', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
# Stubber: 1.5.4
from typing import Any


def hexlify(*args, **kwargs) -> Any:
    ...


class MQTTException(Exception):
    """"""


class MQTTClient:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def connect(self, *args, **kwargs) -> Any:
        ...

    def disconnect(self, *args, **kwargs) -> Any:
        ...

    def set_callback(self, *args, **kwargs) -> Any:
        ...

    def set_last_will(self, *args, **kwargs) -> Any:
        ...

    def ping(self, *args, **kwargs) -> Any:
        ...

    def publish(self, *args, **kwargs) -> Any:
        ...

    def subscribe(self, *args, **kwargs) -> Any:
        ...

    def wait_msg(self, *args, **kwargs) -> Any:
        ...

    def check_msg(self, *args, **kwargs) -> Any:
        ...
