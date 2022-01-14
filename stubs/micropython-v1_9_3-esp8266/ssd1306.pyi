from typing import Any

SET_CHARGE_PUMP: int
SET_COL_ADDR: int
SET_COM_OUT_DIR: int
SET_COM_PIN_CFG: int
SET_CONTRAST: int
SET_DISP: int
SET_DISP_CLK_DIV: int
SET_DISP_OFFSET: int
SET_DISP_START_LINE: int
SET_ENTIRE_ON: int
SET_MEM_ADDR: int
SET_MUX_RATIO: int
SET_NORM_INV: int
SET_PAGE_ADDR: int
SET_PRECHARGE: int
SET_SEG_REMAP: int
SET_VCOM_DESEL: int

class SSD1306:
    def contrast(self, *argv) -> Any: ...
    def init_display(self, *argv) -> Any: ...
    def invert(self, *argv) -> Any: ...
    def poweroff(self, *argv) -> Any: ...
    def poweron(self, *argv) -> Any: ...
    def show(self, *argv) -> Any: ...

class SSD1306_I2C:
    def write_cmd(self, *argv) -> Any: ...
    def write_data(self, *argv) -> Any: ...

class SSD1306_SPI:
    def write_cmd(self, *argv) -> Any: ...
    def write_data(self, *argv) -> Any: ...

def const() -> None: ...

framebuf: Any
