from _typeshed import Incomplete
from machine import SPI as SPI

LDO2: Incomplete
DOTSTAR_CLK: Incomplete
DOTSTAR_DATA: Incomplete
SPI_MOSI: Incomplete
SPI_MISO: Incomplete
SPI_CLK: Incomplete
I2C_SDA: Incomplete
I2C_SCL: Incomplete
DAC1: Incomplete
DAC2: Incomplete
LED: Incomplete
AMB_LIGHT: Incomplete

def set_led(state) -> None: ...
def toggle_led(state) -> None: ...
def get_amb_light(): ...
def set_ldo2_power(state) -> None:
    """Set the power for the on-board Dotstar to allow no current draw when not needed."""

def dotstar_color_wheel(wheel_pos):
    """Color wheel to allow for cycling through the rainbow of RGB colors."""

def go_deepsleep(t) -> None:
    """Deep sleep helper that also powers down the on-board Dotstar."""
