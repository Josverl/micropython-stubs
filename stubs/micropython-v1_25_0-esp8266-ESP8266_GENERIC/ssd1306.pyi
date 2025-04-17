"""
Module: 'ssd1306' on micropython-v1.25.0-esp8266-ESP8266_GENERIC
"""
# MCU: {'version': '1.25.0', 'mpy': 'v6.3', 'port': 'esp8266', 'board': 'ESP8266_GENERIC', 'family': 'micropython', 'build': '', 'arch': 'xtensa', 'ver': '1.25.0', 'cpu': 'ESP8266'}
# Stubber: v1.24.0
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

SET_MEM_ADDR: Final[int] = 32
SET_IREF_SELECT: Final[int] = 173
SET_ENTIRE_ON: Final[int] = 164
SET_DISP_START_LINE: Final[int] = 64
SET_DISP_OFFSET: Final[int] = 211
SET_MUX_RATIO: Final[int] = 168
SET_PRECHARGE: Final[int] = 217
SET_PAGE_ADDR: Final[int] = 34
SET_NORM_INV: Final[int] = 166
SET_SEG_REMAP: Final[int] = 160
SET_DISP_CLK_DIV: Final[int] = 213
SET_COL_ADDR: Final[int] = 33
SET_CHARGE_PUMP: Final[int] = 141
SET_VCOM_DESEL: Final[int] = 219
SET_COM_OUT_DIR: Final[int] = 192
SET_DISP: Final[int] = 174
SET_CONTRAST: Final[int] = 129
SET_COM_PIN_CFG: Final[int] = 218
def const(*args, **kwargs) -> Incomplete:
    ...


class SSD1306_SPI():
    def contrast(self, *args, **kwargs) -> Incomplete:
        ...

    def init_display(self, *args, **kwargs) -> Incomplete:
        ...

    def scroll(self, *args, **kwargs) -> Incomplete:
        ...

    def vline(self, *args, **kwargs) -> Incomplete:
        ...

    def text(self, *args, **kwargs) -> Incomplete:
        ...

    def show(self, *args, **kwargs) -> Incomplete:
        ...

    def write_cmd(self, *args, **kwargs) -> Incomplete:
        ...

    def poweroff(self, *args, **kwargs) -> Incomplete:
        ...

    def rotate(self, *args, **kwargs) -> Incomplete:
        ...

    def poweron(self, *args, **kwargs) -> Incomplete:
        ...

    def write_data(self, *args, **kwargs) -> Incomplete:
        ...

    def fill(self, *args, **kwargs) -> Incomplete:
        ...

    def fill_rect(self, *args, **kwargs) -> Incomplete:
        ...

    def rect(self, *args, **kwargs) -> Incomplete:
        ...

    def ellipse(self, *args, **kwargs) -> Incomplete:
        ...

    def blit(self, *args, **kwargs) -> Incomplete:
        ...

    def pixel(self, *args, **kwargs) -> Incomplete:
        ...

    def poly(self, *args, **kwargs) -> Incomplete:
        ...

    def hline(self, *args, **kwargs) -> Incomplete:
        ...

    def line(self, *args, **kwargs) -> Incomplete:
        ...

    def invert(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class SSD1306_I2C():
    def contrast(self, *args, **kwargs) -> Incomplete:
        ...

    def init_display(self, *args, **kwargs) -> Incomplete:
        ...

    def scroll(self, *args, **kwargs) -> Incomplete:
        ...

    def vline(self, *args, **kwargs) -> Incomplete:
        ...

    def text(self, *args, **kwargs) -> Incomplete:
        ...

    def show(self, *args, **kwargs) -> Incomplete:
        ...

    def write_cmd(self, *args, **kwargs) -> Incomplete:
        ...

    def poweroff(self, *args, **kwargs) -> Incomplete:
        ...

    def rotate(self, *args, **kwargs) -> Incomplete:
        ...

    def poweron(self, *args, **kwargs) -> Incomplete:
        ...

    def write_data(self, *args, **kwargs) -> Incomplete:
        ...

    def fill(self, *args, **kwargs) -> Incomplete:
        ...

    def fill_rect(self, *args, **kwargs) -> Incomplete:
        ...

    def rect(self, *args, **kwargs) -> Incomplete:
        ...

    def ellipse(self, *args, **kwargs) -> Incomplete:
        ...

    def blit(self, *args, **kwargs) -> Incomplete:
        ...

    def pixel(self, *args, **kwargs) -> Incomplete:
        ...

    def poly(self, *args, **kwargs) -> Incomplete:
        ...

    def hline(self, *args, **kwargs) -> Incomplete:
        ...

    def line(self, *args, **kwargs) -> Incomplete:
        ...

    def invert(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class SSD1306():
    def contrast(self, *args, **kwargs) -> Incomplete:
        ...

    def vline(self, *args, **kwargs) -> Incomplete:
        ...

    def text(self, *args, **kwargs) -> Incomplete:
        ...

    def scroll(self, *args, **kwargs) -> Incomplete:
        ...

    def rect(self, *args, **kwargs) -> Incomplete:
        ...

    def init_display(self, *args, **kwargs) -> Incomplete:
        ...

    def rotate(self, *args, **kwargs) -> Incomplete:
        ...

    def poweron(self, *args, **kwargs) -> Incomplete:
        ...

    def poweroff(self, *args, **kwargs) -> Incomplete:
        ...

    def show(self, *args, **kwargs) -> Incomplete:
        ...

    def fill_rect(self, *args, **kwargs) -> Incomplete:
        ...

    def fill(self, *args, **kwargs) -> Incomplete:
        ...

    def ellipse(self, *args, **kwargs) -> Incomplete:
        ...

    def blit(self, *args, **kwargs) -> Incomplete:
        ...

    def poly(self, *args, **kwargs) -> Incomplete:
        ...

    def hline(self, *args, **kwargs) -> Incomplete:
        ...

    def pixel(self, *args, **kwargs) -> Incomplete:
        ...

    def line(self, *args, **kwargs) -> Incomplete:
        ...

    def invert(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

