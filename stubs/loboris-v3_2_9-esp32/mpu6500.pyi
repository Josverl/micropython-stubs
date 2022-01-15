from typing import Any

ACCEL_FS_SEL_16G: int
ACCEL_FS_SEL_2G: int
ACCEL_FS_SEL_4G: int
ACCEL_FS_SEL_8G: int
GYRO_FS_SEL_1000DPS: int
GYRO_FS_SEL_2000DPS: int
GYRO_FS_SEL_250DPS: int
GYRO_FS_SEL_500DPS: int

class I2C:
    CB_DATA: int
    CB_READ: int
    CB_WRITE: int
    MASTER: int
    READ: int
    SLAVE: int
    WRITE: int
    def address(self, *args) -> Any: ...
    def begin(self, *args) -> Any: ...
    def callback(self, *args) -> Any: ...
    def deinit(self, *args) -> Any: ...
    def end(self, *args) -> Any: ...
    def getdata(self, *args) -> Any: ...
    def init(self, *args) -> Any: ...
    def read_byte(self, *args) -> Any: ...
    def read_bytes(self, *args) -> Any: ...
    def readfrom(self, *args) -> Any: ...
    def readfrom_into(self, *args) -> Any: ...
    def readfrom_mem(self, *args) -> Any: ...
    def readfrom_mem_into(self, *args) -> Any: ...
    def scan(self, *args) -> Any: ...
    def setdata(self, *args) -> Any: ...
    def slavewrite(self, *args) -> Any: ...
    def start(self, *args) -> Any: ...
    def stop(self, *args) -> Any: ...
    def write_byte(self, *args) -> Any: ...
    def write_bytes(self, *args) -> Any: ...
    def writeto(self, *args) -> Any: ...
    def writeto_mem(self, *args) -> Any: ...

class MPU6500:
    def _accel_fs(self, *args) -> Any: ...
    def _gyro_fs(self, *args) -> Any: ...
    def _register_char(self, *args) -> Any: ...
    def _register_short(self, *args) -> Any: ...
    def _register_three_shorts(self, *args) -> Any: ...
    acceleration: Any
    gyro: Any
    whoami: Any

class Pin:
    IN: int
    INOUT: int
    INOUT_OD: int
    IRQ_ANYEDGE: int
    IRQ_FALLING: int
    IRQ_HILEVEL: int
    IRQ_LOLEVEL: int
    IRQ_RISING: int
    OUT: int
    OUT_OD: int
    PULL_DOWN: int
    PULL_FLOAT: int
    PULL_UP: int
    PULL_UPDOWN: int
    def init(self, *args) -> Any: ...
    def irq(self, *args) -> Any: ...
    def value(self, *args) -> Any: ...

SF_DEG_S: int
SF_G: int
SF_M_S2: float
SF_RAD_S: float
_ACCEL_SO_16G: int
_ACCEL_SO_2G: int
_ACCEL_SO_4G: int
_ACCEL_SO_8G: int
_GYRO_SO_1000DPS: float
_GYRO_SO_2000DPS: float
_GYRO_SO_250DPS: int
_GYRO_SO_500DPS: float

def const(*args) -> Any: ...

ustruct: Any