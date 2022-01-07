import framebuf
from typing import Any

SET_CONTRAST: Any
SET_ENTIRE_ON: Any
SET_NORM_INV: Any
SET_DISP: Any
SET_MEM_ADDR: Any
SET_COL_ADDR: Any
SET_PAGE_ADDR: Any
SET_DISP_START_LINE: Any
SET_SEG_REMAP: Any
SET_MUX_RATIO: Any
SET_COM_OUT_DIR: Any
SET_DISP_OFFSET: Any
SET_COM_PIN_CFG: Any
SET_DISP_CLK_DIV: Any
SET_PRECHARGE: Any
SET_VCOM_DESEL: Any
SET_CHARGE_PUMP: Any

class SSD1306(framebuf.FrameBuffer):
    width: Any
    height: Any
    external_vcc: Any
    pages: Any
    buffer: Any
    def __init__(self, width, height, external_vcc) -> None: ...
    def init_display(self) -> None: ...
    def poweroff(self) -> None: ...
    def poweron(self) -> None: ...
    def contrast(self, contrast) -> None: ...
    def invert(self, invert) -> None: ...
    def show(self) -> None: ...

class SSD1306_I2C(SSD1306):
    i2c: Any
    addr: Any
    temp: Any
    def __init__(self, width, height, i2c, addr: int = ..., external_vcc: bool = ...) -> None: ...
    def write_cmd(self, cmd) -> None: ...
    def write_data(self, buf) -> None: ...

class SSD1306_SPI(SSD1306):
    rate: Any
    spi: Any
    dc: Any
    res: Any
    cs: Any
    def __init__(self, width, height, spi, dc, res, cs, external_vcc: bool = ...) -> None: ...
    def write_cmd(self, cmd) -> None: ...
    def write_data(self, buf) -> None: ...
