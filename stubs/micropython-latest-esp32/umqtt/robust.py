"""
Module: 'umqtt.robust' on micropython-v1.20.0-449-esp32-Generic_ESP32_module_with_SPIRAM_with_ESP32
"""
# MCU: OrderedDict({'version': '1.20.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'Generic_ESP32_module_with_SPIRAM_with_ESP32', 'family': 'micropython', 'build': '449', 'arch': 'xtensawin', 'ver': 'v1.20.0-449', 'cpu': 'SPIRAM'})
# Stubber: v1.13.7
from typing import Any


class MQTTClient:
    DELAY = 2  # type: int
    DEBUG = False  # type: bool

    def ping(self, *args, **kwargs) -> Any:
        ...

    def set_last_will(self, *args, **kwargs) -> Any:
        ...

    def set_callback(self, *args, **kwargs) -> Any:
        ...

    def subscribe(self, *args, **kwargs) -> Any:
        ...

    def delay(self, *args, **kwargs) -> Any:
        ...

    def log(self, *args, **kwargs) -> Any:
        ...

    def disconnect(self, *args, **kwargs) -> Any:
        ...

    def connect(self, *args, **kwargs) -> Any:
        ...

    check_msg: Any  ## <class 'closure'> = <closure>
    reconnect: Any  ## <class 'closure'> = <closure>
    publish: Any  ## <class 'closure'> = <closure>
    wait_msg: Any  ## <class 'closure'> = <closure>

    def __init__(self, *argv, **kwargs) -> None:
        ...
