"""
Module: 'flowlib.m5cloud' on M5 FlowUI v1.4.0-beta
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


class M5Cloud:
    """"""

    def _backend(self, *argv) -> Any:
        pass

    def _daemonTask(self, *argv) -> Any:
        pass

    def _error(self, *argv) -> Any:
        pass

    def _exec_respond(self, *argv) -> Any:
        pass

    def _msg_deal(self, *argv) -> Any:
        pass

    def _send_data(self, *argv) -> Any:
        pass

    def on_connect(self, *argv) -> Any:
        pass

    def on_data(self, *argv) -> Any:
        pass

    def run(self, *argv) -> Any:
        pass


class MQTTClient:
    """"""

    def _clean_sock_buffer(self, *argv) -> Any:
        pass

    def _recv_len(self, *argv) -> Any:
        pass

    def _send_str(self, *argv) -> Any:
        pass

    def check_msg(self, *argv) -> Any:
        pass

    def connect(self, *argv) -> Any:
        pass

    def disconnect(self, *argv) -> Any:
        pass

    def lock_msg_rec(self, *argv) -> Any:
        pass

    def ping(self, *argv) -> Any:
        pass

    def publish(self, *argv) -> Any:
        pass

    def set_block(self, *argv) -> Any:
        pass

    def set_callback(self, *argv) -> Any:
        pass

    def set_last_will(self, *argv) -> Any:
        pass

    def socket_connect(self, *argv) -> Any:
        pass

    def subscribe(self, *argv) -> Any:
        pass

    def topic_get(self, *argv) -> Any:
        pass

    def topic_msg_get(self, *argv) -> Any:
        pass

    def unlock_msg_rec(self, *argv) -> Any:
        pass

    def wait_msg(self, *argv) -> Any:
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


STA_BUSY = 1
STA_DOWNLOAD = 3
STA_IDLE = 0
STA_UPLOAD = 2


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


_thread = None
apikey = "67C7D165"
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
    """"""


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
node_id = "840d8e2598b4"
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
