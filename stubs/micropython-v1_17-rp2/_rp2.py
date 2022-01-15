"""
Module: '_rp2' on micropython-v1.17-rp2
"""
# MCU: {'family': 'micropython', 'sysname': 'rp2', 'version': '1.17.0', 'build': '', 'mpy': 5637, 'port': 'rp2', 'platform': 'rp2', 'name': 'micropython', 'arch': 'armv7m', 'machine': 'Raspberry Pi Pico with RP2040', 'nodename': 'rp2', 'ver': 'v1.17', 'release': '1.17.0'}
# Stubber: 1.5.2
from typing import Any


class Flash:
    """"""

    def ioctl(self, *args) -> Any:
        ...

    def readblocks(self, *args) -> Any:
        ...

    def writeblocks(self, *args) -> Any:
        ...


class PIO:
    """"""

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

    def add_program(self, *args) -> Any:
        ...

    def irq(self, *args) -> Any:
        ...

    def remove_program(self, *args) -> Any:
        ...

    def state_machine(self, *args) -> Any:
        ...


class StateMachine:
    """"""

    def exec(self, *args) -> Any:
        ...

    def get(self, *args) -> Any:
        ...

    def active(self, *args) -> Any:
        ...

    def init(self, *args) -> Any:
        ...

    def irq(self, *args) -> Any:
        ...

    def put(self, *args) -> Any:
        ...

    def restart(self, *args) -> Any:
        ...

    def rx_fifo(self, *args) -> Any:
        ...

    def tx_fifo(self, *args) -> Any:
        ...
