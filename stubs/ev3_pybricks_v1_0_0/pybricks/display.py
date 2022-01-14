"""
Module: 'pybricks.display' on LEGO EV3 v1.0.0
"""
# MCU: sysname=ev3, nodename=ev3, release=('v1.0.0',), version=('0.0.0',), machine=ev3
# Stubber: 1.3.2 - updated
from typing import Any


class Align:
    """"""

    BOTTOM = 2
    BOTTOM_LEFT = 1
    BOTTOM_RIGHT = 3
    CENTER = 5
    LEFT = 4
    RIGHT = 6
    TOP = 8
    TOP_LEFT = 7
    TOP_RIGHT = 9


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


class Ev3devDisplay:
    """"""

    def image(self, *argv) -> Any:
        pass

    def reset_screen(self, *argv) -> Any:
        pass

    def scroll(self, *argv) -> Any:
        pass

    def text_grid(self, *argv) -> Any:
        pass

    def text_pixels(self, *argv) -> Any:
        pass


class ImageFile:
    """"""


path = None
