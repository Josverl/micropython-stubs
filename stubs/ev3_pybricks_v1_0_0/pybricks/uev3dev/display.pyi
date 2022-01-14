from typing import Any

ARRAY: int

class CompositeOp:
    ALPHA: int
    ATOP: int
    BLEND: int
    BLUR: int
    BUMPMAP: int
    CHANGE_MASK: int
    CLEAR: int
    COLORIZE: int
    COLOR_BURN: int
    COLOR_DODGE: int
    COPY: int
    COPY_ALPHA: int
    COPY_BLACK: int
    COPY_BLUE: int
    COPY_CYAN: int
    COPY_GREEN: int
    COPY_MAGENTA: int
    COPY_RED: int
    COPY_YELLOW: int
    DARKEN: int
    DARKEN_INTENSITY: int
    DIFFERENCE: int
    DISPLACE: int
    DISSOLVE: int
    DISTORT: int
    DIVIDE_DST: int
    DIVIDE_SRC: int
    DST: int
    DST_ATOP: int
    DST_IN: int
    DST_OUT: int
    DST_OVER: int
    EXCLUSION: int
    HARD_LIGHT: int
    HARD_MIX: int
    HUE: int
    IN: int
    INTENSITY: int
    LIGHTEN: int
    LIGHTEN_INTENSITY: int
    LINEAR_BURN: int
    LINEAR_DODGE: int
    LINEAR_LIGHT: int
    LUMINIZE: int
    MATHEMATICS: int
    MINUS_DST: int
    MINUS_SRC: int
    MODULATE: int
    MODULUS_ADD: int
    MODULUS_SUBTRACT: int
    MULTIPLY: int
    NO: int
    OUT: int
    OVER: int
    OVERLAY: int
    PEGTOP_LIGHT: int
    PINLIGHT: int
    PLUS: int
    REPLACE: int
    SATURATE: int
    SCREEN: int
    SOFT_LIGHT: int
    SRC: int
    SRC_ATOP: int
    SRC_IN: int
    SRC_OUT: int
    SRC_OVER: int
    THRESHOLD: int
    UNDEFINED: int
    VIVID_LIGHT: int
    XOR: int

class Display:
    def image(self, *argv) -> Any: ...
    def reset_screen(self, *argv) -> Any: ...
    def scroll(self, *argv) -> Any: ...
    def text_grid(self, *argv) -> Any: ...
    def text_pixels(self, *argv) -> Any: ...

class FrameBuffer:
    def blit(self, *argv) -> Any: ...
    def fill(self, *argv) -> Any: ...
    def fill_rect(self, *argv) -> Any: ...
    def hline(self, *argv) -> Any: ...
    def line(self, *argv) -> Any: ...
    def pixel(self, *argv) -> Any: ...
    def rect(self, *argv) -> Any: ...
    def scroll(self, *argv) -> Any: ...
    def text(self, *argv) -> Any: ...
    def vline(self, *argv) -> Any: ...

class ImageFile: ...

MONO_HLSB: int

class MagickWand:
    def _raise_error(self, *argv) -> Any: ...
    def _set_image_depth(self, *argv) -> Any: ...
    def _set_image_format(self, *argv) -> Any: ...
    def _set_image_gravity(self, *argv) -> Any: ...
    def border_image(self, *argv) -> Any: ...
    def export_image_pixels(self, *argv) -> Any: ...
    def extent_image(self, *argv) -> Any: ...
    image_blob: Any
    image_depth: Any
    image_format: Any
    image_gravity: Any
    image_height: Any
    image_width: Any
    def read_image(self, *argv) -> Any: ...
    def write_image(self, *argv) -> Any: ...

class PixelWand:
    def _raise_error(self, *argv) -> Any: ...
    def _set_color(self, *argv) -> Any: ...
    def color(self, *argv) -> Any: ...

RGB565: int
UINT16: int
UINT32: int
UINT64: int
UINT8: int
XRGB8888: int
_FBIOGET_FSCREENINFO: int
_FBIOGET_VSCREENINFO: int
_FB_VISUAL_MONO01: int
_FB_VISUAL_MONO10: int
_FB_VISUAL_TRUECOLOR: int

class _Screen:
    BLACK: int
    WHITE: int
    bpp: Any
    def framebuffer(self, *argv) -> Any: ...
    height: Any
    def update(self, *argv) -> Any: ...
    width: Any

_fb_bitfield: Any
_fb_fix_screeninfo: Any
_fb_var_screeninfo: Any

def addressof() -> None: ...
def ioctl() -> None: ...

class mmap:
    def close(self, *argv) -> Any: ...
    def read(self, *argv) -> Any: ...
    def seek(self, *argv) -> Any: ...
    def write(self, *argv) -> Any: ...

def sizeof() -> None: ...

class struct: ...
