"""
Module: 'umqtt.robust' on micropython-v1.20.0-esp32-GENERIC_S3
"""

# MCU: OrderedDict({'version': '1.20.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'GENERIC_S3', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': 'v1.20.0', 'cpu': 'ESP32S3'})
# Stubber: v1.13.7
from typing import Any


class MQTTClient:
    DELAY = 2  # type: int
    DEBUG = False  # type: bool

    def ping(self, *args, **kwargs) -> Any: ...

    def set_last_will(self, *args, **kwargs) -> Any: ...

    def set_callback(self, *args, **kwargs) -> Any: ...

    def subscribe(self, *args, **kwargs) -> Any: ...

    def delay(self, *args, **kwargs) -> Any: ...

    def log(self, *args, **kwargs) -> Any: ...

    def disconnect(self, *args, **kwargs) -> Any: ...

    def connect(self, *args, **kwargs) -> Any: ...

    check_msg: Any  ## <class 'closure'> = <closure>
    reconnect: Any  ## <class 'closure'> = <closure>
    publish: Any  ## <class 'closure'> = <closure>
    wait_msg: Any  ## <class 'closure'> = <closure>

    def __init__(self, *argv, **kwargs) -> None: ...
