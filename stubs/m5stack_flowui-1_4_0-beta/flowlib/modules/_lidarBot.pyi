from typing import Any

class LidarBot:
    def controlWheel() -> None: ...
    def deinit() -> None: ...
    def goAhead() -> None: ...
    def goBack() -> None: ...
    def setOneRgb() -> None: ...
    def setRgb() -> None: ...
    def setServo() -> None: ...
    def setStepMotor() -> None: ...
    def turnLeft() -> None: ...
    def turnRight() -> None: ...

class LidarStep:
    def controlWheel() -> None: ...
    def goAhead() -> None: ...
    def goBack() -> None: ...
    def setOneRgb() -> None: ...
    def setRgb() -> None: ...
    def setServo() -> None: ...
    def setStepMotor() -> None: ...
    def turnLeft() -> None: ...
    def turnRight() -> None: ...

controlMap: Any
machine: Any
