"""
Module: 'requests.__init__' on micropython-v1.27.0-esp32-ESP32_GENERIC_S3
"""
# MCU: {'variant': '', 'build': '', 'arch': 'xtensawin', 'port': 'esp32', 'board': 'ESP32_GENERIC_S3', 'board_id': 'ESP32_GENERIC_S3', 'mpy': 'v6.3', 'ver': '1.27.0', 'family': 'micropython', 'cpu': 'ESP32S3', 'version': '1.27.0'}
# Stubber: v1.26.4
from __future__ import annotations
from _typeshed import Incomplete

def delete(*args, **kwargs) -> Incomplete:
    ...

def head(*args, **kwargs) -> Incomplete:
    ...

def patch(*args, **kwargs) -> Incomplete:
    ...

def post(*args, **kwargs) -> Incomplete:
    ...

def request(*args, **kwargs) -> Incomplete:
    ...

def put(*args, **kwargs) -> Incomplete:
    ...

def get(*args, **kwargs) -> Incomplete:
    ...


class Response():
    def json(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    content: Incomplete ## <class 'property'> = <property>
    text: Incomplete ## <class 'property'> = <property>
    def __init__(self, *argv, **kwargs) -> None:
        ...

