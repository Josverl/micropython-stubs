
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class DHTBase:
    def __init__(self, pin: machine.Pin) -> None: ...
    def measure(self) -> None: ...
class DHT11(DHTBase):
    def humidity(self) -> Any: ...
        #   0: return self.buf[]
        # ? 0: return self.buf[]
    def temperature(self) -> Any: ...
        #   0: return self.buf[]
        # ? 0: return self.buf[]
class DHT22(DHTBase):
    def humidity(self) -> Any: ...
        #   0: return self.buf[]<<|self.buf[]*
        # ? 0: return self.buf[]<<|self.buf[]*
    def temperature(self) -> Any: ...
        #   0: return t
        # ? 0: return t
