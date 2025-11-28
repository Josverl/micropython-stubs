from machine import ADC as ADC
from micropython import const as const

RGB_DATA: int
RGB_PWR: int
SPI_MOSI: int
SPI_MISO: int
SPI_CLK: int
I2C_SDA: int
I2C_SCL: int

def set_pixel_power(state) -> None:
    """Enable or Disable power to the onboard NeoPixel to either show colour, or to reduce power for deep sleep."""

def rgb_color_wheel(wheel_pos):
    """Color wheel to allow for cycling through the rainbow of RGB colors."""
