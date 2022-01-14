"""
Module: 'flowlib.lib.mpu6050' on M5 FlowUI v1.4.0-beta
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-284-g5d8e1c867 on 2019-08-30', machine='ESP32 module with ESP32')
# Stubber: 1.3.1 - updated
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

    CBTYPE_ADDR = 1
    CBTYPE_NONE = 0
    CBTYPE_RXDATA = 2
    CBTYPE_TXDATA = 4
    MASTER = 1
    READ = 1
    SLAVE = 0
    WRITE = 0

    def address(self, *argv) -> Any:
        pass

    def begin(self, *argv) -> Any:
        pass

    def callback(self, *argv) -> Any:
        pass

    def clock_timing(self, *argv) -> Any:
        pass

    def data_timing(self, *argv) -> Any:
        pass

    def deinit(self, *argv) -> Any:
        pass

    def end(self, *argv) -> Any:
        pass

    def getdata(self, *argv) -> Any:
        pass

    def init(self, *argv) -> Any:
        pass

    def is_ready(self, *argv) -> Any:
        pass

    def read_byte(self, *argv) -> Any:
        pass

    def read_bytes(self, *argv) -> Any:
        pass

    def readfrom(self, *argv) -> Any:
        pass

    def readfrom_into(self, *argv) -> Any:
        pass

    def readfrom_mem(self, *argv) -> Any:
        pass

    def readfrom_mem_into(self, *argv) -> Any:
        pass

    def resetbusy(self, *argv) -> Any:
        pass

    def scan(self, *argv) -> Any:
        pass

    def setdata(self, *argv) -> Any:
        pass

    def start(self, *argv) -> Any:
        pass

    def start_timing(self, *argv) -> Any:
        pass

    def stop(self, *argv) -> Any:
        pass

    def stop_timing(self, *argv) -> Any:
        pass

    def timeout(self, *argv) -> Any:
        pass

    def write_byte(self, *argv) -> Any:
        pass

    def write_bytes(self, *argv) -> Any:
        pass

    def writeto(self, *argv) -> Any:
        pass

    def writeto_mem(self, *argv) -> Any:
        pass


class MPU6050:
    """"""

    def _accel_fs(self, *argv) -> Any:
        pass

    def _gyro_fs(self, *argv) -> Any:
        pass

    def _register_char(self, *argv) -> Any:
        pass

    def _register_short(self, *argv) -> Any:
        pass

    def _register_three_shorts(self, *argv) -> Any:
        pass

    acceleration = None
    gyro = None

    def setGyroOffsets(self, *argv) -> Any:
        pass

    whoami = None
    ypr = None


class Pin:
    """"""

    IN = 1
    INOUT = 3
    IRQ_FALLING = 2
    IRQ_RISING = 1
    OPEN_DRAIN = 7
    OUT = 3
    OUT_OD = 6
    PULL_DOWN = 1
    PULL_FLOAT = 3
    PULL_HOLD = 4
    PULL_UP = 2
    WAKE_HIGH = 5
    WAKE_LOW = 4

    def deinit(self, *argv) -> Any:
        pass

    def init(self, *argv) -> Any:
        pass

    def irq(self, *argv) -> Any:
        pass

    def off(self, *argv) -> Any:
        pass

    def on(self, *argv) -> Any:
        pass

    def value(self, *argv) -> Any:
        pass


SF_DEG_S = 1
SF_G = 1
SF_M_S2 = 9.80665
SF_RAD_S = 57.29578
_ACCEL_SO_16G = 2048
_ACCEL_SO_2G = 16384
_ACCEL_SO_4G = 8192
_ACCEL_SO_8G = 4096
_GYRO_SO_1000DPS = 32.8
_GYRO_SO_2000DPS = 16.4
_GYRO_SO_250DPS = 131
_GYRO_SO_500DPS = 65.5


def const():
    pass


math = None
time = None
ustruct = None
