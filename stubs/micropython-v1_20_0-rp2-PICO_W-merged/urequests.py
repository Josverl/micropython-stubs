"""
Module: 'urequests' on micropython-v1.20-rp2-PICO_W
"""
# MCU: OrderedDict({'family': 'micropython', 'version': '1.20', 'build': '', 'ver': 'v1.20', 'port': 'rp2', 'board': 'PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.1', 'arch': 'armv6m'})
# Stubber: v1.12.2
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
