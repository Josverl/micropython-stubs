"""
Module: 'flowlib.m5ucloud' on M5 FlowUI v1.4.0-beta
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


class M5UCloud:
    """"""

    def _error(self, *argv) -> Any:
        pass

    def deinit(self, *argv) -> Any:
        pass

    def exec_deal(self, *argv) -> Any:
        pass

    def on_data(self, *argv) -> Any:
        pass

    def run(self, *argv) -> Any:
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
node_id = "840d8e2598b4"
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
