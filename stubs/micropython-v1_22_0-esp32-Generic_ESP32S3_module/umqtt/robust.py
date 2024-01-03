"""
Module: 'umqtt.robust' on micropython-v1.22.0-esp32-Generic_ESP32S3_module
"""
# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'esp32', 'board': 'Generic_ESP32S3_module', 'cpu': 'ESP32S3', 'mpy': 'v6.2', 'arch': 'xtensawin'}
# Stubber: v1.16.2
from _typeshed import Incomplete


class MQTTClient:
    DEBUG = False  # type: bool
    DELAY = 2  # type: int

    def set_callback(self, *args, **kwargs) -> Incomplete:
        ...

    def set_last_will(self, *args, **kwargs) -> Incomplete:
        ...

    def delay(self, *args, **kwargs) -> Incomplete:
        ...

    def ping(self, *args, **kwargs) -> Incomplete:
        ...

    def subscribe(self, *args, **kwargs) -> Incomplete:
        ...

    def connect(self, *args, **kwargs) -> Incomplete:
        ...

    def disconnect(self, *args, **kwargs) -> Incomplete:
        ...

    def log(self, *args, **kwargs) -> Incomplete:
        ...

    def wait_msg(self, *args, **kwargs) -> Incomplete:
        ...

    def check_msg(self, *args, **kwargs) -> Incomplete:
        ...

    def reconnect(self, *args, **kwargs) -> Incomplete:
        ...

    def publish(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
