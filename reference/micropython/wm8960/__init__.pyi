"""
A MicroPython driver for the WM8960 audio codec.
"""

from __future__ import annotations

from _typeshed import Incomplete

from micropython import const

WM8960_I2C_ADDR = const(0x1A)
"""Default I2C address"""

# Config symbol names
# Modules
MODULE_ADC = const(0)
"""ADC module in WM8960"""
MODULE_DAC = const(1)
"""DAC module in WM8960"""
MODULE_VREF = const(2)
"""VREF module"""
MODULE_HEADPHONE = const(3)
"""Headphone"""
MODULE_MIC_BIAS = const(4)
"""Mic bias"""
MODULE_MIC = const(5)
"""Input Mic"""
MODULE_LINE_IN = const(6)
"""Analog in PGA"""
MODULE_LINE_OUT = const(7)
"""Line out module"""
MODULE_SPEAKER = const(8)
"""Speaker module"""
MODULE_OMIX = const(9)
"""Output mixer"""
MODULE_MONO_OUT = const(10)
"""Mono mix"""

# Route
ROUTE_BYPASS = const(0)
"""LINEIN->Headphone."""
ROUTE_PLAYBACK = const(1)
""" I2SIN->DAC->Headphone."""
ROUTE_PLAYBACK_RECORD = const(2)
"""I2SIN->DAC->Headphone, LINEIN->ADC->I2SOUT."""
ROUTE_RECORD = const(5)
"""LINEIN->ADC->I2SOUT."""

# Input
INPUT_CLOSED = const(0)
"""Input device is closed"""
INPUT_MIC1 = const(1)
"""Input as single ended mic, only use L/RINPUT1"""
INPUT_MIC2 = const(2)
"""Input as diff. mic, use L/RINPUT1 and L/RINPUT2"""
INPUT_MIC3 = const(3)
"""Input as diff. mic, use L/RINPUT1 and L/RINPUT3"""
INPUT_LINE2 = const(4)
"""Input as line input, only use L/RINPUT2"""
INPUT_LINE3 = const(5)
"""Input as line input, only use L/RINPUT3"""

# ADC sync input
SYNC_ADC = const(0)
"""Use ADCLRC pin for ADC sync"""
SYNC_DAC = const(1)
"""used DACLRC pin for ADC sync"""

# Protocol type
BUS_I2S = const(2)
"""I2S type"""
BUS_LEFT_JUSTIFIED = const(1)
"""Left justified mode"""
BUS_RIGHT_JUSTIFIED = const(0)
"""Right justified mode"""
BUS_PCMA = const(3)
"""PCM A mode"""
BUS_PCMB = const(3 | (1 << 4))
"""PCM B mode"""

# Channel swap
SWAP_NONE = const(0)
SWAP_INPUT = const(1)
SWAP_OUTPUT = const(2)

# Mute settings
MUTE_FAST = const(0)
MUTE_SLOW = const(1)

# ALC settings
ALC_OFF = const(0)
ALC_RIGHT = const(1)
ALC_LEFT = const(2)
ALC_STEREO = const(3)
ALC_MODE = const(0)
"""ALC mode"""
ALC_LIMITER = const(1)
"""Limiter mode"""

# Clock Source
SYSCLK_MCLK = const(0)
"""sysclk source from external MCLK"""
SYSCLK_PLL = const(1)
"""sysclk source from internal PLL"""

