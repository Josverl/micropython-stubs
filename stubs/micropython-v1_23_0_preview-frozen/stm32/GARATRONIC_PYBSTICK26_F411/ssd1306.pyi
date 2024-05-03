import framebuf
from _typeshed import Incomplete
from micropython import const as const

SET_CONTRAST: int
SET_ENTIRE_ON: int
SET_NORM_INV: int
SET_DISP: int
SET_MEM_ADDR: int
SET_COL_ADDR: int
SET_PAGE_ADDR: int
SET_DISP_START_LINE: int
SET_SEG_REMAP: int
SET_MUX_RATIO: int
SET_IREF_SELECT: int
SET_COM_OUT_DIR: int
SET_DISP_OFFSET: int
SET_COM_PIN_CFG: int
SET_DISP_CLK_DIV: int
SET_PRECHARGE: int
SET_VCOM_DESEL: int
SET_CHARGE_PUMP: int

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
    def __init__(self, width, height, i2c, addr: int = 60, external_vcc: bool = False) -> None: ...
    def write_cmd(self, cmd) -> None: ...
    def write_data(self, buf) -> None: ...

class SSD1306_SPI(SSD1306):
    rate: Incomplete
    spi: Incomplete
    dc: Incomplete
    res: Incomplete
    cs: Incomplete
    def __init__(self, width, height, spi, dc, res, cs, external_vcc: bool = False) -> None: ...
    def write_cmd(self, cmd) -> None: ...
    def write_data(self, buf) -> None: ...
