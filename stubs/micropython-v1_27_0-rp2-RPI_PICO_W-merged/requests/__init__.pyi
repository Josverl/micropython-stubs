"""
Module: 'requests.__init__' on micropython-v1.27.0-rp2-RPI_PICO_W
"""
# MCU: {'mpy': 'v6.3', 'build': '', 'ver': '1.27.0', 'arch': 'armv6m', 'version': '1.27.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'family': 'micropython', 'board_id': 'RPI_PICO_W', 'variant': '', 'cpu': 'RP2040'}
# Stubber: v1.26.5
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

