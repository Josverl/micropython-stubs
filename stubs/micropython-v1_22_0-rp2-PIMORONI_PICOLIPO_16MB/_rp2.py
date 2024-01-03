"""
Module: '_rp2' on micropython-v1.22.0-rp2-PIMORONI_PICOLIPO_16MB
"""
# MCU: {'family': 'micropython', 'version': '1.22.0', 'build': '', 'ver': 'v1.22.0', 'port': 'rp2', 'board': 'PIMORONI_PICOLIPO_16MB', 'cpu': 'RP2040', 'mpy': 'v6.2', 'arch': 'armv6m'}
# Stubber: v1.16.2
from _typeshed import Incomplete


def bootsel_button(*args, **kwargs) -> Incomplete:
    ...


class DMA:
    def irq(self, *args, **kwargs) -> Incomplete:
        ...

    def unpack_ctrl(self, *args, **kwargs) -> Incomplete:
        ...

    def pack_ctrl(self, *args, **kwargs) -> Incomplete:
        ...

    def close(self, *args, **kwargs) -> Incomplete:
        ...

    def config(self, *args, **kwargs) -> Incomplete:
        ...

    def active(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class StateMachine:
    def irq(self, *args, **kwargs) -> Incomplete:
        ...

    def put(self, *args, **kwargs) -> Incomplete:
        ...

    def restart(self, *args, **kwargs) -> Incomplete:
        ...

    def rx_fifo(self, *args, **kwargs) -> Incomplete:
        ...

    def tx_fifo(self, *args, **kwargs) -> Incomplete:
        ...

    def init(self, *args, **kwargs) -> Incomplete:
        ...

    def exec(self, *args, **kwargs) -> Incomplete:
        ...

    def get(self, *args, **kwargs) -> Incomplete:
        ...

    def active(self, *args, **kwargs) -> Incomplete:
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

    def state_machine(self, *args, **kwargs) -> Incomplete:
        ...

    def remove_program(self, *args, **kwargs) -> Incomplete:
        ...

    def irq(self, *args, **kwargs) -> Incomplete:
        ...

    def add_program(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class Flash:
    def readblocks(self, *args, **kwargs) -> Incomplete:
        ...

    def writeblocks(self, *args, **kwargs) -> Incomplete:
        ...

    def ioctl(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
