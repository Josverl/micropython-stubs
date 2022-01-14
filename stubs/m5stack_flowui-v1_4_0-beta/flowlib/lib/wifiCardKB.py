"""
Module: 'flowlib.lib.wifiCardKB' on M5 FlowUI v1.4.0-beta
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


class M5Button:
    """"""


class M5Circle:
    """"""

    def hide(self, *argv) -> Any:
        pass

    def setBgColor(self, *argv) -> Any:
        pass

    def setBorderColor(self, *argv) -> Any:
        pass

    def setPosition(self, *argv) -> Any:
        pass

    def setSize(self, *argv) -> Any:
        pass

    def show(self, *argv) -> Any:
        pass


class M5Img:
    """"""

    def changeImg(self, *argv) -> Any:
        pass

    def hide(self, *argv) -> Any:
        pass

    def setPosition(self, *argv) -> Any:
        pass

    def show(self, *argv) -> Any:
        pass


class M5Rect:
    """"""

    def hide(self, *argv) -> Any:
        pass

    def setBgColor(self, *argv) -> Any:
        pass

    def setBorderColor(self, *argv) -> Any:
        pass

    def setPosition(self, *argv) -> Any:
        pass

    def setSize(self, *argv) -> Any:
        pass

    def show(self, *argv) -> Any:
        pass


class M5TextBox:
    """"""

    def hide(self, *argv) -> Any:
        pass

    def setColor(self, *argv) -> Any:
        pass

    def setFont(self, *argv) -> Any:
        pass

    def setPosition(self, *argv) -> Any:
        pass

    def setRotate(self, *argv) -> Any:
        pass

    def setText(self, *argv) -> Any:
        pass

    def show(self, *argv) -> Any:
        pass


class M5Title:
    """"""

    def hide(self, *argv) -> Any:
        pass

    def setBgColor(self, *argv) -> Any:
        pass

    def setFgColor(self, *argv) -> Any:
        pass

    def setTitle(self, *argv) -> Any:
        pass

    def show(self, *argv) -> Any:
        pass


def M5UI_Deinit():
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


def setScreenColor():
    pass


speaker = None
timEx = None
time = None
timeSchedule = None
time_ex = None
timerSch = None
unit = None
