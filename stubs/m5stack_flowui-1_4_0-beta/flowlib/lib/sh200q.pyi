from typing import Any

ACCEL_FS_SEL_16G: int
ACCEL_FS_SEL_4G: int
ACCEL_FS_SEL_8G: int
GYRO_FS_SEL_1000DPS: int
GYRO_FS_SEL_250DPS: int
GYRO_FS_SEL_500DPS: int
SF_DEG_S: int
SF_G: int
SF_M_S2: float
SF_RAD_S: float

class Sh200q:
    def _accel_fs() -> None: ...
    def _gyro_fs() -> None: ...
    def _regChar() -> None: ...
    def _regInit() -> None: ...
    def _regThreeShort() -> None: ...
    acceleration: Any
    def adcRest() -> None: ...
    def deinit() -> None: ...
    gyro: Any
    ypr: Any

_ACCEL_SO_16G: int
_ACCEL_SO_4G: int
_ACCEL_SO_8G: int
_GYRO_SO_1000DPS: float
_GYRO_SO_250DPS: int
_GYRO_SO_500DPS: float

def const() -> None: ...

i2c_bus: Any
math: Any
time: Any
ustruct: Any
