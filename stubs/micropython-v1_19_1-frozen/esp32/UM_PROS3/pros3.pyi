from _typeshed import Incomplete

VBUS_SENSE: Incomplete
VBAT_SENSE: Incomplete
RGB_DATA: Incomplete
LDO2: Incomplete
SPI_MOSI: Incomplete
SPI_MISO: Incomplete
SPI_CLK: Incomplete
I2C_SDA: Incomplete
I2C_SCL: Incomplete

def set_ldo2_power(state) -> None: ...
def get_battery_voltage(): ...
def get_vbus_present(): ...
def rgb_color_wheel(wheel_pos): ...
