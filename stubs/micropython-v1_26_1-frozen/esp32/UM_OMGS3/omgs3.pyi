from _typeshed import Incomplete
from micropython import const as const

fg_i2c: Incomplete
max17048: Incomplete

def get_bat_voltage():
    """Read the battery voltage from the fuel gauge"""

def get_state_of_charge():
    """Read the battery state of charge from the fuel gauge"""

def get_vbus_present():
    """Detect if VBUS (5V) power source is present"""

def set_pixel_power(state) -> None:
    """Enable or Disable power to the onboard NeoPixel to either show colour, or to reduce power for deep sleep."""

def rgb_color_wheel(wheel_pos):
    """Color wheel to allow for cycling through the rainbow of RGB colors."""
