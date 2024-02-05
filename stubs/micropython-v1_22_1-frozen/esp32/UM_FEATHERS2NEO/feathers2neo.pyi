from micropython import const as const

VBUS_SENSE: int
VBAT_SENSE: int
RGB_DATA: int
RGB_PWR: int
RGB_MATRIX_DATA: int
RGB_MATRIX_PWR: int
SPI_MOSI: int
SPI_MISO: int
SPI_CLK: int
I2C_SDA: int
I2C_SCL: int
DAC1: int
DAC2: int

def set_pixel_power(state) -> None:
    """Enable or Disable power to the onboard NeoPixel to either show colour, or to reduce power for deep sleep."""

def set_pixel_matrix_power(state) -> None:
    """Enable or Disable power to the onboard NeoPixel RGB Matrix to either show colours, or to reduce power for deep sleep."""

def get_battery_voltage():
    """
    Returns the current battery voltage. If no battery is connected, returns 4.2V which is the charge voltage
    This is an approximation only, but useful to detect if the charge state of the battery is getting low.
    """

def get_vbus_present():
    """Detect if VBUS (5V) power source is present"""

def rgb_color_wheel(wheel_pos):
    """Color wheel to allow for cycling through the rainbow of RGB colors."""

def go_deepsleep(t) -> None:
    """Deep sleep helper that also powers down the on-board NeoPixel."""
