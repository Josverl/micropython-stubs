"""
Module: 'umqtt.robust' on micropython-v1.11-esp32
"""
# MCU: {'ver': 'v1.11', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module with ESP32', 'release': '1.11.0', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.11.0'}
# Stubber: 1.5.0
from typing import Any


class MQTTClient:
    """"""

    def __init__(self, *args) -> None:
        ...

    DEBUG = False  # type: bool

    def connect(self, *args) -> Any:
        ...

    def disconnect(self, *args) -> Any:
        ...

    def log(self, *args) -> Any:
        ...

    DELAY = 2  # type: int

    def delay(self, *args) -> Any:
        ...

    reconnect: Any  ## <class 'closure'> = <closure>
    publish: Any  ## <class 'closure'> = <closure>
    wait_msg: Any  ## <class 'closure'> = <closure>

    def set_callback(self, *args) -> Any:
        ...

    def set_last_will(self, *args) -> Any:
        ...

    def ping(self, *args) -> Any:
        ...

    def subscribe(self, *args) -> Any:
        ...

    def check_msg(self, *args) -> Any:
        ...
