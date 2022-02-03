"""
Module: 'umqtt.robust' on micropython-v1.11-esp32
"""
# MCU: {'ver': 'v1.11', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module with ESP32', 'release': '1.11.0', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.11.0'}
# Stubber: 1.5.4
from typing import Any


class MQTTClient:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    DEBUG = False  # type: bool

    def connect(self, *args, **kwargs) -> Any:
        ...

    def disconnect(self, *args, **kwargs) -> Any:
        ...

    def log(self, *args, **kwargs) -> Any:
        ...

    DELAY = 2  # type: int

    def delay(self, *args, **kwargs) -> Any:
        ...

    reconnect: Any  ## <class 'closure'> = <closure>
    publish: Any  ## <class 'closure'> = <closure>
    wait_msg: Any  ## <class 'closure'> = <closure>

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
