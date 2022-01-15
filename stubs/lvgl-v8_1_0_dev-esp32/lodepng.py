"""
Module: 'lodepng' on lvgl-8_1_0-dev-esp32
"""
# MCU: {'ver': '1.17-564', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.17.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.17.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '564', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.4.2
from typing import Any


class C_Pointer:
    """"""


class LCT:
    """"""

    GREY = 0  # type: int
    GREY_ALPHA = 4  # type: int
    MAX_OCTET_VALUE = 255  # type: int
    PALETTE = 3  # type: int
    RGB = 2  # type: int
    RGBA = 6  # type: int


class LodePNGColorMode:
    """"""


class LodePNGDecoderSettings:
    """"""


class LodePNGDecompressSettings:
    """"""


class LodePNGInfo:
    """"""


class LodePNGState:
    """"""


class LodePNGTime:
    """"""


def add_itext(*args) -> Any:
    ...


def add_text(*args) -> Any:
    ...


def can_have_alpha(*args) -> Any:
    ...


def chunk_ancillary(*args) -> Any:
    ...


def chunk_append(*args) -> Any:
    ...


def chunk_check_crc(*args) -> Any:
    ...


def chunk_create(*args) -> Any:
    ...


def chunk_data(*args) -> Any:
    ...


def chunk_data_const(*args) -> Any:
    ...


def chunk_find(*args) -> Any:
    ...


def chunk_find_const(*args) -> Any:
    ...


def chunk_generate_crc(*args) -> Any:
    ...


def chunk_length(*args) -> Any:
    ...


def chunk_next(*args) -> Any:
    ...


def chunk_next_const(*args) -> Any:
    ...


def chunk_private(*args) -> Any:
    ...


def chunk_safetocopy(*args) -> Any:
    ...


def chunk_type(*args) -> Any:
    ...


def chunk_type_equals(*args) -> Any:
    ...


def clear_icc(*args) -> Any:
    ...


def clear_itext(*args) -> Any:
    ...


def clear_text(*args) -> Any:
    ...


def color_mode_cleanup(*args) -> Any:
    ...


def color_mode_copy(*args) -> Any:
    ...


def color_mode_init(*args) -> Any:
    ...


def color_mode_make(*args) -> Any:
    ...


def convert(*args) -> Any:
    ...


def crc32(*args) -> Any:
    ...


def decode(*args) -> Any:
    ...


def decode24(*args) -> Any:
    ...


def decode32(*args) -> Any:
    ...


def decode_memory(*args) -> Any:
    ...


def decoder_settings_init(*args) -> Any:
    ...


def decompress_settings_init(*args) -> Any:
    ...


default_decompress_settings: Any  ## <class 'LodePNGDecompressSettings'> = struct LodePNGDecompressSettings


def error_text(*args) -> Any:
    ...


def get_bpp(*args) -> Any:
    ...


def get_channels(*args) -> Any:
    ...


def get_raw_size(*args) -> Any:
    ...


def has_palette_alpha(*args) -> Any:
    ...


def inflate(*args) -> Any:
    ...


def info_cleanup(*args) -> Any:
    ...


def info_copy(*args) -> Any:
    ...


def info_init(*args) -> Any:
    ...


def inspect(*args) -> Any:
    ...


def inspect_chunk(*args) -> Any:
    ...


def is_alpha_type(*args) -> Any:
    ...


def is_greyscale_type(*args) -> Any:
    ...


def is_palette_type(*args) -> Any:
    ...


def palette_add(*args) -> Any:
    ...


def palette_clear(*args) -> Any:
    ...


def set_icc(*args) -> Any:
    ...


def state_cleanup(*args) -> Any:
    ...


def state_copy(*args) -> Any:
    ...


def state_init(*args) -> Any:
    ...


def zlib_decompress(*args) -> Any:
    ...
