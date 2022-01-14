"""
Module: 'pybricks.uev3dev.display' on LEGO EV3 v1.0.0
"""
# MCU: sysname=ev3, nodename=ev3, release=('v1.0.0',), version=('0.0.0',), machine=ev3
# Stubber: 1.3.2 - updated
from typing import Any

ARRAY = -1073741824


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


class Display:
    """"""

    def image(self, *argv) -> Any:
        pass

    def reset_screen(self, *argv) -> Any:
        pass

    def scroll(self, *argv) -> Any:
        pass

    def text_grid(self, *argv) -> Any:
        pass

    def text_pixels(self, *argv) -> Any:
        pass


class FrameBuffer:
    """"""

    def blit(self, *argv) -> Any:
        pass

    def fill(self, *argv) -> Any:
        pass

    def fill_rect(self, *argv) -> Any:
        pass

    def hline(self, *argv) -> Any:
        pass

    def line(self, *argv) -> Any:
        pass

    def pixel(self, *argv) -> Any:
        pass

    def rect(self, *argv) -> Any:
        pass

    def scroll(self, *argv) -> Any:
        pass

    def text(self, *argv) -> Any:
        pass

    def vline(self, *argv) -> Any:
        pass


class ImageFile:
    """"""


MONO_HLSB = 3


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


class PixelWand:
    """"""

    def _raise_error(self, *argv) -> Any:
        pass

    def _set_color(self, *argv) -> Any:
        pass

    def color(self, *argv) -> Any:
        pass


RGB565 = 1
UINT16 = 268435456
UINT32 = 536870912
UINT64 = 805306368
UINT8 = 0
XRGB8888 = 7
_FBIOGET_FSCREENINFO = 17922
_FBIOGET_VSCREENINFO = 17920
_FB_VISUAL_MONO01 = 0
_FB_VISUAL_MONO10 = 1
_FB_VISUAL_TRUECOLOR = 2


class _Screen:
    """"""

    BLACK = 0
    WHITE = -1
    bpp = None

    def framebuffer(self, *argv) -> Any:
        pass

    height = None

    def update(self, *argv) -> Any:
        pass

    width = None


_fb_bitfield = None
_fb_fix_screeninfo = None
_fb_var_screeninfo = None


def addressof():
    pass


def ioctl():
    pass


class mmap:
    """"""

    def close(self, *argv) -> Any:
        pass

    def read(self, *argv) -> Any:
        pass

    def seek(self, *argv) -> Any:
        pass

    def write(self, *argv) -> Any:
        pass


def sizeof():
    pass


class struct:
    """"""
