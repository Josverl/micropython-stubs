"""
Module: 'flowlib.modules._lego' on M5 FlowUI v1.4.0-beta
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-284-g5d8e1c867 on 2019-08-30', machine='ESP32 module with ESP32')
# Stubber: 1.3.1 - updated
from typing import Any

ENCODER_ADDR = 4


class Lego:
    """"""

    def deinit(self, *argv) -> Any:
        pass


class Lego_Motor:
    """"""

    def _available(self, *argv) -> Any:
        pass

    def _read_encoder(self, *argv) -> Any:
        pass

    def deinit(self, *argv) -> Any:
        pass

    def position_update(self, *argv) -> Any:
        pass

    def read_encoder(self, *argv) -> Any:
        pass

    def run_distance(self, *argv) -> Any:
        pass

    def run_to(self, *argv) -> Any:
        pass

    def set_pwm(self, *argv) -> Any:
        pass

    def stop(self, *argv) -> Any:
        pass


M5GO_WHEEL_ADDR = 86
MOTOR_CTRL_ADDR = 0


def const():
    pass


def constrain():
    pass


def dead_area():
    pass


i2c_bus = None
machine = None
module = None
motor1_pwm = 0
motor2_pwm = 0
os = None
time = None
ustruct = None
