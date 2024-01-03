"""
Module: '_thread' on micropython-v1.22.0-esp32-ESP32_GENERIC_S3
"""
# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'esp32', 'board': 'ESP32_GENERIC_S3', 'cpu': 'ESP32S3', 'mpy': 'v6.2', 'arch': 'xtensawin'}
# Stubber: v1.16.2
from _typeshed import Incomplete


def get_ident(*args, **kwargs) -> Incomplete:
    ...


def start_new_thread(*args, **kwargs) -> Incomplete:
    ...


def stack_size(*args, **kwargs) -> Incomplete:
    ...


def exit(*args, **kwargs) -> Incomplete:
    ...


def allocate_lock(*args, **kwargs) -> Incomplete:
    ...


class LockType:
    def locked(self, *args, **kwargs) -> Incomplete:
        ...

    def release(self, *args, **kwargs) -> Incomplete:
        ...

    def acquire(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
