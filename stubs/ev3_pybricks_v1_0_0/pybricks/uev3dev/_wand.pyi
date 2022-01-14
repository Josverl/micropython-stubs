from typing import Any

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

class Gravity:
    CENTER: int
    EAST: int
    FORGET: int
    NORTH: int
    NORTH_EAST: int
    NORTH_WEST: int
    SOUTH: int
    SOUTH_EAST: int
    SOUTH_WEST: int
    UNDEFINED: int
    WEST: int

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

class MagickWandError(Exception): ...
class PixelError(Exception): ...

class PixelWand:
    def _raise_error(self, *argv) -> Any: ...
    def _set_color(self, *argv) -> Any: ...
    def color(self, *argv) -> Any: ...

class StorageType:
    CHAR: int
    DOUBLE: int
    FLOAT: int
    LONG: int
    LONG_LONG: int
    QUANTUM: int
    SHORT: int
    UNDEFINED: int

_border_image: Any
_clear_exception: Any
_destroy: Any
_destroy_pixel_wand: Any
_export_image_pixels: Any
_extent_image: Any
_genisis: Any
_get_exception: Any
_get_image_blob: Any
_get_image_depth: Any
_get_image_format: Any
_get_image_gravity: Any
_get_image_height: Any
_get_image_width: Any
_new: Any
_new_pixel_wand: Any
_pixel_clear_exception: Any
_pixel_get_color: Any
_pixel_get_exception: Any
_pixel_set_color: Any
_read_image: Any
_relinquish_memory: Any
_reset_iterator: Any
_set_image_depth: Any
_set_image_format: Any
_set_image_gravity: Any
_terminus: Any
_wand: Any
_write_image: Any

def bytearray_at() -> None: ...
def calcsize() -> None: ...

ffilib: Any

def unpack() -> None: ...
