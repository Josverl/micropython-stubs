"""
Module: 'ssd1306' on micropython-v1.17-esp8266
"""
# MCU: {'ver': 'v1.17', 'port': 'esp8266', 'arch': 'xtensa', 'sysname': 'esp8266', 'release': '1.17', 'name': 'micropython', 'mpy': 9733, 'version': '1.17', 'machine': 'ESP module with ESP8266', 'build': '', 'nodename': 'esp8266', 'platform': 'esp8266', 'family': 'micropython'}
# Stubber: 1.5.4
from typing import Any


def const(*args, **kwargs) -> Any:
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
SET_IREF_SELECT = 173  # type: int
SET_COM_OUT_DIR = 192  # type: int
SET_DISP_OFFSET = 211  # type: int
SET_COM_PIN_CFG = 218  # type: int
SET_DISP_CLK_DIV = 213  # type: int
SET_PRECHARGE = 217  # type: int
SET_VCOM_DESEL = 219  # type: int
SET_CHARGE_PUMP = 141  # type: int


class SSD1306:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def blit(self, *args, **kwargs) -> Any:
        ...

    def fill(self, *args, **kwargs) -> Any:
        ...

    def fill_rect(self, *args, **kwargs) -> Any:
        ...

    def hline(self, *args, **kwargs) -> Any:
        ...

    def invert(self, *args, **kwargs) -> Any:
        ...

    def line(self, *args, **kwargs) -> Any:
        ...

    def pixel(self, *args, **kwargs) -> Any:
        ...

    def rect(self, *args, **kwargs) -> Any:
        ...

    def scroll(self, *args, **kwargs) -> Any:
        ...

    def text(self, *args, **kwargs) -> Any:
        ...

    def vline(self, *args, **kwargs) -> Any:
        ...

    def init_display(self, *args, **kwargs) -> Any:
        ...

    def poweroff(self, *args, **kwargs) -> Any:
        ...

    def poweron(self, *args, **kwargs) -> Any:
        ...

    def contrast(self, *args, **kwargs) -> Any:
        ...

    def rotate(self, *args, **kwargs) -> Any:
        ...

    def show(self, *args, **kwargs) -> Any:
        ...


class SSD1306_I2C:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def blit(self, *args, **kwargs) -> Any:
        ...

    def fill(self, *args, **kwargs) -> Any:
        ...

    def fill_rect(self, *args, **kwargs) -> Any:
        ...

    def hline(self, *args, **kwargs) -> Any:
        ...

    def invert(self, *args, **kwargs) -> Any:
        ...

    def line(self, *args, **kwargs) -> Any:
        ...

    def pixel(self, *args, **kwargs) -> Any:
        ...

    def rect(self, *args, **kwargs) -> Any:
        ...

    def scroll(self, *args, **kwargs) -> Any:
        ...

    def text(self, *args, **kwargs) -> Any:
        ...

    def vline(self, *args, **kwargs) -> Any:
        ...

    def init_display(self, *args, **kwargs) -> Any:
        ...

    def poweroff(self, *args, **kwargs) -> Any:
        ...

    def poweron(self, *args, **kwargs) -> Any:
        ...

    def contrast(self, *args, **kwargs) -> Any:
        ...

    def rotate(self, *args, **kwargs) -> Any:
        ...

    def show(self, *args, **kwargs) -> Any:
        ...

    def write_cmd(self, *args, **kwargs) -> Any:
        ...

    def write_data(self, *args, **kwargs) -> Any:
        ...


class SSD1306_SPI:
    """"""

    def __init__(self, *argv, **kwargs) -> None:
        """"""
        ...

    def blit(self, *args, **kwargs) -> Any:
        ...

    def fill(self, *args, **kwargs) -> Any:
        ...

    def fill_rect(self, *args, **kwargs) -> Any:
        ...

    def hline(self, *args, **kwargs) -> Any:
        ...

    def invert(self, *args, **kwargs) -> Any:
        ...

    def line(self, *args, **kwargs) -> Any:
        ...

    def pixel(self, *args, **kwargs) -> Any:
        ...

    def rect(self, *args, **kwargs) -> Any:
        ...

    def scroll(self, *args, **kwargs) -> Any:
        ...

    def text(self, *args, **kwargs) -> Any:
        ...

    def vline(self, *args, **kwargs) -> Any:
        ...

    def init_display(self, *args, **kwargs) -> Any:
        ...

    def poweroff(self, *args, **kwargs) -> Any:
        ...

    def poweron(self, *args, **kwargs) -> Any:
        ...

    def contrast(self, *args, **kwargs) -> Any:
        ...

    def rotate(self, *args, **kwargs) -> Any:
        ...

    def show(self, *args, **kwargs) -> Any:
        ...

    def write_cmd(self, *args, **kwargs) -> Any:
        ...

    def write_data(self, *args, **kwargs) -> Any:
        ...
