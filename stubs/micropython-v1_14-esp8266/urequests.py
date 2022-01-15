"""
Module: 'urequests' on micropython-v1.14-esp8266
"""
# MCU: {'ver': 'v1.14', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '1.14', 'name': 'micropython', 'mpy': 9733, 'version': '1.14', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
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
