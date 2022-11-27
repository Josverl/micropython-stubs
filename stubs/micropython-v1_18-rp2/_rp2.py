"""
Module: '_rp2' on micropython-v1.18-rp2
"""
# MCU: {'family': 'micropython', 'sysname': 'rp2', 'version': '1.18.0', 'build': '', 'mpy': 5637, 'port': 'rp2', 'platform': 'rp2', 'name': 'micropython', 'arch': 'armv7m', 'machine': 'Arduino Nano RP2040 Connect with RP2040', 'nodename': 'rp2', 'ver': 'v1.18', 'release': '1.18.0'}
# Stubber: 1.5.3
from typing import Any


class Flash:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def ioctl(self, *args, **kwargs) -> Any:
        ...

    def readblocks(self, *args, **kwargs) -> Any:
        ...

    def writeblocks(self, *args, **kwargs) -> Any:
        ...


class PIO:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    IN_HIGH = 1  # type: int
    IN_LOW = 0  # type: int
    IRQ_SM0 = 256  # type: int
    IRQ_SM1 = 512  # type: int
    IRQ_SM2 = 1024  # type: int
    IRQ_SM3 = 2048  # type: int
    JOIN_NONE = 0  # type: int
    JOIN_RX = 2  # type: int
    JOIN_TX = 1  # type: int
    OUT_HIGH = 3  # type: int
    OUT_LOW = 2  # type: int
    SHIFT_LEFT = 0  # type: int
    SHIFT_RIGHT = 1  # type: int

    def add_program(self, *args, **kwargs) -> Any:
        ...

    def irq(self, *args, **kwargs) -> Any:
        ...

    def remove_program(self, *args, **kwargs) -> Any:
        ...

    def state_machine(self, *args, **kwargs) -> Any:
        ...


class StateMachine:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def exec(self, *args, **kwargs) -> Any:
        ...

    def get(self, *args, **kwargs) -> Any:
        ...

    def active(self, *args, **kwargs) -> Any:
        ...

    def init(self, *args, **kwargs) -> Any:
        ...

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


def dht_readinto(*args, **kwargs) -> Any:
    ...
