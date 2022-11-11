import framebuf
from _typeshed import Incomplete

SET_CONTRAST: Incomplete
SET_ENTIRE_ON: Incomplete
SET_NORM_INV: Incomplete
SET_DISP: Incomplete
SET_MEM_ADDR: Incomplete
SET_COL_ADDR: Incomplete
SET_PAGE_ADDR: Incomplete
SET_DISP_START_LINE: Incomplete
SET_SEG_REMAP: Incomplete
SET_MUX_RATIO: Incomplete
SET_IREF_SELECT: Incomplete
SET_COM_OUT_DIR: Incomplete
SET_DISP_OFFSET: Incomplete
SET_COM_PIN_CFG: Incomplete
SET_DISP_CLK_DIV: Incomplete
SET_PRECHARGE: Incomplete
SET_VCOM_DESEL: Incomplete
SET_CHARGE_PUMP: Incomplete

class SSD1306(framebuf.FrameBuffer):
    width: Incomplete
    height: Incomplete
    external_vcc: Incomplete
    pages: Incomplete
    buffer: Incomplete
    def __init__(self, width, height, external_vcc) -> None: ...
    def init_display(self) -> None: ...
    def poweroff(self) -> None: ...
    def poweron(self) -> None: ...
    def contrast(self, contrast) -> None: ...
    def invert(self, invert) -> None: ...
    def rotate(self, rotate) -> None: ...
    def show(self) -> None: ...

class SSD1306_I2C(SSD1306):
    i2c: Incomplete
    addr: Incomplete
    temp: Incomplete
    write_list: Incomplete
    def __init__(self, width, height, i2c, addr: int = ..., external_vcc: bool = ...) -> None: ...
    def write_cmd(self, cmd) -> None: ...
    def write_data(self, buf) -> None: ...

class SSD1306_SPI(SSD1306):
    rate: Incomplete
    spi: Incomplete
    dc: Incomplete
    res: Incomplete
    cs: Incomplete
    def __init__(self, width, height, spi, dc, res, cs, external_vcc: bool = ...) -> None: ...
    def write_cmd(self, cmd) -> None: ...
    def write_data(self, buf) -> None: ...
