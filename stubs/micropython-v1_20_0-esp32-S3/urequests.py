"""
Module: 'urequests' on micropython-v1.20.0-esp32-GENERIC_S3
"""
# MCU: OrderedDict({'version': '1.20.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'GENERIC_S3', 'family': 'micropython', 'build': '', 'arch': 'xtensawin', 'ver': 'v1.20.0', 'cpu': 'ESP32S3'})
# Stubber: v1.13.7
from typing import Any


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


def put(*args, **kwargs) -> Any:
    ...


def get(*args, **kwargs) -> Any:
    ...


class Response:
    def json(self, *args, **kwargs) -> Any:
        ...

    def close(self, *args, **kwargs) -> Any:
        ...

    text: Any  ## <class 'property'> = <property>
    content: Any  ## <class 'property'> = <property>

    def __init__(self, *argv, **kwargs) -> None:
        ...
