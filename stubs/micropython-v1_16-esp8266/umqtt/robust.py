"""
Module: 'umqtt.robust' on micropython-v1.16-esp8266
"""
# MCU: {'ver': 'v1.16', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '1.16', 'name': 'micropython', 'mpy': 9733, 'version': '1.16', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
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
