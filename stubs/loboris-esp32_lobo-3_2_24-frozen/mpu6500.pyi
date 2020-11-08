# make_stub_files: Tue 23 Apr 2019 at 22:52:01

from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class MPU6500:
    def __init__(self, i2c: Any, address: Any=104, accel_fs: Any=ACCEL_FS_SEL_2G, gyro_fs: Any=GYRO_FS_SEL_250DPS, accel_sf: Any=SF_M_S2, gyro_sf: Any=SF_RAD_S) -> None: ...
    def acceleration(self) -> Tuple[Any]: ...
    def gyro(self) -> Tuple[Any]: ...
    def whoami(self) -> Any: ...
        #   0: return self._register_char(_WHO_AM_I)
        # ? 0: return self._register_char(_WHO_AM_I)
    def _register_short(self, register: Any, value: Any=None, buf: Any=bytearray(2)) -> Any: ...
        #   0: return ustruct.unpack('>h',buf)[0]
        # ? 0: return ustruct.unpack(str, buf)[number]
        #   1: return self.i2c.writeto_mem(self.address,register,buf)
        # ? 1: return self.i2c.writeto_mem(self.address, register, buf)
    def _register_three_shorts(self, register: Any, buf: Any=bytearray(6)) -> Any: ...
        #   0: return ustruct.unpack('>hhh',buf)
        # ? 0: return ustruct.unpack(str, buf)
    def _register_char(self, register: Any, value: Any=None, buf: Any=bytearray(1)) -> Any: ...
        #   0: return buf[0]
        # ? 0: return buf[number]
        #   1: return self.i2c.writeto_mem(self.address,register,buf)
        # ? 1: return self.i2c.writeto_mem(self.address, register, buf)
    def _accel_fs(self, value: Any) -> Any: ...
        #   0: return _ACCEL_SO_2G
        # ? 0: return _ACCEL_SO_2G
        #   1: return _ACCEL_SO_4G
        # ? 1: return _ACCEL_SO_4G
        #   2: return _ACCEL_SO_8G
        # ? 2: return _ACCEL_SO_8G
        #   3: return _ACCEL_SO_16G
        # ? 3: return _ACCEL_SO_16G
    def _gyro_fs(self, value: Any) -> Any: ...
        #   0: return _GYRO_SO_250DPS
        # ? 0: return _GYRO_SO_250DPS
        #   1: return _GYRO_SO_500DPS
        # ? 1: return _GYRO_SO_500DPS
        #   2: return _GYRO_SO_1000DPS
        # ? 2: return _GYRO_SO_1000DPS
        #   3: return _GYRO_SO_2000DPS
        # ? 3: return _GYRO_SO_2000DPS
    def __enter__(self) -> Any: ...
        #   0: return self
        # ? 0: return self
    def __exit__(self, exception_type: Any, exception_value: Any, traceback: Any) -> None: ...
