from typing import Any

class AlsaError(Exception): ...

EPIPE: int

class Mixer:
    _attach: Any
    _close: Any
    _find_selem: Any
    _load: Any
    _open: Any
    _selem_get_playback_volume_range: Any
    _selem_id_set_index: Any
    _selem_id_set_name: Any
    _selem_id_sizeof: Any
    _selem_register: Any
    _selem_set_playback_volume_all: Any
    def close(self, *argv) -> Any: ...
    def set_beep_volume(self, *argv) -> Any: ...
    def set_pcm_volume(self, *argv) -> Any: ...

class PCM:
    _ACCESS_RW_INTERLEAVED: int
    _FORMAT_S16_LE: int
    _STREAM_PLAYBACK: int
    _close: Any
    _drain: Any
    _drop: Any
    _hw_params: Any
    _hw_params_any: Any
    _hw_params_get_period_size: Any
    _hw_params_set_access: Any
    _hw_params_set_channels: Any
    _hw_params_set_format: Any
    _hw_params_set_rate: Any
    _hw_params_sizeof: Any
    _open: Any
    _prepare: Any
    _writei: Any
    def close(self, *argv) -> Any: ...
    def play(self, *argv) -> Any: ...

_alsa: Any

def _check_error() -> None: ...

_strerror: Any

def addressof() -> None: ...
def calcsize() -> None: ...

ffi: Any

def unpack() -> None: ...
