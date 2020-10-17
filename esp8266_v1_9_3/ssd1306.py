"""
Module: 'ssd1306' on esp8266 v1.9.3
"""
# MCU: (sysname='esp8266', nodename='esp8266', release='2.0.0(5a875ba)', version='v1.9.3-8-g63826ac5c on 2017-11-01', machine='ESP module with ESP8266')
# Stubber: 1.1.2
SET_CHARGE_PUMP = 141
SET_COL_ADDR = 33
SET_COM_OUT_DIR = 192
SET_COM_PIN_CFG = 218
SET_CONTRAST = 129
SET_DISP = 174
SET_DISP_CLK_DIV = 213
SET_DISP_OFFSET = 211
SET_DISP_START_LINE = 64
SET_ENTIRE_ON = 164
SET_MEM_ADDR = 32
SET_MUX_RATIO = 168
SET_NORM_INV = 166
SET_PAGE_ADDR = 34
SET_PRECHARGE = 217
SET_SEG_REMAP = 160
SET_VCOM_DESEL = 219

class SSD1306:
    ''
    def contrast():
        pass

    def init_display():
        pass

    def invert():
        pass

    def poweroff():
        pass

    def poweron():
        pass

    def show():
        pass


class SSD1306_I2C:
    ''
    def write_cmd():
        pass

    def write_data():
        pass


class SSD1306_SPI:
    ''
    def write_cmd():
        pass

    def write_data():
        pass

def const():
    pass

framebuf = None
