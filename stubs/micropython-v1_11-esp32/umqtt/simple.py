"""
Module: 'umqtt.simple' on micropython-esp32-1.11
"""
# MCU: {'ver': '1.11', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module with ESP32', 'release': '1.11.0', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.11.0'}
# Stubber: 1.4.2
from typing import Any

def hexlify(*args) -> Any:
    ...

# import socket
# import struct

class MQTTClient:
    ''
    def __init__(self, *args) -> None:
        ...

    def connect(self, *args) -> Any:
        ...

    def disconnect(self, *args) -> Any:
        ...

    def publish(self, *args) -> Any:
        ...

    def wait_msg(self, *args) -> Any:
        ...

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


class MQTTException:
    ''
