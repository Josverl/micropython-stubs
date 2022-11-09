"""
Module: 'lsm6dsox' on micropython-v1.19.1-rp2
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'sysname': 'rp2', 'platform': 'rp2', 'version': '1.19.1', 'release': '1.19.1', 'port': 'rp2', 'family': 'micropython', 'name': 'micropython', 'machine': 'Arduino Nano RP2040 Connect with RP2040', 'nodename': 'rp2'}
# Stubber: 1.9.11
from typing import Any


def const(*args, **kwargs) -> Any:
    ...


class LSM6DSOX:
    def read_mlc_output(self, *args, **kwargs) -> Any:
        ...

    def set_embedded_functions(self, *args, **kwargs) -> Any:
        ...

    def read_gyro(self, *args, **kwargs) -> Any:
        ...

    def read_accel(self, *args, **kwargs) -> Any:
        ...

    def reset(self, *args, **kwargs) -> Any:
        ...

    def set_mem_bank(self, *args, **kwargs) -> Any:
        ...

    def load_mlc(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
