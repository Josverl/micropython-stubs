"""
Module: 'urequests' on micropython-v1.10-esp32
"""
# MCU: {'ver': 'v1.10', 'build': '', 'platform': 'esp32', 'port': 'esp32', 'machine': 'ESP32 module with ESP32', 'release': '1.10.0', 'nodename': 'esp32', 'name': 'micropython', 'family': 'micropython', 'sysname': 'esp32', 'version': '1.10.0'}
# Stubber: 1.5.4
from typing import Any


def get(*args, **kwargs) -> Any:
    ...


def put(*args, **kwargs) -> Any:
    ...


def head(*args, **kwargs) -> Any:
    ...


class Response:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def close(self, *args, **kwargs) -> Any:
        ...

    def json(self, *args, **kwargs) -> Any:
        ...

    text: Any  ## <class 'property'> = <property>
    content: Any  ## <class 'property'> = <property>


def request(*args, **kwargs) -> Any:
    ...


def post(*args, **kwargs) -> Any:
    ...


def patch(*args, **kwargs) -> Any:
    ...


def delete(*args, **kwargs) -> Any:
    ...
