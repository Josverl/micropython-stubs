"""
Module: 'flowlib.lib.wavplayer' on M5 FlowUI v1.4.0-beta
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-284-g5d8e1c867 on 2019-08-30', machine='ESP32 module with ESP32')
# Stubber: 1.3.1 - updated
from typing import Any


class Btn:
    """"""

    def attach(self, *argv) -> Any:
        pass

    def deinit(self, *argv) -> Any:
        pass

    def detach(self, *argv) -> Any:
        pass

    def multiBtnCb(self, *argv) -> Any:
        pass

    def restart(self, *argv) -> Any:
        pass

    def timerCb(self, *argv) -> Any:
        pass


class BtnChild:
    """"""

    def deinit(self, *argv) -> Any:
        pass

    def isPressed(self, *argv) -> Any:
        pass

    def isReleased(self, *argv) -> Any:
        pass

    def pressFor(self, *argv) -> Any:
        pass

    def restart(self, *argv) -> Any:
        pass

    def upDate(self, *argv) -> Any:
        pass

    def wasDoublePress(self, *argv) -> Any:
        pass

    def wasPressed(self, *argv) -> Any:
        pass

    def wasReleased(self, *argv) -> Any:
        pass


class I2S:
    """"""

    CHANNEL_ALL_LEFT = 2
    CHANNEL_ALL_RIGHT = 1
    CHANNEL_ONLY_LEFT = 4
    CHANNEL_ONLY_RIGHT = 3
    CHANNEL_RIGHT_LEFT = 0
    DAC_BOTH_EN = 3
    DAC_DISABLE = 0
    DAC_LEFT_EN = 2
    DAC_RIGHT_EN = 1
    FORMAT_I2S = 1
    FORMAT_I2S_LSB = 4
    FORMAT_I2S_MSB = 2
    FORMAT_PCM = 8
    FORMAT_PCM_LONG = 32
    FORMAT_PCM_SHORT = 16
    I2S_NUM_0 = 0
    I2S_NUM_1 = 1
    MODE_ADC_BUILT_IN = 32
    MODE_DAC_BUILT_IN = 16
    MODE_MASTER = 1
    MODE_PDM = 64
    MODE_RX = 8
    MODE_SLAVE = 2
    MODE_TX = 4

    def adc_enable(self, *argv) -> Any:
        pass

    def bits(self, *argv) -> Any:
        pass

    def deinit(self, *argv) -> Any:
        pass

    def init(self, *argv) -> Any:
        pass

    def nchannels(self, *argv) -> Any:
        pass

    def read(self, *argv) -> Any:
        pass

    def sample_rate(self, *argv) -> Any:
        pass

    def set_adc_pin(self, *argv) -> Any:
        pass

    def set_dac_mode(self, *argv) -> Any:
        pass

    def set_pin(self, *argv) -> Any:
        pass

    def start(self, *argv) -> Any:
        pass

    def stop(self, *argv) -> Any:
        pass

    def volume(self, *argv) -> Any:
        pass

    def write(self, *argv) -> Any:
        pass


class IP5306:
    """"""

    def getBatteryLevel(self, *argv) -> Any:
        pass

    def init(self, *argv) -> Any:
        pass

    def isChargeFull(self, *argv) -> Any:
        pass

    def isCharging(self, *argv) -> Any:
        pass

    def setCharge(self, *argv) -> Any:
        pass

    def setChargeVolt(self, *argv) -> Any:
        pass

    def setVinMaxCurrent(self, *argv) -> Any:
        pass


class Rgb_multi:
    """"""

    def deinit(self, *argv) -> Any:
        pass

    def setBrightness(self, *argv) -> Any:
        pass

    def setColor(self, *argv) -> Any:
        pass

    def setColorAll(self, *argv) -> Any:
        pass

    def setColorFrom(self, *argv) -> Any:
        pass

    def setShowLock(self, *argv) -> Any:
        pass

    def show(self, *argv) -> Any:
        pass


class Speaker:
    """"""

    def _timeout_cb(self, *argv) -> Any:
        pass

    def checkInit(self, *argv) -> Any:
        pass

    def setBeat(self, *argv) -> Any:
        pass

    def setVolume(self, *argv) -> Any:
        pass

    def sing(self, *argv) -> Any:
        pass

    def tone(self, *argv) -> Any:
        pass


apikey = "67C7D165"
binascii = None
btn = None
btnA = None
btnB = None
btnC = None


def btnText():
    pass


def const():
    pass


display = None


def get_sd_state():
    pass


def hwDeinit():
    pass


lcd = None
m5base = None
machine = None
node_id = "840d8e2598b4"
os = None
power = None
rgb = None


def sd_mount():
    pass


def sd_umount():
    pass


speaker = None
timEx = None
timeSchedule = None
time_ex = None
timerSch = None
