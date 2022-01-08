"""
Module: 'flowlib.button' on M5 FlowUI v1.4.0-beta
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

DOUBLEPRESS = 8
LONGPRESS = 4
MULTIPRESS = 16
PRESS = 1
PRESSWAIT = 32
RELEASE = 2
_state_list = None
machine = None
micropython = None
time = None
