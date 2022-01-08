"""
Module: 'umqtt.robust' on micropython-v1.17-esp32
"""
# MCU: {'ver': 'v1.17', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.17.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.17.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.5.0
from typing import Any


class MQTTClient:
    """"""

    def __init__(self, *args) -> None:
        ...

    def connect(self, *args) -> Any:
        ...

    def disconnect(self, *args) -> Any:
        ...

    def log(self, *args) -> Any:
        ...

    DEBUG = False  # type: bool

    def set_callback(self, *args) -> Any:
        ...

    def set_last_will(self, *args) -> Any:
        ...

    def ping(self, *args) -> Any:
        ...

    publish: Any  ## <class 'closure'> = <closure>

    def subscribe(self, *args) -> Any:
        ...

    wait_msg: Any  ## <class 'closure'> = <closure>

    def check_msg(self, *args) -> Any:
        ...

    DELAY = 2  # type: int

    def delay(self, *args) -> Any:
        ...

    reconnect: Any  ## <class 'closure'> = <closure>
