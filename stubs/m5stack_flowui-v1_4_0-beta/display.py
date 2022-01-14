"""
Module: 'display' on M5 FlowUI v1.4.0-beta
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-284-g5d8e1c867 on 2019-08-30', machine='ESP32 module with ESP32')
# Stubber: 1.3.1 - updated
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
    FONT_DejaVu40 = 11
    FONT_DejaVu56 = 12
    FONT_DejaVu72 = 13
    FONT_Minya = 5
    FONT_Small = 7
    FONT_Tooney = 6
    FONT_Ubuntu = 3
    GREEN = 65280
    GREENYELLOW = 11336748
    HSPI = 1
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
    VSPI = 2
    WHITE = 16579836
    YELLOW = 16579584

    def arc(self, *argv) -> Any:
        pass

    def attrib7seg(self, *argv) -> Any:
        pass

    def backlight(self, *argv) -> Any:
        pass

    def circle(self, *argv) -> Any:
        pass

    def clear(self, *argv) -> Any:
        pass

    def clearwin(self, *argv) -> Any:
        pass

    def compileFont(self, *argv) -> Any:
        pass

    def deinit(self, *argv) -> Any:
        pass

    def drawCircle(self, *argv) -> Any:
        pass

    def drawLine(self, *argv) -> Any:
        pass

    def drawPixel(self, *argv) -> Any:
        pass

    def drawRect(self, *argv) -> Any:
        pass

    def drawRoundRect(self, *argv) -> Any:
        pass

    def drawTriangle(self, *argv) -> Any:
        pass

    def ellipse(self, *argv) -> Any:
        pass

    def fill(self, *argv) -> Any:
        pass

    def fillCircle(self, *argv) -> Any:
        pass

    def fillRect(self, *argv) -> Any:
        pass

    def fillRoundRect(self, *argv) -> Any:
        pass

    def fillScreen(self, *argv) -> Any:
        pass

    def fillTriangle(self, *argv) -> Any:
        pass

    def font(self, *argv) -> Any:
        pass

    def fontSize(self, *argv) -> Any:
        pass

    def getCursor(self, *argv) -> Any:
        pass

    def get_bg(self, *argv) -> Any:
        pass

    def get_fg(self, *argv) -> Any:
        pass

    def hsb2rgb(self, *argv) -> Any:
        pass

    def image(self, *argv) -> Any:
        pass

    def init(self, *argv) -> Any:
        pass

    def line(self, *argv) -> Any:
        pass

    def lineByAngle(self, *argv) -> Any:
        pass

    def orient(self, *argv) -> Any:
        pass

    def pixel(self, *argv) -> Any:
        pass

    def polygon(self, *argv) -> Any:
        pass

    def print(self, *argv) -> Any:
        pass

    def println(self, *argv) -> Any:
        pass

    def qrcode(self, *argv) -> Any:
        pass

    def rect(self, *argv) -> Any:
        pass

    def resetwin(self, *argv) -> Any:
        pass

    def restorewin(self, *argv) -> Any:
        pass

    def roundrect(self, *argv) -> Any:
        pass

    def savewin(self, *argv) -> Any:
        pass

    def screensize(self, *argv) -> Any:
        pass

    def setBrightness(self, *argv) -> Any:
        pass

    def setColor(self, *argv) -> Any:
        pass

    def setCursor(self, *argv) -> Any:
        pass

    def setRotation(self, *argv) -> Any:
        pass

    def setTextColor(self, *argv) -> Any:
        pass

    def set_bg(self, *argv) -> Any:
        pass

    def set_fg(self, *argv) -> Any:
        pass

    def setwin(self, *argv) -> Any:
        pass

    def text(self, *argv) -> Any:
        pass

    def textClear(self, *argv) -> Any:
        pass

    def textWidth(self, *argv) -> Any:
        pass

    def text_x(self, *argv) -> Any:
        pass

    def text_y(self, *argv) -> Any:
        pass

    def tft_deselect(self, *argv) -> Any:
        pass

    def tft_readcmd(self, *argv) -> Any:
        pass

    def tft_select(self, *argv) -> Any:
        pass

    def tft_setspeed(self, *argv) -> Any:
        pass

    def tft_writecmd(self, *argv) -> Any:
        pass

    def tft_writecmddata(self, *argv) -> Any:
        pass

    def triangle(self, *argv) -> Any:
        pass

    def winsize(self, *argv) -> Any:
        pass
