"""
Module: '_rp2' on micropython-v1.20-rp2-PICO_W
"""
# MCU: OrderedDict({'family': 'micropython', 'version': '1.20', 'build': '', 'ver': 'v1.20', 'port': 'rp2', 'board': 'PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.1', 'arch': 'armv6m'})
# Stubber: v1.12.2
from typing import Any


def country(*args, **kwargs) -> Any:
    ...


def bootsel_button(*args, **kwargs) -> Any:
    ...


class Flash:
    def readblocks(self, *args, **kwargs) -> Any:
        ...

    def writeblocks(self, *args, **kwargs) -> Any:
        ...

    def ioctl(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class PIO:
    JOIN_TX = 1  # type: int
    JOIN_NONE = 0  # type: int
    JOIN_RX = 2  # type: int
    SHIFT_LEFT = 0  # type: int
    OUT_HIGH = 3  # type: int
    OUT_LOW = 2  # type: int
    SHIFT_RIGHT = 1  # type: int
    IN_LOW = 0  # type: int
    IRQ_SM3 = 2048  # type: int
    IN_HIGH = 1  # type: int
    IRQ_SM2 = 1024  # type: int
    IRQ_SM0 = 256  # type: int
    IRQ_SM1 = 512  # type: int

    def state_machine(self, *args, **kwargs) -> Any:
        ...

    def remove_program(self, *args, **kwargs) -> Any:
        ...

    def irq(self, *args, **kwargs) -> Any:
        ...

    def add_program(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class StateMachine:
    def irq(self, *args, **kwargs) -> Any:
        ...

    def put(self, *args, **kwargs) -> Any:
        ...

    def restart(self, *args, **kwargs) -> Any:
        ...

    def rx_fifo(self, *args, **kwargs) -> Any:
        ...

    def tx_fifo(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

    def exec(self, *args, **kwargs) -> Any:
        ...

    def get(self, *args, **kwargs) -> Any:
        ...

    def active(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
