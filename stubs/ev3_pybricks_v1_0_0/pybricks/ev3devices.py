"""
Module: 'pybricks.ev3devices' on LEGO EV3 v1.0.0
"""
# MCU: sysname=ev3, nodename=ev3, release=('v1.0.0',), version=('0.0.0',), machine=ev3
# Stubber: 1.3.2 - updated
from typing import Any


class Button:
    """"""

    BEACON = 256
    CENTER = 32
    DOWN = 4
    LEFT = 16
    LEFT_DOWN = 2
    LEFT_UP = 128
    RIGHT = 64
    RIGHT_DOWN = 8
    RIGHT_UP = 512
    UP = 256


class Color:
    """"""

    BLACK = 1
    BLUE = 2
    BROWN = 7
    GREEN = 3
    ORANGE = 8
    PURPLE = 9
    RED = 5
    WHITE = 6
    YELLOW = 4


class ColorSensor:
    """"""

    def _close_files(self, *argv) -> Any:
        pass

    _default_mode = None
    _ev3dev_driver_name = "lego-ev3-color"

    def _mode(self, *argv) -> Any:
        pass

    _number_of_values = 3

    def _open_files(self, *argv) -> Any:
        pass

    def _value(self, *argv) -> Any:
        pass

    def ambient(self, *argv) -> Any:
        pass

    def color(self, *argv) -> Any:
        pass

    def reflection(self, *argv) -> Any:
        pass

    def rgb(self, *argv) -> Any:
        pass


class Direction:
    """"""

    CLOCKWISE = 0
    COUNTERCLOCKWISE = 1


class Ev3devSensor:
    """"""

    def _close_files(self, *argv) -> Any:
        pass

    _default_mode = None
    _ev3dev_driver_name = "none"

    def _mode(self, *argv) -> Any:
        pass

    _number_of_values = 1

    def _open_files(self, *argv) -> Any:
        pass

    def _value(self, *argv) -> Any:
        pass


class Ev3devUartSensor:
    """"""

    def _close_files(self, *argv) -> Any:
        pass

    _default_mode = None
    _ev3dev_driver_name = "none"

    def _mode(self, *argv) -> Any:
        pass

    _number_of_values = 1

    def _open_files(self, *argv) -> Any:
        pass

    def _reset(self, *argv) -> Any:
        pass

    def _reset_port(self, *argv) -> Any:
        pass

    def _value(self, *argv) -> Any:
        pass


class GyroSensor:
    """"""

    def _calibrate(self, *argv) -> Any:
        pass

    def _close_files(self, *argv) -> Any:
        pass

    _default_mode = "GYRO-G&A"
    _ev3dev_driver_name = "lego-ev3-gyro"

    def _mode(self, *argv) -> Any:
        pass

    _number_of_values = 2

    def _open_files(self, *argv) -> Any:
        pass

    def _reset(self, *argv) -> Any:
        pass

    def _reset_port(self, *argv) -> Any:
        pass

    def _value(self, *argv) -> Any:
        pass

    def angle(self, *argv) -> Any:
        pass

    def reset_angle(self, *argv) -> Any:
        pass

    def speed(self, *argv) -> Any:
        pass


class InfraredSensor:
    """"""

    def _close_files(self, *argv) -> Any:
        pass

    _combinations = None
    _default_mode = None
    _ev3dev_driver_name = "lego-ev3-ir"

    def _mode(self, *argv) -> Any:
        pass

    _number_of_values = 8

    def _open_files(self, *argv) -> Any:
        pass

    def _value(self, *argv) -> Any:
        pass

    def beacon(self, *argv) -> Any:
        pass

    def buttons(self, *argv) -> Any:
        pass

    def distance(self, *argv) -> Any:
        pass


class Motor:
    """"""

    def angle(self, *argv) -> Any:
        pass

    def dc(self, *argv) -> Any:
        pass

    def reset_angle(self, *argv) -> Any:
        pass

    def run(self, *argv) -> Any:
        pass

    def run_angle(self, *argv) -> Any:
        pass

    def run_target(self, *argv) -> Any:
        pass

    def run_time(self, *argv) -> Any:
        pass

    def run_until_stalled(self, *argv) -> Any:
        pass

    def set_dc_settings(self, *argv) -> Any:
        pass

    def set_pid_settings(self, *argv) -> Any:
        pass

    def set_run_settings(self, *argv) -> Any:
        pass

    def speed(self, *argv) -> Any:
        pass

    def stalled(self, *argv) -> Any:
        pass

    def stop(self, *argv) -> Any:
        pass

    def track_target(self, *argv) -> Any:
        pass


class StopWatch:
    """"""

    def pause(self, *argv) -> Any:
        pass

    def reset(self, *argv) -> Any:
        pass

    def resume(self, *argv) -> Any:
        pass

    def time(self, *argv) -> Any:
        pass


class TouchSensor:
    """"""

    def _close_files(self, *argv) -> Any:
        pass

    _default_mode = None
    _ev3dev_driver_name = "lego-ev3-touch"

    def _mode(self, *argv) -> Any:
        pass

    _number_of_values = 1

    def _open_files(self, *argv) -> Any:
        pass

    def _value(self, *argv) -> Any:
        pass

    def pressed(self, *argv) -> Any:
        pass


class UltrasonicSensor:
    """"""

    PING_WAIT = 300

    def _close_files(self, *argv) -> Any:
        pass

    _default_mode = None
    _ev3dev_driver_name = "lego-ev3-us"

    def _mode(self, *argv) -> Any:
        pass

    _number_of_values = 1

    def _open_files(self, *argv) -> Any:
        pass

    def _value(self, *argv) -> Any:
        pass

    def distance(self, *argv) -> Any:
        pass

    def presence(self, *argv) -> Any:
        pass


def wait():
    pass
