"""
Module: 'pybricks.uev3dev._wand' on LEGO EV3 v1.0.0
"""
# MCU: sysname=ev3, nodename=ev3, release=('v1.0.0',), version=('0.0.0',), machine=ev3
# Stubber: 1.3.2 - updated
from typing import Any


class CompositeOp:
    """"""

    ALPHA = 1
    ATOP = 2
    BLEND = 3
    BLUR = 4
    BUMPMAP = 5
    CHANGE_MASK = 6
    CLEAR = 7
    COLORIZE = 10
    COLOR_BURN = 8
    COLOR_DODGE = 9
    COPY = 14
    COPY_ALPHA = 18
    COPY_BLACK = 11
    COPY_BLUE = 12
    COPY_CYAN = 15
    COPY_GREEN = 16
    COPY_MAGENTA = 17
    COPY_RED = 18
    COPY_YELLOW = 19
    DARKEN = 20
    DARKEN_INTENSITY = 21
    DIFFERENCE = 22
    DISPLACE = 23
    DISSOLVE = 24
    DISTORT = 25
    DIVIDE_DST = 26
    DIVIDE_SRC = 27
    DST = 29
    DST_ATOP = 28
    DST_IN = 30
    DST_OUT = 31
    DST_OVER = 32
    EXCLUSION = 33
    HARD_LIGHT = 34
    HARD_MIX = 35
    HUE = 36
    IN = 37
    INTENSITY = 38
    LIGHTEN = 39
    LIGHTEN_INTENSITY = 40
    LINEAR_BURN = 41
    LINEAR_DODGE = 42
    LINEAR_LIGHT = 43
    LUMINIZE = 44
    MATHEMATICS = 45
    MINUS_DST = 46
    MINUS_SRC = 47
    MODULATE = 48
    MODULUS_ADD = 49
    MODULUS_SUBTRACT = 50
    MULTIPLY = 51
    NO = 52
    OUT = 53
    OVER = 54
    OVERLAY = 55
    PEGTOP_LIGHT = 56
    PINLIGHT = 57
    PLUS = 58
    REPLACE = 59
    SATURATE = 60
    SCREEN = 61
    SOFT_LIGHT = 62
    SRC = 64
    SRC_ATOP = 63
    SRC_IN = 65
    SRC_OUT = 66
    SRC_OVER = 67
    THRESHOLD = 68
    UNDEFINED = 0
    VIVID_LIGHT = 69
    XOR = 70


class Gravity:
    """"""

    CENTER = 6
    EAST = 7
    FORGET = 1
    NORTH = 3
    NORTH_EAST = 4
    NORTH_WEST = 2
    SOUTH = 9
    SOUTH_EAST = 10
    SOUTH_WEST = 8
    UNDEFINED = 0
    WEST = 5


class MagickWand:
    """"""

    def _raise_error(self, *argv) -> Any:
        pass

    def _set_image_depth(self, *argv) -> Any:
        pass

    def _set_image_format(self, *argv) -> Any:
        pass

    def _set_image_gravity(self, *argv) -> Any:
        pass

    def border_image(self, *argv) -> Any:
        pass

    def export_image_pixels(self, *argv) -> Any:
        pass

    def extent_image(self, *argv) -> Any:
        pass

    image_blob = None
    image_depth = None
    image_format = None
    image_gravity = None
    image_height = None
    image_width = None

    def read_image(self, *argv) -> Any:
        pass

    def write_image(self, *argv) -> Any:
        pass


class MagickWandError(Exception):
    """"""


class PixelError(Exception):
    """"""


class PixelWand:
    """"""

    def _raise_error(self, *argv) -> Any:
        pass

    def _set_color(self, *argv) -> Any:
        pass

    def color(self, *argv) -> Any:
        pass


class StorageType:
    """"""

    CHAR = 1
    DOUBLE = 2
    FLOAT = 3
    LONG = 4
    LONG_LONG = 5
    QUANTUM = 6
    SHORT = 7
    UNDEFINED = 0


_border_image = None
_clear_exception = None
_destroy = None
_destroy_pixel_wand = None
_export_image_pixels = None
_extent_image = None
_genisis = None
_get_exception = None
_get_image_blob = None
_get_image_depth = None
_get_image_format = None
_get_image_gravity = None
_get_image_height = None
_get_image_width = None
_new = None
_new_pixel_wand = None
_pixel_clear_exception = None
_pixel_get_color = None
_pixel_get_exception = None
_pixel_set_color = None
_read_image = None
_relinquish_memory = None
_reset_iterator = None
_set_image_depth = None
_set_image_format = None
_set_image_gravity = None
_terminus = None
_wand = None
_write_image = None


def bytearray_at():
    pass


def calcsize():
    pass


ffilib = None


def unpack():
    pass
