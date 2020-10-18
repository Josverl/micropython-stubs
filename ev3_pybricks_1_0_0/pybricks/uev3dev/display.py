"""
Module: 'pybricks.uev3dev.display' on LEGO EV3 v1.0.0
"""
# MCU: sysname=ev3, nodename=ev3, release=('v1.0.0',), version=('0.0.0',), machine=ev3
# Stubber: 1.3.2
ARRAY = -1073741824

class CompositeOp:
    ''
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
    ''
    def image():
        pass

    def reset_screen():
        pass

    def scroll():
        pass

    def text_grid():
        pass

    def text_pixels():
        pass


class FrameBuffer:
    ''
    def blit():
        pass

    def fill():
        pass

    def fill_rect():
        pass

    def hline():
        pass

    def line():
        pass

    def pixel():
        pass

    def rect():
        pass

    def scroll():
        pass

    def text():
        pass

    def vline():
        pass


class ImageFile:
    ''
MONO_HLSB = 3

class MagickWand:
    ''
    def _raise_error():
        pass

    def _set_image_depth():
        pass

    def _set_image_format():
        pass

    def _set_image_gravity():
        pass

    def border_image():
        pass

    def export_image_pixels():
        pass

    def extent_image():
        pass

    image_blob = None
    image_depth = None
    image_format = None
    image_gravity = None
    image_height = None
    image_width = None
    def read_image():
        pass

    def write_image():
        pass


class PixelWand:
    ''
    def _raise_error():
        pass

    def _set_color():
        pass

    def color():
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
    ''
    BLACK = 0
    WHITE = -1
    bpp = None
    def framebuffer():
        pass

    height = None
    def update():
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
    ''
    def close():
        pass

    def read():
        pass

    def seek():
        pass

    def write():
        pass

def sizeof():
    pass


class struct:
    ''
