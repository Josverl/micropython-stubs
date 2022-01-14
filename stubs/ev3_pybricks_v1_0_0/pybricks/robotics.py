"""
Module: 'pybricks.robotics' on LEGO EV3 v1.0.0
"""
# MCU: sysname=ev3, nodename=ev3, release=('v1.0.0',), version=('0.0.0',), machine=ev3
# Stubber: 1.3.2 - updated
from typing import Any


class DriveBase:
    """"""

    def drive(self, *argv) -> Any:
        pass

    def drive_time(self, *argv) -> Any:
        pass

    def stop(self, *argv) -> Any:
        pass


class Stop:
    """"""

    BRAKE = 1
    COAST = 0
    HOLD = 2


pi = 3.141592653589793


def wait():
    pass
