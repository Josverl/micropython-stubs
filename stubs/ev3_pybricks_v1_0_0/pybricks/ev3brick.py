"""
Module: 'pybricks.ev3brick' on LEGO EV3 v1.0.0
"""
# MCU: sysname=ev3, nodename=ev3, release=('v1.0.0',), version=('0.0.0',), machine=ev3
# Stubber: 1.3.2 - updated
from typing import Any


class Display:
    """"""

    _font_height = 8

    def _next_line(self, *argv) -> Any:
        pass

    def _reset_text_history(self, *argv) -> Any:
        pass

    _valid_devices = None

    def clear(self, *argv) -> Any:
        pass

    def image(self, *argv) -> Any:
        pass

    def text(self, *argv) -> Any:
        pass


class Speaker:
    """"""

    _valid_devices = None

    def beep(self, *argv) -> Any:
        pass

    def beeps(self, *argv) -> Any:
        pass

    def file(self, *argv) -> Any:
        pass

    def speech(self, *argv) -> Any:
        pass

    def tune(self, *argv) -> Any:
        pass


battery = None


def buttons():
    pass


display = None


def exit():
    pass


def light():
    pass


sound = None
stderr = None
