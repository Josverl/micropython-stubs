"""
Module: 'flowlib.lib.sh200q' on M5 FlowUI v1.4.0-beta
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-284-g5d8e1c867 on 2019-08-30', machine='ESP32 module with ESP32')
# Stubber: 1.3.1
ACCEL_FS_SEL_16G = 2
ACCEL_FS_SEL_4G = 0
ACCEL_FS_SEL_8G = 1
GYRO_FS_SEL_1000DPS = 1
GYRO_FS_SEL_250DPS = 3
GYRO_FS_SEL_500DPS = 2
SF_DEG_S = 1
SF_G = 1
SF_M_S2 = 9.80665
SF_RAD_S = 57.29578

class Sh200q:
    ''
    def _accel_fs():
        pass

    def _gyro_fs():
        pass

    def _regChar():
        pass

    def _regInit():
        pass

    def _regThreeShort():
        pass

    acceleration = None
    def adcRest():
        pass

    def deinit():
        pass

    gyro = None
    ypr = None
_ACCEL_SO_16G = 2048
_ACCEL_SO_4G = 8192
_ACCEL_SO_8G = 4096
_GYRO_SO_1000DPS = 32.8
_GYRO_SO_250DPS = 131
_GYRO_SO_500DPS = 65.5
def const():
    pass

i2c_bus = None
math = None
time = None
ustruct = None
