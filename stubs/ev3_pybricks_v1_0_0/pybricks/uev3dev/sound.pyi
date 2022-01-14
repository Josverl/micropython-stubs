from typing import Any

INT32: int

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

class PlayType:
    ONCE: int
    REPEAT: int
    WAIT: int

class Sound:
    def _beep(self, *argv) -> Any: ...
    def _play_tone(self, *argv) -> Any: ...
    def _stop(self, *argv) -> Any: ...
    def play_file(self, *argv) -> Any: ...
    def play_note(self, *argv) -> Any: ...
    def play_tone(self, *argv) -> Any: ...
    def stop(self, *argv) -> Any: ...

class SoundFile:
    def _cancel_token(self, *argv) -> Any: ...
    _read: Any
    def close(self, *argv) -> Any: ...

class SoundFileError(Exception): ...

class Timeout:
    _ONE: Any
    def _run(self, *argv) -> Any: ...
    def cancel(self, *argv) -> Any: ...
    def close(self, *argv) -> Any: ...
    def start(self, *argv) -> Any: ...
    def wait(self, *argv) -> Any: ...

UINT16: int
UINT32: int
UINT64: int
_BEEP_DEV: str

class _CancelToken:
    def cancel(self, *argv) -> Any: ...

_EV_SND: int
_NOTES: Any
_SEEK_SET: int
_SF_INFO: Any
_SMF_READ: int
_SND_TONE: int
_input_event: Any
_libsndfile: Any
_sf_close: Any
_sf_count_t: int
_sf_open: Any
_sf_readf_short: Any
_sf_seek: Any
_sf_strerror: Any
_thread: Any

def addressof() -> None: ...
def calcsize() -> None: ...
def debug_print() -> None: ...

ffilib: Any
os: Any

def pack() -> None: ...
def sizeof() -> None: ...
def sleep() -> None: ...
def sleep_ms() -> None: ...

class struct: ...

def unpack() -> None: ...
