"""
Module: 'lsm6dsox' on micropython-v1.24.1-rp2-ARDUINO_NANO_RP2040_CONNECT
"""

# MCU: {'family': 'micropython', 'version': '1.24.1', 'build': '', 'ver': '1.24.1', 'port': 'rp2', 'board': 'ARDUINO_NANO_RP2040_CONNECT', 'cpu': 'RP2040', 'mpy': 'v6.3', 'arch': 'armv6m'}
# Stubber: v1.24.0
from __future__ import annotations
from _typeshed import Incomplete

def const(*args, **kwargs) -> Incomplete: ...

class LSM6DSOX:
    def load_mlc(self, *args, **kwargs) -> Incomplete: ...
    def gyro(self, *args, **kwargs) -> Incomplete: ...
    def set_mem_bank(self, *args, **kwargs) -> Incomplete: ...
    def mlc_output(self, *args, **kwargs) -> Incomplete: ...
    def set_embedded_functions(self, *args, **kwargs) -> Incomplete: ...
    def _read_reg(self, *args, **kwargs) -> Incomplete: ...
    def reset(self, *args, **kwargs) -> Incomplete: ...
    def accel(self, *args, **kwargs) -> Incomplete: ...
    def _read_reg_into(self, *args, **kwargs) -> Incomplete: ...
    def _write_reg(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
