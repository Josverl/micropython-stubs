"""
Module: 'umqtt.robust' on micropython-v1.13-266-esp32
"""
# MCU: {'ver': 'v1.13-266', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.13.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.13.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '266', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.5.4
from typing import Any


class MQTTClient:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def connect(self, *args, **kwargs) -> Any:
        ...

    def disconnect(self, *args, **kwargs) -> Any:
        ...

    def log(self, *args, **kwargs) -> Any:
        ...

    DEBUG = False  # type: bool

    def set_callback(self, *args, **kwargs) -> Any:
        ...

    def set_last_will(self, *args, **kwargs) -> Any:
        ...

    def ping(self, *args, **kwargs) -> Any:
        ...

    publish: Any  ## <class 'closure'> = <closure>

    def subscribe(self, *args, **kwargs) -> Any:
        ...

    wait_msg: Any  ## <class 'closure'> = <closure>

    def check_msg(self, *args, **kwargs) -> Any:
        ...

    DELAY = 2  # type: int

    def delay(self, *args, **kwargs) -> Any:
        ...

    reconnect: Any  ## <class 'closure'> = <closure>
