"""
Module: 'umqtt.robust' on micropython-v1.19.1-esp32
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module (spiram) with ESP32', 'release': '1.19.1', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.19.1'}
# Stubber: 1.9.11
from typing import Any


class MQTTClient:
    DEBUG = False  # type: bool
    DELAY = 2  # type: int

    def ping(self, *args, **kwargs) -> Any:
        ...

    def check_msg(self, *args, **kwargs) -> Any:
        ...

    def delay(self, *args, **kwargs) -> Any:
        ...

    def subscribe(self, *args, **kwargs) -> Any:
        ...

    def disconnect(self, *args, **kwargs) -> Any:
        ...

    def connect(self, *args, **kwargs) -> Any:
        ...

    def set_last_will(self, *args, **kwargs) -> Any:
        ...

    def log(self, *args, **kwargs) -> Any:
        ...

    def set_callback(self, *args, **kwargs) -> Any:
        ...

    reconnect: Any  ## <class 'closure'> = <closure>
    wait_msg: Any  ## <class 'closure'> = <closure>
    publish: Any  ## <class 'closure'> = <closure>

    def __init__(self, *argv, **kwargs) -> None:
        ...
