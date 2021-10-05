"""
Module: 'lodepng' on lvgl-8_1_0_dev-esp32
"""
# MCU: {'ver': '1.17-564', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.17.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.17.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '564', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.4.0.beta
from typing import Any


class C_Pointer:
    ''

class LCT:
    ''
    GREY = 0 # type: int
    GREY_ALPHA = 4 # type: int
    MAX_OCTET_VALUE = 255 # type: int
    PALETTE = 3 # type: int
    RGB = 2 # type: int
    RGBA = 6 # type: int

class LodePNGColorMode:
    ''

class LodePNGDecoderSettings:
    ''

class LodePNGDecompressSettings:
    ''

class LodePNGInfo:
    ''

class LodePNGState:
    ''

class LodePNGTime:
    ''
def add_itext(self, *args) -> Any:
    ...

def add_text(self, *args) -> Any:
    ...

def can_have_alpha(self, *args) -> Any:
    ...

def chunk_ancillary(self, *args) -> Any:
    ...

def chunk_append(self, *args) -> Any:
    ...

def chunk_check_crc(self, *args) -> Any:
    ...

def chunk_create(self, *args) -> Any:
    ...

def chunk_data(self, *args) -> Any:
    ...

def chunk_data_const(self, *args) -> Any:
    ...

def chunk_find(self, *args) -> Any:
    ...

def chunk_find_const(self, *args) -> Any:
    ...

def chunk_generate_crc(self, *args) -> Any:
    ...

def chunk_length(self, *args) -> Any:
    ...

def chunk_next(self, *args) -> Any:
    ...

def chunk_next_const(self, *args) -> Any:
    ...

def chunk_private(self, *args) -> Any:
    ...

def chunk_safetocopy(self, *args) -> Any:
    ...

def chunk_type(self, *args) -> Any:
    ...

def chunk_type_equals(self, *args) -> Any:
    ...

def clear_icc(self, *args) -> Any:
    ...

def clear_itext(self, *args) -> Any:
    ...

def clear_text(self, *args) -> Any:
    ...

def color_mode_cleanup(self, *args) -> Any:
    ...

def color_mode_copy(self, *args) -> Any:
    ...

def color_mode_init(self, *args) -> Any:
    ...

def color_mode_make(self, *args) -> Any:
    ...

def convert(self, *args) -> Any:
    ...

def crc32(self, *args) -> Any:
    ...

def decode(self, *args) -> Any:
    ...

def decode24(self, *args) -> Any:
    ...

def decode32(self, *args) -> Any:
    ...

def decode_memory(self, *args) -> Any:
    ...

def decoder_settings_init(self, *args) -> Any:
    ...

def decompress_settings_init(self, *args) -> Any:
    ...

default_decompress_settings: Any
def error_text(self, *args) -> Any:
    ...

def get_bpp(self, *args) -> Any:
    ...

def get_channels(self, *args) -> Any:
    ...

def get_raw_size(self, *args) -> Any:
    ...

def has_palette_alpha(self, *args) -> Any:
    ...

def inflate(self, *args) -> Any:
    ...

def info_cleanup(self, *args) -> Any:
    ...

def info_copy(self, *args) -> Any:
    ...

def info_init(self, *args) -> Any:
    ...

def inspect(self, *args) -> Any:
    ...

def inspect_chunk(self, *args) -> Any:
    ...

def is_alpha_type(self, *args) -> Any:
    ...

def is_greyscale_type(self, *args) -> Any:
    ...

def is_palette_type(self, *args) -> Any:
    ...

def palette_add(self, *args) -> Any:
    ...

def palette_clear(self, *args) -> Any:
    ...

def set_icc(self, *args) -> Any:
    ...

def state_cleanup(self, *args) -> Any:
    ...

def state_copy(self, *args) -> Any:
    ...

def state_init(self, *args) -> Any:
    ...

def zlib_decompress(self, *args) -> Any:
    ...

