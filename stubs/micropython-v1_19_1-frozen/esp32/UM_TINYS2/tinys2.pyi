from _typeshed import Incomplete
from machine import SPI as SPI

VBUS_SENSE: Incomplete
VBAT_SENSE: Incomplete
RGB_DATA: Incomplete
RGB_PWR: Incomplete
SPI_MOSI: Incomplete
SPI_MISO: Incomplete
SPI_CLK: Incomplete
I2C_SDA: Incomplete
I2C_SCL: Incomplete
DAC1: Incomplete
DAC2: Incomplete

def set_pixel_power(state) -> None: ...
def get_battery_voltage(): ...
def get_vbus_present(): ...
def rgb_color_wheel(wheel_pos): ...
def go_deepsleep(t) -> None: ...
