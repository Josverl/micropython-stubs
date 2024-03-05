from _typeshed import Incomplete

class HTS221:
    bus: Incomplete
    odr: Incomplete
    slv_addr: Incomplete
    H0: Incomplete
    H1: Incomplete
    H2: Incomplete
    H3: Incomplete
    T0: Incomplete
    T1: Incomplete
    T2: Incomplete
    T3: Incomplete
    def __init__(self, i2c, data_rate: int = ..., address: int = ...) -> None: ...
    def _read_reg(self, reg_addr, size): ...
    def humidity(self): ...
    def temperature(self): ...
