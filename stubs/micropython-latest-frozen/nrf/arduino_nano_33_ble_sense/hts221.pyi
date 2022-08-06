from typing import Any

class HTS221:
    bus: Any
    odr: Any
    slv_addr: Any
    H0: Any
    H1: Any
    H2: Any
    H3: Any
    T0: Any
    T1: Any
    T2: Any
    T3: Any
    def __init__(self, i2c, data_rate: int = ..., address: int = ...) -> None: ...
    def _read_reg(self, reg_addr, size): ...
    def humidity(self): ...
    def temperature(self): ...
