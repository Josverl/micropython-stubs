from machine import SPI as SPI
from micropython import const as const

LDO2: int
DOTSTAR_CLK: int
DOTSTAR_DATA: int
SPI_MOSI: int
SPI_MISO: int
SPI_CLK: int
I2C_SDA: int
I2C_SCL: int
DAC1: int
DAC2: int
LED: int
AMB_LIGHT: int

def set_led(state) -> None: ...
def toggle_led(state) -> None: ...
def get_amb_light(): ...
def set_ldo2_power(state) -> None:
    """Set the power for the on-board Dotstar to allow no current draw when not needed."""

def dotstar_color_wheel(wheel_pos):
    """Color wheel to allow for cycling through the rainbow of RGB colors."""

def go_deepsleep(t) -> None:
    """Deep sleep helper that also powers down the on-board Dotstar."""
