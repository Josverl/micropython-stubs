from ssd1306 import SSD1306_I2C

class OLED(SSD1306_I2C):
    def __init__(self, i2c) -> None: ...
    def test(self) -> None: ...
    def display_wifi(self) -> None: ...
