"""
Module: 'flowlib.lib.wavplayer' on M5 FlowUI v1.4.0-beta
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-284-g5d8e1c867 on 2019-08-30', machine='ESP32 module with ESP32')
# Stubber: 1.3.1

class Btn:
    ''
    def attach():
        pass

    def deinit():
        pass

    def detach():
        pass

    def multiBtnCb():
        pass

    def restart():
        pass

    def timerCb():
        pass


class BtnChild:
    ''
    def deinit():
        pass

    def isPressed():
        pass

    def isReleased():
        pass

    def pressFor():
        pass

    def restart():
        pass

    def upDate():
        pass

    def wasDoublePress():
        pass

    def wasPressed():
        pass

    def wasReleased():
        pass


class I2S:
    ''
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
    def adc_enable():
        pass

    def bits():
        pass

    def deinit():
        pass

    def init():
        pass

    def nchannels():
        pass

    def read():
        pass

    def sample_rate():
        pass

    def set_adc_pin():
        pass

    def set_dac_mode():
        pass

    def set_pin():
        pass

    def start():
        pass

    def stop():
        pass

    def volume():
        pass

    def write():
        pass


class IP5306:
    ''
    def getBatteryLevel():
        pass

    def init():
        pass

    def isChargeFull():
        pass

    def isCharging():
        pass

    def setCharge():
        pass

    def setChargeVolt():
        pass

    def setVinMaxCurrent():
        pass


class Rgb_multi:
    ''
    def deinit():
        pass

    def setBrightness():
        pass

    def setColor():
        pass

    def setColorAll():
        pass

    def setColorFrom():
        pass

    def setShowLock():
        pass

    def show():
        pass


class Speaker:
    ''
    def _timeout_cb():
        pass

    def checkInit():
        pass

    def setBeat():
        pass

    def setVolume():
        pass

    def sing():
        pass

    def tone():
        pass

apikey = '67C7D165'
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
node_id = '840d8e2598b4'
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
