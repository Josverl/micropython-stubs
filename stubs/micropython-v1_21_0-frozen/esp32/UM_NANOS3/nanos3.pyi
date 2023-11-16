from _typeshed import Incomplete
from machine import ADC as ADC

RGB_DATA: Incomplete
RGB_PWR: Incomplete
SPI_MOSI: Incomplete
SPI_MISO: Incomplete
SPI_CLK: Incomplete
I2C_SDA: Incomplete
I2C_SCL: Incomplete

def set_pixel_power(state) -> None:
    """Enable or Disable power to the onboard NeoPixel to either show colour, or to reduce power for deep sleep."""

def rgb_color_wheel(wheel_pos):
    """Color wheel to allow for cycling through the rainbow of RGB colors."""
