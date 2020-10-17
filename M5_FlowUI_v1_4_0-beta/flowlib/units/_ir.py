"""
Module: 'flowlib.units._ir' on M5 FlowUI v1.4.0-beta
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-284-g5d8e1c867 on 2019-08-30', machine='ESP32 module with ESP32')
# Stubber: 1.3.1

class Ir:
    ''
    def _irq_cb():
        pass

    def _update():
        pass

    def deinit():
        pass

    portMethod = 15
    def rxStatus():
        pass

    def txOff():
        pass

    def txOn():
        pass


class PWM:
    ''
    def deinit():
        pass

    def duty():
        pass

    def freq():
        pass

    def init():
        pass

    def list():
        pass

    def pause():
        pass

    def resume():
        pass


class Pin:
    ''
    IN = 1
    INOUT = 3
    IRQ_FALLING = 2
    IRQ_RISING = 1
    OPEN_DRAIN = 7
    OUT = 3
    OUT_OD = 6
    PULL_DOWN = 1
    PULL_FLOAT = 3
    PULL_HOLD = 4
    PULL_UP = 2
    WAKE_HIGH = 5
    WAKE_LOW = 4
    def deinit():
        pass

    def init():
        pass

    def irq():
        pass

    def off():
        pass

    def on():
        pass

    def value():
        pass


class Timer:
    ''
    ONE_SHOT = 0
    PERIODIC = 1
    def deinit():
        pass

    def init():
        pass

    def value():
        pass

peripheral = None
unit = None
