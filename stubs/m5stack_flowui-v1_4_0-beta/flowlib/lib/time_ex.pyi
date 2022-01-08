from typing import Any

ONE_SHOT: int
PERIODIC: int

class Timer:
    ONE_SHOT: int
    PERIODIC: int
    def deinit() -> None: ...
    def update() -> None: ...

class TimerEx:
    ONE_SHOT: int
    PERIODIC: int
    def addTimer() -> None: ...
    def checkInit() -> None: ...
    def deinit() -> None: ...
    def timeCb() -> None: ...

_thread: Any
delete_num: Any
time: Any
