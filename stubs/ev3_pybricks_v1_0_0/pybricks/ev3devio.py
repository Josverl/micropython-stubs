"""
Module: 'pybricks.ev3devio' on LEGO EV3 v1.0.0
"""
# MCU: sysname=ev3, nodename=ev3, release=('v1.0.0',), version=('0.0.0',), machine=ev3
# Stubber: 1.3.2 - updated
from typing import Any


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


def get_sensor_path():
    pass


def listdir():
    pass


path = None


def read_int():
    pass


def read_str():
    pass


def wait():
    pass


def write_int():
    pass


def write_str():
    pass
