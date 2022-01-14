"""
Module: 'flowlib.lib.imu' on M5 FlowUI v1.4.0-beta
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-284-g5d8e1c867 on 2019-08-30', machine='ESP32 module with ESP32')
# Stubber: 1.3.1 - updated
from typing import Any


class IMU:
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


MPU6050_ADDR = 104
SH200Q_ADDR = 108
i2c_bus = None
imu_i2c = None
mpu6050 = None
