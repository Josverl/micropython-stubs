"""
Module: 'urequests' on micropython-v1.18-esp8266
"""
# MCU: {'ver': 'v1.18', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '1.18', 'name': 'micropython', 'mpy': 9733, 'version': '1.18', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
# Stubber: 1.5.3
from typing import Any


def get(*args) -> Any:
    ...


def put(*args) -> Any:
    ...


def head(*args) -> Any:
    ...


class Response:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def close(self, *args) -> Any:
        ...

    text: Any  ## <class 'property'> = <property>

    def json(self, *args) -> Any:
        ...

    content: Any  ## <class 'property'> = <property>


def request(*args) -> Any:
    ...


def post(*args) -> Any:
    ...


def patch(*args) -> Any:
    ...


def delete(*args) -> Any:
    ...
