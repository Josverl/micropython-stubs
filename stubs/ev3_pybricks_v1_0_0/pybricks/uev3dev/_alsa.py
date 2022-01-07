"""
Module: 'pybricks.uev3dev._alsa' on LEGO EV3 v1.0.0
"""
# MCU: sysname=ev3, nodename=ev3, release=('v1.0.0',), version=('0.0.0',), machine=ev3
# Stubber: 1.3.2

class AlsaError:
    ''
EPIPE = 32

class Mixer:
    ''
    _attach = None
    _close = None
    _find_selem = None
    _load = None
    _open = None
    _selem_get_playback_volume_range = None
    _selem_id_set_index = None
    _selem_id_set_name = None
    _selem_id_sizeof = None
    _selem_register = None
    _selem_set_playback_volume_all = None
    def close():
        pass

    def set_beep_volume():
        pass

    def set_pcm_volume():
        pass


class PCM:
    ''
    _ACCESS_RW_INTERLEAVED = 3
    _FORMAT_S16_LE = 2
    _STREAM_PLAYBACK = 0
    _close = None
    _drain = None
    _drop = None
    _hw_params = None
    _hw_params_any = None
    _hw_params_get_period_size = None
    _hw_params_set_access = None
    _hw_params_set_channels = None
    _hw_params_set_format = None
    _hw_params_set_rate = None
    _hw_params_sizeof = None
    _open = None
    _prepare = None
    _writei = None
    def close():
        pass

    def play():
        pass

_alsa = None
def _check_error():
    pass

_strerror = None
def addressof():
    pass

def calcsize():
    pass

ffi = None
def unpack():
    pass

