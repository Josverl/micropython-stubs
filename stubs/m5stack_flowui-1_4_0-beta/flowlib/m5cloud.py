"""
Module: 'flowlib.m5cloud' on M5 FlowUI v1.4.0-beta
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


class M5Cloud:
    ''
    def _backend():
        pass

    def _daemonTask():
        pass

    def _error():
        pass

    def _exec_respond():
        pass

    def _msg_deal():
        pass

    def _send_data():
        pass

    def on_connect():
        pass

    def on_data():
        pass

    def run():
        pass


class MQTTClient:
    ''
    def _clean_sock_buffer():
        pass

    def _recv_len():
        pass

    def _send_str():
        pass

    def check_msg():
        pass

    def connect():
        pass

    def disconnect():
        pass

    def lock_msg_rec():
        pass

    def ping():
        pass

    def publish():
        pass

    def set_block():
        pass

    def set_callback():
        pass

    def set_last_will():
        pass

    def socket_connect():
        pass

    def subscribe():
        pass

    def topic_get():
        pass

    def topic_msg_get():
        pass

    def unlock_msg_rec():
        pass

    def wait_msg():
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

STA_BUSY = 1
STA_DOWNLOAD = 3
STA_IDLE = 0
STA_UPLOAD = 2

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
json = None
lcd = None
def loopExit():
    pass

def loopSetIdle():
    pass

def loopState():
    pass

m5base = None
machine = None
def modeSet():
    pass

module = None
network = None
node_id = '840d8e2598b4'
os = None
power = None
def reconnect():
    pass

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
unit = None
def wait():
    pass

def wait_ms():
    pass

wlan_sta = None
