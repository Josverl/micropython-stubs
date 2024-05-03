"""
Module: 'aioble.l2cap' on micropython-v1.21.0-rp2-RPI_PICO_W
"""

# MCU: {'build': '', 'ver': 'v1.21.0', 'version': '1.21.0', 'port': 'rp2', 'board': 'RPI_PICO_W', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.13.8
from typing import Any
from _typeshed import Incomplete


def register_irq_handler(*args, **kwargs) -> Incomplete: ...


def log_error(*args, **kwargs) -> Incomplete: ...


def const(*args, **kwargs) -> Incomplete: ...


class L2CAPChannel:
    def available(self, *args, **kwargs) -> Incomplete: ...

    disconnected: Incomplete  ## <class 'generator'> = <generator>
    recvinto: Incomplete  ## <class 'generator'> = <generator>
    send: Incomplete  ## <class 'generator'> = <generator>
    flush: Incomplete  ## <class 'generator'> = <generator>
    disconnect: Incomplete  ## <class 'generator'> = <generator>

    def __init__(self, *argv, **kwargs) -> None: ...


class L2CAPConnectionError(Exception): ...
