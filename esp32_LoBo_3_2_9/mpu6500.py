"""
Module: 'mpu6500' on esp32_LoBo 3.2.9
"""
# MCU: (sysname='esp32_LoBo', nodename='esp32_LoBo', release='3.2.9', version='ESP32_LoBo_v3.2.9 on 2018-04-12', machine='ESP32 board with ESP32')
# Stubber: 1.1.2
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
    CB_DATA = 3
    CB_READ = 1
    CB_WRITE = 2
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

    def deinit():
        pass

    def end():
        pass

    def getdata():
        pass

    def init():
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

    def scan():
        pass

    def setdata():
        pass

    def slavewrite():
        pass

    def start():
        pass

    def stop():
        pass

    def write_byte():
        pass

    def write_bytes():
        pass

    def writeto():
        pass

    def writeto_mem():
        pass


class MPU6500:
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
    whoami = None

class Pin:
    ''
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
    def init():
        pass

    def irq():
        pass

    def value():
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
def const():
    pass

ustruct = None
