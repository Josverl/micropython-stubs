"""
Module: 'urequests' on micropython-v1.18-esp8266
"""
# MCU: {'ver': 'v1.18', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '1.18', 'name': 'micropython', 'mpy': 9733, 'version': '1.18', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
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

    text: Any  ## <class 'property'> = <property>

    def json(self, *args, **kwargs) -> Any:
        ...

    content: Any  ## <class 'property'> = <property>


def request(*args, **kwargs) -> Any:
    ...


def post(*args, **kwargs) -> Any:
    ...


def patch(*args, **kwargs) -> Any:
    ...


def delete(*args, **kwargs) -> Any:
    ...
