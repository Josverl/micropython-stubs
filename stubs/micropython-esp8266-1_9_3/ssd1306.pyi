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
    def contrast() -> None: ...
    def init_display() -> None: ...
    def invert() -> None: ...
    def poweroff() -> None: ...
    def poweron() -> None: ...
    def show() -> None: ...

class SSD1306_I2C:
    def write_cmd() -> None: ...
    def write_data() -> None: ...

class SSD1306_SPI:
    def write_cmd() -> None: ...
    def write_data() -> None: ...

def const() -> None: ...

framebuf: Any
