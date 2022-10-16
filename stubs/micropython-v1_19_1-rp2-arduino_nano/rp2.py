"""
Module: 'rp2' on micropython-v1.19.1-rp2
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'sysname': 'rp2', 'platform': 'rp2', 'version': '1.19.1', 'release': '1.19.1', 'port': 'rp2', 'family': 'micropython', 'name': 'micropython', 'machine': 'Arduino Nano RP2040 Connect with RP2040', 'nodename': 'rp2'}
# Stubber: 1.9.11
from typing import Any


def asm_pio_encode(*args, **kwargs) -> Any:
    ...


def asm_pio(*args, **kwargs) -> Any:
    ...


def dht_readinto(*args, **kwargs) -> Any:
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
