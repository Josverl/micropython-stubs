"""
Module: 'rp2' on micropython-v1.21.0-rp2-RPI_PICO
"""
# MCU: {'build': '', 'ver': 'v1.21.0', 'version': '1.21.0', 'port': 'rp2', 'board': 'RPI_PICO', 'mpy': 'v6.1', 'family': 'micropython', 'cpu': 'RP2040', 'arch': 'armv6m'}
# Stubber: v1.13.8
from typing import Any
from _typeshed import Incomplete


def asm_pio_encode(*args, **kwargs) -> Incomplete:
    ...


def asm_pio(*args, **kwargs) -> Incomplete:
    ...


def bootsel_button(*args, **kwargs) -> Incomplete:
    ...


def const(*args, **kwargs) -> Incomplete:
    ...


class PIOASMEmit:
    def wrap(self, *args, **kwargs) -> Incomplete:
        ...

    def wait(self, *args, **kwargs) -> Incomplete:
        ...

    def jmp(self, *args, **kwargs) -> Incomplete:
        ...

    def word(self, *args, **kwargs) -> Incomplete:
        ...

    def in_(self, *args, **kwargs) -> Incomplete:
        ...

    def delay(self, *args, **kwargs) -> Incomplete:
        ...

    def start_pass(self, *args, **kwargs) -> Incomplete:
        ...

    def out(self, *args, **kwargs) -> Incomplete:
        ...

    def side(self, *args, **kwargs) -> Incomplete:
        ...

    def wrap_target(self, *args, **kwargs) -> Incomplete:
        ...

    def label(self, *args, **kwargs) -> Incomplete:
        ...

    def irq(self, *args, **kwargs) -> Incomplete:
        ...

    def set(self, *args, **kwargs) -> Incomplete:
        ...

    def mov(self, *args, **kwargs) -> Incomplete:
        ...

    def push(self, *args, **kwargs) -> Incomplete:
        ...

    def pull(self, *args, **kwargs) -> Incomplete:
        ...

    def nop(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class PIOASMError(Exception):
    ...
