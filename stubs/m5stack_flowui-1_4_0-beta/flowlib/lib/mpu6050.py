"""
Module: 'flowlib.lib.mpu6050' on M5 FlowUI v1.4.0-beta
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-284-g5d8e1c867 on 2019-08-30', machine='ESP32 module with ESP32')
# Stubber: 1.3.1
ACCEL_FS_SEL_16G = 24
ACCEL_FS_SEL_2G = 0
ACCEL_FS_SEL_4G = 8
ACCEL_FS_SEL_8G = 16
GYRO_FS_SEL_1000DPS = 16
GYRO_FS_SEL_2000DPS = 24
GYRO_FS_SEL_250DPS = 0
GYRO_FS_SEL_500DPS = 8

class I2C:
    ''
    CBTYPE_ADDR = 1
    CBTYPE_NONE = 0
    CBTYPE_RXDATA = 2
    CBTYPE_TXDATA = 4
    MASTER = 1
    READ = 1
    SLAVE = 0
    WRITE = 0
    def address():
        pass

    def begin():
        pass

    def callback():
        pass

    def clock_timing():
        pass

    def data_timing():
        pass

    def deinit():
        pass

    def end():
        pass

    def getdata():
        pass

    def init():
        pass

    def is_ready():
        pass

    def read_byte():
        pass

    def read_bytes():
        pass

    def readfrom():
        pass

    def readfrom_into():
        pass

    def readfrom_mem():
        pass

    def readfrom_mem_into():
        pass

    def resetbusy():
        pass

    def scan():
        pass

    def setdata():
        pass

    def start():
        pass

    def start_timing():
        pass

    def stop():
        pass

    def stop_timing():
        pass

    def timeout():
        pass

    def write_byte():
        pass

    def write_bytes():
        pass

    def writeto():
        pass

    def writeto_mem():
        pass


class MPU6050:
    ''
    def _accel_fs():
        pass

    def _gyro_fs():
        pass

    def _register_char():
        pass

    def _register_short():
        pass

    def _register_three_shorts():
        pass

    acceleration = None
    gyro = None
    def setGyroOffsets():
        pass

    whoami = None
    ypr = None

class Pin:
    ''
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
    def deinit():
        pass

    def init():
        pass

    def irq():
        pass

    def off():
        pass

    def on():
        pass

    def value():
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
