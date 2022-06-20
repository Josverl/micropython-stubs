from typing import Any

VBUS_SENSE: Any
VBAT_SENSE: Any
RGB_DATA: Any
LDO2: Any
SPI_MOSI: Any
SPI_MISO: Any
SPI_CLK: Any
I2C_SDA: Any
I2C_SCL: Any

def set_ldo2_power(state) -> None: ...
def get_battery_voltage(): ...
def get_vbus_present(): ...
def rgb_color_wheel(wheel_pos): ...
