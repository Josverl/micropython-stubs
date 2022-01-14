"""
Module: 'mpu6500' on esp32_LoBo 3.2.9
"""
# MCU: (sysname='esp32_LoBo', nodename='esp32_LoBo', release='3.2.9', version='ESP32_LoBo_v3.2.9 on 2018-04-12', machine='ESP32 board with ESP32')
# Stubber: 1.1.2 - updated
from typing import Any

ACCEL_FS_SEL_16G = 24
ACCEL_FS_SEL_2G = 0
ACCEL_FS_SEL_4G = 8
ACCEL_FS_SEL_8G = 16
GYRO_FS_SEL_1000DPS = 16
GYRO_FS_SEL_2000DPS = 24
GYRO_FS_SEL_250DPS = 0
GYRO_FS_SEL_500DPS = 8


class I2C:
    """"""

    CB_DATA = 3
    CB_READ = 1
    CB_WRITE = 2
    MASTER = 1
    READ = 1
    SLAVE = 0
    WRITE = 0

    def address(self, *args) -> Any:
        pass

    def begin(self, *args) -> Any:
        pass

    def callback(self, *args) -> Any:
        pass

    def deinit(self, *args) -> Any:
        pass

    def end(self, *args) -> Any:
        pass

    def getdata(self, *args) -> Any:
        pass

    def init(self, *args) -> Any:
        pass

    def read_byte(self, *args) -> Any:
        pass

    def read_bytes(self, *args) -> Any:
        pass

    def readfrom(self, *args) -> Any:
        pass

    def readfrom_into(self, *args) -> Any:
        pass

    def readfrom_mem(self, *args) -> Any:
        pass

    def readfrom_mem_into(self, *args) -> Any:
        pass

    def scan(self, *args) -> Any:
        pass

    def setdata(self, *args) -> Any:
        pass

    def slavewrite(self, *args) -> Any:
        pass

    def start(self, *args) -> Any:
        pass

    def stop(self, *args) -> Any:
        pass

    def write_byte(self, *args) -> Any:
        pass

    def write_bytes(self, *args) -> Any:
        pass

    def writeto(self, *args) -> Any:
        pass

    def writeto_mem(self, *args) -> Any:
        pass


class MPU6500:
    """"""

    def _accel_fs(self, *args) -> Any:
        pass

    def _gyro_fs(self, *args) -> Any:
        pass

    def _register_char(self, *args) -> Any:
        pass

    def _register_short(self, *args) -> Any:
        pass

    def _register_three_shorts(self, *args) -> Any:
        pass

    acceleration = None
    gyro = None
    whoami = None


class Pin:
    """"""

    IN = 1
    INOUT = 3
    INOUT_OD = 7
    IRQ_ANYEDGE = 3
    IRQ_FALLING = 2
    IRQ_HILEVEL = 5
    IRQ_LOLEVEL = 4
    IRQ_RISING = 1
    OUT = 2
    OUT_OD = 6
    PULL_DOWN = 1
    PULL_FLOAT = 3
    PULL_UP = 0
    PULL_UPDOWN = 2

    def init(self, *args) -> Any:
        pass

    def irq(self, *args) -> Any:
        pass

    def value(self, *args) -> Any:
        pass


SF_DEG_S = 1
SF_G = 1
SF_M_S2 = 9.806650000000001
SF_RAD_S = 57.29577957855201
_ACCEL_SO_16G = 2048
_ACCEL_SO_2G = 16384
_ACCEL_SO_4G = 8192
_ACCEL_SO_8G = 4096
_GYRO_SO_1000DPS = 32.8
_GYRO_SO_2000DPS = 16.4
_GYRO_SO_250DPS = 131
_GYRO_SO_500DPS = 62.5


def const(*args) -> Any:
    pass


ustruct = None
