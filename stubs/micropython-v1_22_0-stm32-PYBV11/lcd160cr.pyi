from _typeshed import Incomplete as Incomplete

STARTUP_DECO_MLOGO: int
LANDSCAPE_UPSIDEDOWN: int
LANDSCAPE: int
PORTRAIT: int
PORTRAIT_UPSIDEDOWN: int
STARTUP_DECO_INFO: int
STARTUP_DECO_NONE: int

def sleep_ms(*args, **kwargs) -> Incomplete: ...
def const(*args, **kwargs) -> Incomplete: ...
def calcsize(*args, **kwargs) -> Incomplete: ...
def pack_into(*args, **kwargs) -> Incomplete: ...

class LCD160CR:
    def set_font(self, *args, **kwargs) -> Incomplete: ...
    def rect_no_clip(self, *args, **kwargs) -> Incomplete: ...
    def set_brightness(self, *args, **kwargs) -> Incomplete: ...
    def set_pen(self, *args, **kwargs) -> Incomplete: ...
    def set_i2c_addr(self, *args, **kwargs) -> Incomplete: ...
    def set_orient(self, *args, **kwargs) -> Incomplete: ...
    def rect_outline_no_clip(self, *args, **kwargs) -> Incomplete: ...
    def screen_load(self, *args, **kwargs) -> Incomplete: ...
    def rect_outline(self, *args, **kwargs) -> Incomplete: ...
    def screen_dump(self, *args, **kwargs) -> Incomplete: ...
    def rgb(self, *args, **kwargs) -> Incomplete: ...
    def save_to_flash(self, *args, **kwargs) -> Incomplete: ...
    def set_startup_deco(self, *args, **kwargs) -> Incomplete: ...
    def set_pixel(self, *args, **kwargs) -> Incomplete: ...
    def set_spi_win(self, *args, **kwargs) -> Incomplete: ...
    def show_framebuf(self, *args, **kwargs) -> Incomplete: ...
    def set_text_color(self, *args, **kwargs) -> Incomplete: ...
    def set_uart_baudrate(self, *args, **kwargs) -> Incomplete: ...
    def set_power(self, *args, **kwargs) -> Incomplete: ...
    def set_scroll_win_param(self, *args, **kwargs) -> Incomplete: ...
    def set_pos(self, *args, **kwargs) -> Incomplete: ...
    def set_scroll_win(self, *args, **kwargs) -> Incomplete: ...
    def set_scroll(self, *args, **kwargs) -> Incomplete: ...
    def set_scroll_buf(self, *args, **kwargs) -> Incomplete: ...
    def touch_config(self, *args, **kwargs) -> Incomplete: ...
    def erase(self, *args, **kwargs) -> Incomplete: ...
    def rect_interior_no_clip(self, *args, **kwargs) -> Incomplete: ...
    def dot_no_clip(self, *args, **kwargs) -> Incomplete: ...
    def get_line(self, *args, **kwargs) -> Incomplete: ...
    def fast_spi(self, *args, **kwargs) -> Incomplete: ...
    def feed_wdt(self, *args, **kwargs) -> Incomplete: ...
    def line(self, *args, **kwargs) -> Incomplete: ...
    def dot(self, *args, **kwargs) -> Incomplete: ...
    def write(self, *args, **kwargs) -> Incomplete: ...
    def clip_line(self, *args, **kwargs) -> Incomplete: ...
    def rect(self, *args, **kwargs) -> Incomplete: ...
    def reset(self, *args, **kwargs) -> Incomplete: ...
    def oflush(self, *args, **kwargs) -> Incomplete: ...
    def get_pixel(self, *args, **kwargs) -> Incomplete: ...
    def line_no_clip(self, *args, **kwargs) -> Incomplete: ...
    def rect_interior(self, *args, **kwargs) -> Incomplete: ...
    def poly_dot(self, *args, **kwargs) -> Incomplete: ...
    def poly_line(self, *args, **kwargs) -> Incomplete: ...
    def iflush(self, *args, **kwargs) -> Incomplete: ...
    def jpeg_start(self, *args, **kwargs) -> Incomplete: ...
    def get_touch(self, *args, **kwargs) -> Incomplete: ...
    def jpeg_data(self, *args, **kwargs) -> Incomplete: ...
    def is_touched(self, *args, **kwargs) -> Incomplete: ...
    def jpeg(self, *args, **kwargs) -> Incomplete: ...
    def __init__(self, *argv, **kwargs) -> None: ...
