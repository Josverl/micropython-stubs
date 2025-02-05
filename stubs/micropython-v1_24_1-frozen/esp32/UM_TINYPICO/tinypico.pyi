from machine import SPI as SPI
from micropython import const as const

BAT_VOLTAGE: int
BAT_CHARGE: int
DOTSTAR_CLK: int
DOTSTAR_DATA: int
DOTSTAR_PWR: int
SPI_MOSI: int
SPI_CLK: int
SPI_MISO: int
I2C_SDA: int
I2C_SCL: int
DAC1: int
DAC2: int

def get_battery_voltage():
    """
    Returns the current battery voltage. If no battery is connected, returns 3.7V
    This is an approximation only, but useful to detect of the charge state of the battery is getting low.
    """

def get_battery_charging():
    """
    Returns the current battery charging state.
    This can trigger false positives as the charge IC can't tell the difference between a full battery or no battery connected.
    """

def set_dotstar_power(state) -> None:
    """Set the power for the on-board Dotstar to allow no current draw when not needed."""

def dotstar_color_wheel(wheel_pos):
    """Color wheel to allow for cycling through the rainbow of RGB colors."""

def go_deepsleep(t) -> None:
    """Deep sleep helper that also powers down the on-board Dotstar."""
