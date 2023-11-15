from _typeshed import Incomplete

VBUS_SENSE: Incomplete
VBAT_SENSE: Incomplete
RGB_DATA: Incomplete
LDO2: Incomplete
LED: Incomplete
AMB_LIGHT: Incomplete
SPI_MOSI: Incomplete
SPI_MISO: Incomplete
SPI_CLK: Incomplete
I2C_SDA: Incomplete
I2C_SCL: Incomplete

def led_set(state) -> None:
    """Set the state of the BLUE LED on IO13"""

def led_blink() -> None:
    """Toggle the BLUE LED on IO13"""

def get_amb_light():
    """Get Ambient Light Sensor reading"""

def set_ldo2_power(state) -> None:
    """Enable or Disable power to the second LDO"""

def get_battery_voltage():
    """
    Returns the current battery voltage. If no battery is connected, returns 4.2V which is the charge voltage
    This is an approximation only, but useful to detect if the charge state of the battery is getting low.
    """

def get_vbus_present():
    """Detect if VBUS (5V) power source is present"""

def rgb_color_wheel(wheel_pos):
    """Color wheel to allow for cycling through the rainbow of RGB colors."""
