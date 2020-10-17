# make_stub_files: Tue 23 Apr 2019 at 22:52:00

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class AK8963:
    def __init__(self, i2c: Any, address: Any=12, mode: Any=MODE_CONTINOUS_MEASURE_1, output: Any=OUTPUT_16_BIT, offset: Any=(0, 0, 0), scale: Any=(1, 1, 1)) -> None: ...
    def magnetic(self) -> Tuple[Any]: ...
    def adjustement(self) -> Any: ...
        #   0: return self._adjustement
        # ? 0: return self._adjustement
    def whoami(self) -> Any: ...
        #   0: return self._register_char(_WIA)
        # ? 0: return self._register_char(_WIA)
    def _register_short(self, register: Any, value: Any=None, buf: Any=bytearray(2)) -> Any: ...
        #   0: return ustruct.unpack('<h',buf)[0]
        # ? 0: return ustruct.unpack(str, buf)[number]
        #   1: return self.i2c.writeto_mem(self.address,register,buf)
        # ? 1: return self.i2c.writeto_mem(self.address, register, buf)
    def _register_three_shorts(self, register: Any, buf: Any=bytearray(6)) -> Any: ...
        #   0: return ustruct.unpack('<hhh',buf)
        # ? 0: return ustruct.unpack(str, buf)
    def _register_char(self, register: Any, value: Any=None, buf: Any=bytearray(1)) -> Any: ...
        #   0: return buf[0]
        # ? 0: return buf[number]
        #   1: return self.i2c.writeto_mem(self.address,register,buf)
        # ? 1: return self.i2c.writeto_mem(self.address, register, buf)
    def __enter__(self) -> Any: ...
        #   0: return self
        # ? 0: return self
    def __exit__(self, exception_type: Any, exception_value: Any, traceback: Any) -> None: ...
