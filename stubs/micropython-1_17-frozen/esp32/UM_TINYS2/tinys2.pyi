from machine import SPI as SPI
from typing import Any

VBUS_SENSE: Any
VBAT_SENSE: Any
RGB_DATA: Any
RGB_PWR: Any
SPI_MOSI: Any
SPI_MISO: Any
SPI_CLK: Any
I2C_SDA: Any
I2C_SCL: Any
DAC1: Any
DAC2: Any

def set_pixel_power(state) -> None: ...
def get_battery_voltage(): ...
def get_vbus_present(): ...
def rgb_color_wheel(wheel_pos): ...
def go_deepsleep(t) -> None: ...
