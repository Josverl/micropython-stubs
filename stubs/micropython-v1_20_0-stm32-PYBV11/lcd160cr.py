"""
Module: 'lcd160cr' on micropython-v1.20.0-stm32-PYBV11
"""
# MCU: OrderedDict({'version': '1.20.0', 'mpy': 'v6.1', 'port': 'stm32', 'board': 'PYBV11', 'family': 'micropython', 'build': '', 'arch': 'armv7emsp', 'ver': 'v1.20.0', 'cpu': 'STM32F405RG'})
# Stubber: v1.13.7
from typing import Any

LANDSCAPE = 1  # type: int
PORTRAIT_UPSIDEDOWN = 2  # type: int
PORTRAIT = 0  # type: int
STARTUP_DECO_INFO = 2  # type: int
STARTUP_DECO_MLOGO = 1  # type: int
LANDSCAPE_UPSIDEDOWN = 3  # type: int
STARTUP_DECO_NONE = 0  # type: int


def calcsize(*args, **kwargs) -> Any:
    ...


def pack_into(*args, **kwargs) -> Any:
    ...


def sleep_ms(*args, **kwargs) -> Any:
    ...


def const(*args, **kwargs) -> Any:
    ...


class LCD160CR:
    def line_no_clip(self, *args, **kwargs) -> Any:
        ...

    def erase(self, *args, **kwargs) -> Any:
        ...

    def rect_interior_no_clip(self, *args, **kwargs) -> Any:
        ...

    def touch_config(self, *args, **kwargs) -> Any:
        ...

    def poly_dot(self, *args, **kwargs) -> Any:
        ...

    def poly_line(self, *args, **kwargs) -> Any:
        ...

    def rect_outline(self, *args, **kwargs) -> Any:
        ...

    def rect_outline_no_clip(self, *args, **kwargs) -> Any:
        ...

    def dot(self, *args, **kwargs) -> Any:
        ...

    def rect_no_clip(self, *args, **kwargs) -> Any:
        ...

    def rect_interior(self, *args, **kwargs) -> Any:
        ...

    def dot_no_clip(self, *args, **kwargs) -> Any:
        ...

    def set_scroll_buf(self, *args, **kwargs) -> Any:
        ...

    def is_touched(self, *args, **kwargs) -> Any:
        ...

    def set_scroll_win_param(self, *args, **kwargs) -> Any:
        ...

    def jpeg(self, *args, **kwargs) -> Any:
        ...

    def jpeg_start(self, *args, **kwargs) -> Any:
        ...

    def jpeg_data(self, *args, **kwargs) -> Any:
        ...

    def set_spi_win(self, *args, **kwargs) -> Any:
        ...

    def set_scroll_win(self, *args, **kwargs) -> Any:
        ...

    def get_touch(self, *args, **kwargs) -> Any:
        ...

    def set_scroll(self, *args, **kwargs) -> Any:
        ...

    def fast_spi(self, *args, **kwargs) -> Any:
        ...

    def show_framebuf(self, *args, **kwargs) -> Any:
        ...

    def feed_wdt(self, *args, **kwargs) -> Any:
        ...

    def rgb(self, *args, **kwargs) -> Any:
        ...

    def set_pen(self, *args, **kwargs) -> Any:
        ...

    def iflush(self, *args, **kwargs) -> Any:
        ...

    def set_brightness(self, *args, **kwargs) -> Any:
        ...

    def clip_line(self, *args, **kwargs) -> Any:
        ...

    def set_power(self, *args, **kwargs) -> Any:
        ...

    def line(self, *args, **kwargs) -> Any:
        ...

    def oflush(self, *args, **kwargs) -> Any:
        ...

    def write(self, *args, **kwargs) -> Any:
        ...

    def set_orient(self, *args, **kwargs) -> Any:
        ...

    def rect(self, *args, **kwargs) -> Any:
        ...

    def reset(self, *args, **kwargs) -> Any:
        ...

    def screen_load(self, *args, **kwargs) -> Any:
        ...

    def set_i2c_addr(self, *args, **kwargs) -> Any:
        ...

    def screen_dump(self, *args, **kwargs) -> Any:
        ...

    def set_font(self, *args, **kwargs) -> Any:
        ...

    def set_pos(self, *args, **kwargs) -> Any:
        ...

    def set_text_color(self, *args, **kwargs) -> Any:
        ...

    def set_startup_deco(self, *args, **kwargs) -> Any:
        ...

    def get_line(self, *args, **kwargs) -> Any:
        ...

    def set_uart_baudrate(self, *args, **kwargs) -> Any:
        ...

    def get_pixel(self, *args, **kwargs) -> Any:
        ...

    def save_to_flash(self, *args, **kwargs) -> Any:
        ...

    def set_pixel(self, *args, **kwargs) -> Any:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...
