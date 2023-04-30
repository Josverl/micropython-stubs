"""
Module: 'rp2' on micropython-v1.20-rp2-PICO_W
"""
# MCU: OrderedDict({'family': 'micropython', 'version': '1.20', 'build': '', 'ver': 'v1.20', 'port': 'rp2', 'board': 'PICO_W', 'cpu': 'RP2040', 'mpy': 'v6.1', 'arch': 'armv6m'})
# Stubber: v1.12.2
from typing import Any


def asm_pio(*args, **kwargs) -> Any:
    ...


def asm_pio_encode(*args, **kwargs) -> Any:
    ...


def bootsel_button(*args, **kwargs) -> Any:
    ...


def country(*args, **kwargs) -> Any:
    ...


def const(*args, **kwargs) -> Any:
    ...


class PIOASMEmit:
    def wrap(self, *args, **kwargs) -> Any:
        ...

    def wait(self, *args, **kwargs) -> Any:
        ...

    def jmp(self, *args, **kwargs) -> Any:
        ...

    def word(self, *args, **kwargs) -> Any:
        ...

    def in_(self, *args, **kwargs) -> Any:
        ...

    def delay(self, *args, **kwargs) -> Any:
        ...

    def start_pass(self, *args, **kwargs) -> Any:
        ...

    def out(self, *args, **kwargs) -> Any:
        ...

    def side(self, *args, **kwargs) -> Any:
        ...

    def wrap_target(self, *args, **kwargs) -> Any:
        ...

    def label(self, *args, **kwargs) -> Any:
        ...

    def irq(self, *args, **kwargs) -> Any:
        ...

    def set(self, *args, **kwargs) -> Any:
        ...

    def mov(self, *args, **kwargs) -> Any:
        ...

    def push(self, *args, **kwargs) -> Any:
        ...

    def pull(self, *args, **kwargs) -> Any:
        ...

    def nop(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class PIOASMError(Exception):
    ...
