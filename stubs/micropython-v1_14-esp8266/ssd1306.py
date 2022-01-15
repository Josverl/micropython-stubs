"""
Module: 'ssd1306' on micropython-v1.14-esp8266
"""
# MCU: {'ver': 'v1.14', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '1.14', 'name': 'micropython', 'mpy': 9733, 'version': '1.14', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
# Stubber: 1.5.0
from typing import Any


def const(*args) -> Any:
    ...


SET_CONTRAST = 129  # type: int
SET_ENTIRE_ON = 164  # type: int
SET_NORM_INV = 166  # type: int
SET_DISP = 174  # type: int
SET_MEM_ADDR = 32  # type: int
SET_COL_ADDR = 33  # type: int
SET_PAGE_ADDR = 34  # type: int
SET_DISP_START_LINE = 64  # type: int
SET_SEG_REMAP = 160  # type: int
SET_MUX_RATIO = 168  # type: int
SET_COM_OUT_DIR = 192  # type: int
SET_DISP_OFFSET = 211  # type: int
SET_COM_PIN_CFG = 218  # type: int
SET_DISP_CLK_DIV = 213  # type: int
SET_PRECHARGE = 217  # type: int
SET_VCOM_DESEL = 219  # type: int
SET_CHARGE_PUMP = 141  # type: int


class SSD1306:
    """"""

    def __init__(self, *args) -> None:
        ...

    def blit(self, *args) -> Any:
        ...

    def fill(self, *args) -> Any:
        ...

    def fill_rect(self, *args) -> Any:
        ...

    def hline(self, *args) -> Any:
        ...

    def invert(self, *args) -> Any:
        ...

    def line(self, *args) -> Any:
        ...

    def pixel(self, *args) -> Any:
        ...

    def rect(self, *args) -> Any:
        ...

    def scroll(self, *args) -> Any:
        ...

    def text(self, *args) -> Any:
        ...

    def vline(self, *args) -> Any:
        ...

    def init_display(self, *args) -> Any:
        ...

    def poweroff(self, *args) -> Any:
        ...

    def poweron(self, *args) -> Any:
        ...

    def contrast(self, *args) -> Any:
        ...

    def show(self, *args) -> Any:
        ...


class SSD1306_I2C:
    """"""

    def __init__(self, *args) -> None:
        ...

    def blit(self, *args) -> Any:
        ...

    def fill(self, *args) -> Any:
        ...

    def fill_rect(self, *args) -> Any:
        ...

    def hline(self, *args) -> Any:
        ...

    def invert(self, *args) -> Any:
        ...

    def line(self, *args) -> Any:
        ...

    def pixel(self, *args) -> Any:
        ...

    def rect(self, *args) -> Any:
        ...

    def scroll(self, *args) -> Any:
        ...

    def text(self, *args) -> Any:
        ...

    def vline(self, *args) -> Any:
        ...

    def init_display(self, *args) -> Any:
        ...

    def poweroff(self, *args) -> Any:
        ...

    def poweron(self, *args) -> Any:
        ...

    def contrast(self, *args) -> Any:
        ...

    def show(self, *args) -> Any:
        ...

    def write_cmd(self, *args) -> Any:
        ...

    def write_data(self, *args) -> Any:
        ...


class SSD1306_SPI:
    """"""

    def __init__(self, *args) -> None:
        ...

    def blit(self, *args) -> Any:
        ...

    def fill(self, *args) -> Any:
        ...

    def fill_rect(self, *args) -> Any:
        ...

    def hline(self, *args) -> Any:
        ...

    def invert(self, *args) -> Any:
        ...

    def line(self, *args) -> Any:
        ...

    def pixel(self, *args) -> Any:
        ...

    def rect(self, *args) -> Any:
        ...

    def scroll(self, *args) -> Any:
        ...

    def text(self, *args) -> Any:
        ...

    def vline(self, *args) -> Any:
        ...

    def init_display(self, *args) -> Any:
        ...

    def poweroff(self, *args) -> Any:
        ...

    def poweron(self, *args) -> Any:
        ...

    def contrast(self, *args) -> Any:
        ...

    def show(self, *args) -> Any:
        ...

    def write_cmd(self, *args) -> Any:
        ...

    def write_data(self, *args) -> Any:
        ...
