from typing import Any

ONE_SHOT: int
PERIODIC: int

class Timer:
    ONE_SHOT: int
    PERIODIC: int
    def deinit(self, *argv) -> Any: ...
    def update(self, *argv) -> Any: ...

class TimerEx:
    ONE_SHOT: int
    PERIODIC: int
    def addTimer(self, *argv) -> Any: ...
    def checkInit(self, *argv) -> Any: ...
    def deinit(self, *argv) -> Any: ...
    def timeCb(self, *argv) -> Any: ...

_thread: Any
delete_num: Any
time: Any
