"""
Module: 'display' on esp32_LoBo
MCU: (sysname='esp32_LoBo', nodename='esp32_LoBo', release='3.2.24', version='ESP32_LoBo_v3.2.24 on 2018-09-06', machine='ESP32 board with ESP32')
Stubber: 1.0.0 - updated
"""
from typing import Any


class TFT:
    """"""

    BLACK = 0
    BLUE = 255
    BMP = 2
    BOTTOM = -9004
    CENTER = -9003
    COLOR_BITS16 = 16
    COLOR_BITS24 = 24
    CYAN = 65535
    DARKCYAN = 32896
    DARKGREEN = 32768
    DARKGREY = 8421504
    FONT_7seg = 9
    FONT_Comic = 4
    FONT_Default = 0
    FONT_DefaultSmall = 8
    FONT_DejaVu18 = 1
    FONT_DejaVu24 = 2
    FONT_Minya = 5
    FONT_Small = 7
    FONT_Tooney = 6
    FONT_Ubuntu = 3
    GENERIC = 7
    GREEN = 65280
    GREENYELLOW = 11336748
    HSPI = 1
    ILI9341 = 0
    ILI9488 = 1
    JPG = 1
    LANDSCAPE = 1
    LANDSCAPE_FLIP = 3
    LASTX = 7000
    LASTY = 8000
    LIGHTGREY = 12632256
    M5STACK = 6
    MAGENTA = 16515327
    MAROON = 8388608
    NAVY = 128
    OLIVE = 8421376
    ORANGE = 16557056
    PINK = 16564426
    PORTRAIT = 0
    PORTRAIT_FLIP = 2
    PURPLE = 8388736
    RED = 16515072
    RIGHT = -9004
    ST7735 = 3
    ST7735B = 5
    ST7735R = 4
    ST7789 = 2
    TOUCH_NONE = 0
    TOUCH_STMPE = 2
    TOUCH_XPT = 1
    VSPI = 2
    WHITE = 16579836
    YELLOW = 16579584

    def arc(self, *args) -> Any:
        pass

    def attrib7seg(self, *args) -> Any:
        pass

    def backlight(self, *args) -> Any:
        pass

    def circle(self, *args) -> Any:
        pass

    def clear(self, *args) -> Any:
        pass

    def clearwin(self, *args) -> Any:
        pass

    def compileFont(self, *args) -> Any:
        pass

    def deinit(self, *args) -> Any:
        pass

    def ellipse(self, *args) -> Any:
        pass

    def font(self, *args) -> Any:
        pass

    def fontSize(self, *args) -> Any:
        pass

    def getCalib(self, *args) -> Any:
        pass

    def getTouchType(self, *args) -> Any:
        pass

    def get_bg(self, *args) -> Any:
        pass

    def get_fg(self, *args) -> Any:
        pass

    def gettouch(self, *args) -> Any:
        pass

    def hsb2rgb(self, *args) -> Any:
        pass

    def image(self, *args) -> Any:
        pass

    def init(self, *args) -> Any:
        pass

    def line(self, *args) -> Any:
        pass

    def lineByAngle(self, *args) -> Any:
        pass

    def orient(self, *args) -> Any:
        pass

    def pixel(self, *args) -> Any:
        pass

    def polygon(self, *args) -> Any:
        pass

    def readPixel(self, *args) -> Any:
        pass

    def readScreen(self, *args) -> Any:
        pass

    def rect(self, *args) -> Any:
        pass

    def resetwin(self, *args) -> Any:
        pass

    def restorewin(self, *args) -> Any:
        pass

    def roundrect(self, *args) -> Any:
        pass

    def savewin(self, *args) -> Any:
        pass

    def screensize(self, *args) -> Any:
        pass

    def setCalib(self, *args) -> Any:
        pass

    def set_bg(self, *args) -> Any:
        pass

    def set_fg(self, *args) -> Any:
        pass

    def setwin(self, *args) -> Any:
        pass

    def text(self, *args) -> Any:
        pass

    def textClear(self, *args) -> Any:
        pass

    def textWidth(self, *args) -> Any:
        pass

    def text_x(self, *args) -> Any:
        pass

    def text_y(self, *args) -> Any:
        pass

    def tft_deselect(self, *args) -> Any:
        pass

    def tft_readcmd(self, *args) -> Any:
        pass

    def tft_select(self, *args) -> Any:
        pass

    def tft_setspeed(self, *args) -> Any:
        pass

    def tft_writecmd(self, *args) -> Any:
        pass

    def tft_writecmddata(self, *args) -> Any:
        pass

    def triangle(self, *args) -> Any:
        pass

    def winsize(self, *args) -> Any:
        pass
