from machine import SPI as SPI
from typing import Any

LDO2: Any
DOTSTAR_CLK: Any
DOTSTAR_DATA: Any
SPI_MOSI: Any
SPI_MISO: Any
SPI_CLK: Any
I2C_SDA: Any
I2C_SCL: Any
DAC1: Any
DAC2: Any
LED: Any
AMB_LIGHT: Any

def set_led(state) -> None: ...
def toggle_led(state) -> None: ...
def get_amb_light(): ...
def set_ldo2_power(state) -> None: ...
def dotstar_color_wheel(wheel_pos): ...
def go_deepsleep(t) -> None: ...
