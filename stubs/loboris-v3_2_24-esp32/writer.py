"""
Module: 'writer' on esp32_LoBo
MCU: (sysname='esp32_LoBo', nodename='esp32_LoBo', release='3.2.24', version='ESP32_LoBo_v3.2.24 on 2018-09-06', machine='ESP32 board with ESP32')
Stubber: 1.0.0 - updated
"""
from typing import Any


class Writer:
    """"""

    def _newline(self, *args) -> Any:
        pass

    def _printchar(self, *args) -> Any:
        pass

    def _printchar_bitwise(self, *args) -> Any:
        pass

    col_clip = None

    def printstring(self, *args) -> Any:
        pass

    row_clip = None

    def set_clip(self, *args) -> Any:
        pass

    def set_textpos(self, *args) -> Any:
        pass

    text_col = 0
    text_row = 0


framebuf = None
