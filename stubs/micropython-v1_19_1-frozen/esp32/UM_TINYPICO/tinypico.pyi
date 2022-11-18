from _typeshed import Incomplete
from machine import SPI as SPI

BAT_VOLTAGE: Incomplete
BAT_CHARGE: Incomplete
DOTSTAR_CLK: Incomplete
DOTSTAR_DATA: Incomplete
DOTSTAR_PWR: Incomplete
SPI_MOSI: Incomplete
SPI_CLK: Incomplete
SPI_MISO: Incomplete
I2C_SDA: Incomplete
I2C_SCL: Incomplete
DAC1: Incomplete
DAC2: Incomplete

def get_battery_voltage(): ...
def get_battery_charging(): ...
def set_dotstar_power(state) -> None: ...
def dotstar_color_wheel(wheel_pos): ...
def go_deepsleep(t) -> None: ...
