"""
Module: 'lcd160cr' on micropython-v1.17-pyboard
"""
# MCU: {'ver': 'v1.17', 'port': 'pyboard', 'arch': 'armv7emsp', 'sysname': 'pyboard', 'release': '1.17.0', 'name': 'micropython', 'mpy': 7685, 'version': '1.17.0', 'machine': 'PYBv1.1 with STM32F405RG', 'build': '', 'nodename': 'pyboard', 'platform': 'pyboard', 'family': 'micropython'}
# Stubber: 1.5.2
from typing import Any


def const(*args) -> Any:
    ...


def calcsize(*args) -> Any:
    ...


def pack_into(*args) -> Any:
    ...


def sleep_ms(*args) -> Any:
    ...


PORTRAIT = 0  # type: int
LANDSCAPE = 1  # type: int
PORTRAIT_UPSIDEDOWN = 2  # type: int
LANDSCAPE_UPSIDEDOWN = 3  # type: int
STARTUP_DECO_NONE = 0  # type: int
STARTUP_DECO_MLOGO = 1  # type: int
STARTUP_DECO_INFO = 2  # type: int


class LCD160CR:
    """"""

    def __init__(self, *args) -> None:
        ...

    def write(self, *args) -> Any:
        ...

    def line(self, *args) -> Any:
        ...

    def rect(self, *args) -> Any:
        ...

    def reset(self, *args) -> Any:
        ...

    def oflush(self, *args) -> Any:
        ...

    def iflush(self, *args) -> Any:
        ...

    def rgb(self, *args) -> Any:
        ...

    def clip_line(self, *args) -> Any:
        ...

    def set_power(self, *args) -> Any:
        ...

    def set_orient(self, *args) -> Any:
        ...

    def set_brightness(self, *args) -> Any:
        ...

    def set_i2c_addr(self, *args) -> Any:
        ...

    def set_uart_baudrate(self, *args) -> Any:
        ...

    def set_startup_deco(self, *args) -> Any:
        ...

    def save_to_flash(self, *args) -> Any:
        ...

    def set_pixel(self, *args) -> Any:
        ...

    def get_pixel(self, *args) -> Any:
        ...

    def get_line(self, *args) -> Any:
        ...

    def screen_dump(self, *args) -> Any:
        ...

    def screen_load(self, *args) -> Any:
        ...

    def set_pos(self, *args) -> Any:
        ...

    def set_text_color(self, *args) -> Any:
        ...

    def set_font(self, *args) -> Any:
        ...

    def set_pen(self, *args) -> Any:
        ...

    def erase(self, *args) -> Any:
        ...

    def dot(self, *args) -> Any:
        ...

    def rect_outline(self, *args) -> Any:
        ...

    def rect_interior(self, *args) -> Any:
        ...

    def dot_no_clip(self, *args) -> Any:
        ...

    def rect_no_clip(self, *args) -> Any:
        ...

    def rect_outline_no_clip(self, *args) -> Any:
        ...

    def rect_interior_no_clip(self, *args) -> Any:
        ...

    def line_no_clip(self, *args) -> Any:
        ...

    def poly_dot(self, *args) -> Any:
        ...

    def poly_line(self, *args) -> Any:
        ...

    def touch_config(self, *args) -> Any:
        ...

    def is_touched(self, *args) -> Any:
        ...

    def get_touch(self, *args) -> Any:
        ...

    def set_spi_win(self, *args) -> Any:
        ...

    def fast_spi(self, *args) -> Any:
        ...

    def show_framebuf(self, *args) -> Any:
        ...

    def set_scroll(self, *args) -> Any:
        ...

    def set_scroll_win(self, *args) -> Any:
        ...

    def set_scroll_win_param(self, *args) -> Any:
        ...

    def set_scroll_buf(self, *args) -> Any:
        ...

    def jpeg_start(self, *args) -> Any:
        ...

    def jpeg_data(self, *args) -> Any:
        ...

    def jpeg(self, *args) -> Any:
        ...

    def feed_wdt(self, *args) -> Any:
        ...
