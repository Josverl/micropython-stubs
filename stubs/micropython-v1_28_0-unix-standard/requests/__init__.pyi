"""
Module: 'requests.__init__' on micropython-v1.28.0-unix-standard
"""
# MCU: {'family': 'micropython', 'version': '1.28.0', 'build': '', 'ver': '1.28.0', 'port': 'unix', 'board': 'standard', 'board_id': 'standard', 'variant': '', 'cpu': 'linux [GCC 12.5.0] version', 'mpy': 'v6.3', 'arch': 'x64'}
# Stubber: v1.28.3
from __future__ import annotations
from typing import Any, Final, Generator, AsyncGenerator
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

