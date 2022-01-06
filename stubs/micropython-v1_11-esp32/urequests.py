"""
Module: 'urequests' on micropython-v1.11-esp32
"""
# MCU: {'ver': 'v1.11', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module with ESP32', 'release': '1.11.0', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.11.0'}
# Stubber: 1.5.0
from typing import Any


def get(*args) -> Any:
    ...


def put(*args) -> Any:
    ...


def head(*args) -> Any:
    ...


class Response:
    """"""

    def __init__(self, *args) -> None:
        ...

    def close(self, *args) -> Any:
        ...

    def json(self, *args) -> Any:
        ...

    text: Any  ## <class 'property'> = <property>
    content: Any  ## <class 'property'> = <property>


def request(*args) -> Any:
    ...


def post(*args) -> Any:
    ...


def patch(*args) -> Any:
    ...


def delete(*args) -> Any:
    ...
