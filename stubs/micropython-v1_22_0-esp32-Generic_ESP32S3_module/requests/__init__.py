"""
Module: 'requests.__init__' on micropython-v1.22.0-esp32-Generic_ESP32S3_module
"""
# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'esp32', 'board': 'Generic_ESP32S3_module', 'cpu': 'ESP32S3', 'mpy': 'v6.2', 'arch': 'xtensawin'}
# Stubber: v1.16.2
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