class WM8960:
    """
    Create a WM8960 driver object, initialize the device with default settings and return the
    WM8960 object.

    Only the first two arguments are mandatory. All others are optional. The arguments are:

        - *i2c* is the I2C bus object.
        - *sample_rate* is the audio sample rate. Acceptable values are 8000,
          11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000, 96000, 192000
          and 384000.  Note that not every I2S hardware will support all values.
        - *bits* is the number of bits per audio word. Acceptable value are 16,
          20, 24, and 32.
        - *swap* swaps the left & right channel, if set; see below for options.
        - *route* Setting the audio path in the codec; see below for options.
        - *left_input* sets the audio source for the left input channel;
          see below for options.
        - *right_input* sets the audio source for the right input channel;
          see below for options.
        - *play_source* sets the audio target for the output audio;
          see below for options.
        - *sysclk_source* controls whether the internal master clock called
          "sysclk" is directly taken from the MCLK input or derived from it
          using an internal PLL. It is usually not required to change this.
        - *mclk_freq* sets the mclk frequency applied to the MCLK pin of the
          codec. If not set, default values are used.
        - *primary* lets the WM8960 act as primary or secondary device. The
          default setting is ``False``.  When set to ``False``,
          *sample_rate* and *bits* are controlled by the MCU.
        - *adc_sync* sets which input is used for the ADC sync signal.
          The default is using the DACLRC pin.
        - *protocol* sets the communication protocol. The default is I2S.
          See below for all options.
        - *i2c_address* sets the I2C address of the WM8960, with default ``0x1A``.

    If *mclk_freq* is not set the following default values are used:

        - sysclk_source == SYSCLK_PLL: 11.2896 MHz for sample rates of 44100,
          22050 and 11015 Hz, and 12.288 Mhz for sample rates < 48000, otherwise
          sample_rate * 256.
        - sysclk_source == SYSCLK_MCLK: sample_rate * 256.

    If the MCLK signal is applied using, for example,. a separate oscillator,
    it must be specified for proper operation.
    """

    def __init__(
        self,
        i2c,
        sample_rate,
        *,
        bits=16,
        swap=SWAP_NONE,
        route=ROUTE_PLAYBACK_RECORD,
        left_input=INPUT_MIC3,
        right_input=INPUT_MIC2,
        sysclk_source=SYSCLK_MCLK,
        mclk_freq=None,
        primary=False,
        adc_sync=SYNC_DAC,
        protocol=BUS_I2S,
        i2c_address=WM8960_I2C_ADDR,
    ) -> None: ...
    def set_left_input(self, input_source) -> None:
        """
        Specify the source for the left input.  The input source names are listed above.
        """
        ...

    def set_right_input(self, input_source) -> None:
        """
        Specify the source for the right input.  The input source names are listed above.
        """
        ...

    def volume(self, module, volume_l=None, volume_r=None) -> None:
        """
        Sets or gets the volume of a certain module.

        If no volume values are supplied, the actual volume tuple is returned.

        If one or two values are supplied, it sets the volume of a certain module.
        If two values are provided, the first one is used for the left channel,
        the second for the right channel.  If only one value is supplied, it is used
        for both channels.  The value range is normalized to 0.0-100.0 with a
        logarithmic scale.

        For a list of suitable modules and db/step, see the table below.
        """
        ...

    def mute(self, module, mute, soft=True, ramp=MUTE_FAST) -> None:
        """
        Mute or unmute the output. If *mute* is True, the output is muted, if ``False``
        it is unmuted.

        If *soft* is set as True, muting will happen as a soft transition.  The time for
        the transition is defined by *ramp*, which is either ``MUTE_FAST`` or ``MUTE_SLOW``.
        """
        ...

    def set_data_route(self, route) -> None:
        """
        Set the audio data route.  For the parameter value/names, see the table above.
        """
        ...

    def set_module(self, module, active) -> None:
        """
        Enable or disable a module, with *active* being ``False`` or ``True``.  For
        the list of module names, see the table above.

        Note that enabling ``MODULE_MONO_OUT`` is different from the `WM8960.mono`
        method.  The first enables output 3, while the `WM8960.mono` method sends a
        mono mix to the left and right output.
        """
        ...

    def enable_module(self, module) -> None:
        """
        Enable a module.  For the list of module names, see the table above.
        """
        ...

    def disable_module(self, module) -> None:
        """
        Disable a module.  For the list of module names, see the table above.
        """
        ...

    def expand_3d(self, level) -> None:
        """
        Enable Stereo 3D expansion.  *level* is a number between 0 and 15.
        A value of 0 disables the expansion.
        """
        ...

    def mono(self, active) -> None:
        """
        If *active* is ``True``, a Mono mix is sent to the left and right output
        channel.  This is different from enabling the ``MODULE_MONO_MIX``, which
        enables output 3.
        """
        ...

    def alc_mode(self, channel, mode: int = ALC_MODE) -> None:
        """
        Enables or disables ALC mode.  Parameters are:

        - *channel* enables and sets the channel for ALC. The parameter values are:

            - ALC_OFF:   Switch ALC off
            - ALS_RIGHT:  Use the right input channel
            - ALC_LEFT:   Use the left input channel
            - ALC_STEREO: Use both input channels.

        - *mode* sets the ALC mode. Input values are:

            - ALC_MODE:   act as ALC
            - ALC_LIMITER: act as limiter.
        """
        ...

    def alc_gain(self, target=-12, max_gain=30, min_gain=-17.25, noise_gate=-78) -> None:
        """
        Set the target level, highest and lowest gain levels and the noise gate as dB level.
        Permitted ranges are:

        - *target*: -22.5 to -1.5 dB
        - *max_gain*: -12 to 30 dB
        - *min_gain*: -17 to 25 dB
        - *noise_gate*: -78 to -30 dB

        Excess values are limited to the permitted ranges.  A value of -78 or less
        for *noise_gate* disables the noise gate function.
        """
        ...

    def alc_time(self, attack=24, decay=192, hold=0) -> None:
        """
        Set the dynamic characteristic of ALC.  The times are given as millisecond
        values.  Permitted ranges are:

        - *attack*: 6 to 6140
        - *decay*: 24 to 24580
        - *hold*: 0 to 43000

        Excess values are limited within the permitted ranges.
        """
        ...

    def deemphasis(self, active) -> None:
        """
        Enables or disables a deemphasis filter for playback, with *active* being
        ``False`` or ``True``.  This filter is applied only for sample rates of
        32000, 44100 and 48000.  For other sample rates, the filter setting
        is silently ignored.
        """
        ...

    def deinit(self) -> None:
        """
        Disable all modules.
        """
        ...

    def set_internal_pll_config(self, input_mclk, output_clk):
        """ """
        ...

    def set_master_clock(self, sysclk, sample_rate, bit_width):
        """ """
        ...

    def set_speaker_clock(self, sysclk):
        """ """
        ...
