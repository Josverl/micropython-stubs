"""
Module: 'aioble.l2cap' on micropython-v1.19.1-rp2
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'sysname': 'rp2', 'platform': 'rp2', 'version': '1.19.1', 'release': '1.19.1', 'port': 'rp2', 'family': 'micropython', 'name': 'micropython', 'machine': 'Arduino Nano RP2040 Connect with RP2040', 'nodename': 'rp2'}
# Stubber: 1.9.11
from typing import Any


def log_error(*args, **kwargs) -> Any:
    ...


def register_irq_handler(*args, **kwargs) -> Any:
    ...


def const(*args, **kwargs) -> Any:
    ...


class L2CAPChannel:
    def available(self, *args, **kwargs) -> Any:
        ...

    send: Any  ## <class 'generator'> = <generator>
    recvinto: Any  ## <class 'generator'> = <generator>
    flush: Any  ## <class 'generator'> = <generator>
    disconnect: Any  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None:
        ...


class L2CAPDisconnectedError(Exception):
    ...
