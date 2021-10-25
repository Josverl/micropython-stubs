from typing import Any

CLOCK_MONOTONIC: int
CLOCK_REALTIME: int

class Pin:
    IN: str
    OUT: str
    def deinit() -> None: ...
    def value() -> None: ...

class PinBase: ...

SIGEV_SIGNAL: int
SIGINT: int
SIGPIPE: int
SIGRTMIN: int
SIGTERM: int
SIG_DFL: int
SIG_IGN: int

class Signal:
    def off() -> None: ...
    def on() -> None: ...
    def value() -> None: ...

class Timer:
    def callback() -> None: ...
    def handler() -> None: ...

array: Any
ffilib: Any
itimerspec_t: Any
libc: Any
librt: Any
mem16: Any
mem32: Any
mem8: Any

def new() -> None: ...

os: Any
pin: Any
sigevent_t: Any

def signal() -> None: ...

signal_i: Any
signal_p: Any
sigval_t: Any

def time_pulse_us() -> None: ...

timer: Any

def timer_create() -> None: ...

timer_create_: Any

def timer_settime() -> None: ...

timer_settime_: Any
timespec_t: Any
uctypes: Any
umachine: Any

def unique_id() -> None: ...

uos: Any
utime: Any
