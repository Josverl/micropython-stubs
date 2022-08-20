"""
Module: 'rp2' on micropython-v1.19.1-rp2
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'sysname': 'rp2', 'platform': 'rp2', 'version': '1.19.1', 'release': '1.19.1', 'port': 'rp2', 'family': 'micropython', 'name': 'micropython', 'machine': 'Raspberry Pi Pico W with RP2040', 'nodename': 'rp2'}
# Stubber: 1.7.2
from typing import Any

def const(*args, **kwargs) -> Any:
    ...


class Flash():
    def __init__(self, *argv, **kwargs) -> None:
        ...

    def ioctl(self, *args, **kwargs) -> Any:
        ...

    def readblocks(self, *args, **kwargs) -> Any:
        ...

    def writeblocks(self, *args, **kwargs) -> Any:
        ...


class PIO():
    def __init__(self, *argv, **kwargs) -> None:
        ...

    IN_HIGH = 1 # type: int
    IN_LOW = 0 # type: int
    IRQ_SM0 = 256 # type: int
    IRQ_SM1 = 512 # type: int
    IRQ_SM2 = 1024 # type: int
    IRQ_SM3 = 2048 # type: int
    JOIN_NONE = 0 # type: int
    JOIN_RX = 2 # type: int
    JOIN_TX = 1 # type: int
    OUT_HIGH = 3 # type: int
    OUT_LOW = 2 # type: int
    SHIFT_LEFT = 0 # type: int
    SHIFT_RIGHT = 1 # type: int
    def add_program(self, *args, **kwargs) -> Any:
        ...

    def irq(self, *args, **kwargs) -> Any:
        ...

    def remove_program(self, *args, **kwargs) -> Any:
        ...

    def state_machine(self, *args, **kwargs) -> Any:
        ...


class StateMachine():
    def __init__(self, *argv, **kwargs) -> None:
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

def asm_pio_encode(*args, **kwargs) -> Any:
    ...

def country(*args, **kwargs) -> Any:
    ...

def dht_readinto(*args, **kwargs) -> Any:
    ...


class PIOASMError(Exception):
    ...

class PIOASMEmit():
    def __init__(self, *argv, **kwargs) -> None:
        ...

    def set(self, *args, **kwargs) -> Any:
        ...

    def irq(self, *args, **kwargs) -> Any:
        ...

    def label(self, *args, **kwargs) -> Any:
        ...

    def mov(self, *args, **kwargs) -> Any:
        ...

    def nop(self, *args, **kwargs) -> Any:
        ...

    def pull(self, *args, **kwargs) -> Any:
        ...

    def push(self, *args, **kwargs) -> Any:
        ...

    def wrap_target(self, *args, **kwargs) -> Any:
        ...

    def wrap(self, *args, **kwargs) -> Any:
        ...

    def word(self, *args, **kwargs) -> Any:
        ...

    def jmp(self, *args, **kwargs) -> Any:
        ...

    def wait(self, *args, **kwargs) -> Any:
        ...

    def in_(self, *args, **kwargs) -> Any:
        ...

    def out(self, *args, **kwargs) -> Any:
        ...

    def start_pass(self, *args, **kwargs) -> Any:
        ...

    def delay(self, *args, **kwargs) -> Any:
        ...

    def side(self, *args, **kwargs) -> Any:
        ...

def asm_pio(*args, **kwargs) -> Any:
    ...

