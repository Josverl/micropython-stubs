"""
Module: 'machine' on LEGO EV3 v1.0.0
"""
# MCU: sysname=ev3, nodename=ev3, release=('v1.0.0',), version=('0.0.0',), machine=ev3
# Stubber: 1.3.2 - updated
from typing import Any

CLOCK_MONOTONIC = 1
CLOCK_REALTIME = 0


class Pin:
    """"""

    IN = "in"
    OUT = "out"

    def deinit(self, *argv) -> Any:
        pass

    def value(self, *argv) -> Any:
        pass


class PinBase:
    """"""


SIGEV_SIGNAL = 0
SIGINT = 2
SIGPIPE = 13
SIGRTMIN = 34
SIGTERM = 15
SIG_DFL = 0
SIG_IGN = 1


class Signal:
    """"""

    def off(self, *argv) -> Any:
        pass

    def on(self, *argv) -> Any:
        pass

    def value(self, *argv) -> Any:
        pass


class Timer:
    """"""

    def callback(self, *argv) -> Any:
        pass

    def handler(self, *argv) -> Any:
        pass


array = None
ffilib = None
itimerspec_t = None
libc = None
librt = None
mem16 = None
mem32 = None
mem8 = None


def new():
    pass


os = None
pin = None
sigevent_t = None


def signal():
    pass


signal_i = None
signal_p = None
sigval_t = None


def time_pulse_us():
    pass


timer = None


def timer_create():
    pass


timer_create_ = None


def timer_settime():
    pass


timer_settime_ = None
timespec_t = None
uctypes = None
umachine = None


def unique_id():
    pass


uos = None
utime = None
