"""
Module: 'urequests' on micropython-v1.20.0-449-esp32-Generic_ESP32_module_with_SPIRAM_with_ESP32
"""
# MCU: OrderedDict({'version': '1.20.0', 'mpy': 'v6.1', 'port': 'esp32', 'board': 'Generic_ESP32_module_with_SPIRAM_with_ESP32', 'family': 'micropython', 'build': '449', 'arch': 'xtensawin', 'ver': 'v1.20.0-449', 'cpu': 'SPIRAM'})
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

    content: Any  ## <class 'property'> = <property>
    text: Any  ## <class 'property'> = <property>

    def __init__(self, *argv, **kwargs) -> None:
        ...
