"""
Module: 'urequests' on micropython-v1.18-esp32
"""
# MCU: {'ver': 'v1.18', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.18.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.18.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.5.4
from typing import Any


def get(*args, **kwargs) -> Any:
    ...


def put(*args, **kwargs) -> Any:
    ...


class Response:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def close(self, *args, **kwargs) -> Any:
        ...

    text: Any  ## <class 'property'> = <property>

    def json(self, *args, **kwargs) -> Any:
        ...

    content: Any  ## <class 'property'> = <property>


def request(*args, **kwargs) -> Any:
    ...


def head(*args, **kwargs) -> Any:
    ...


def post(*args, **kwargs) -> Any:
    ...


def patch(*args, **kwargs) -> Any:
    ...


def delete(*args, **kwargs) -> Any:
    ...
