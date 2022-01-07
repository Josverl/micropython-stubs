"""
Module: 'flowlib.m5ucloud' on M5 FlowUI v1.4.0-beta
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


class M5UCloud:
    ''
    def _error():
        pass

    def deinit():
        pass

    def exec_deal():
        pass

    def on_data():
        pass

    def run():
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

_thread = None
apikey = '67C7D165'
binascii = None
btn = None
btnA = None
btnB = None
btnC = None
def btnText():
    pass

def cfgRead():
    pass

def cfgWrite():
    pass

config_normal = '{\n    "start": "flow",\n    "mode": "internet",\n    "server": "Flow.m5stack.com", \n    "wifi": {\n        "ssid": "",\n        "password": ""\n    }\n}\n'
def const():
    pass

def core_start():
    pass

display = None
def flowDeinit():
    pass


class flowExit:
    ''
gc = None
def getP2PData():
    pass

def get_sd_state():
    pass

def hwDeinit():
    pass

io = None
lcd = None
def loopExit():
    pass

def loopSetIdle():
    pass

def loopState():
    pass

m5base = None
m5uart = None
machine = None
def modeSet():
    pass

module = None
node_id = '840d8e2598b4'
os = None
power = None
def remoteInit():
    pass

def resetDefault():
    pass

rgb = None
def sd_mount():
    pass

def sd_umount():
    pass

def sendP2PData():
    pass

def setP2PData():
    pass

speaker = None
def start():
    pass

def startBeep():
    pass

sys = None
timEx = None
time = None
timeSchedule = None
time_ex = None
timerSch = None
uiflow = None
unit = None
def wait():
    pass

def wait_ms():
    pass

