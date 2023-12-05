"""
Module: 'requests' on micropython-v1.22.0.preview-unix-linux_[GCC_9.4.0]_version
"""
# MCU: {'family': 'micropython', 'version': '1.22.0.preview', 'build': '', 'ver': 'v1.22.0.preview', 'port': 'unix', 'board': 'linux_[GCC_9.4.0]_version', 'cpu': '', 'mpy': '', 'arch': ''}
# Stubber: v1.15.1
from typing import Any
from _typeshed import Incomplete


def head(*args, **kwargs) -> Incomplete:
    ...


def delete(*args, **kwargs) -> Incomplete:
    ...


def patch(*args, **kwargs) -> Incomplete:
    ...


def post(*args, **kwargs) -> Incomplete:
    ...


def get(*args, **kwargs) -> Incomplete:
    ...


def request(*args, **kwargs) -> Incomplete:
    ...


def put(*args, **kwargs) -> Incomplete:
    ...


class Response:
    def json(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    content: Incomplete  ## <class 'property'> = <property>
    text: Incomplete  ## <class 'property'> = <property>

    def __init__(self, *argv, **kwargs) -> None:
        ...
