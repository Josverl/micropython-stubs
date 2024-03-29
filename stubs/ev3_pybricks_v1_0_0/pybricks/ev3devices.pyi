from typing import Any

class Button:
    BEACON: int
    CENTER: int
    DOWN: int
    LEFT: int
    LEFT_DOWN: int
    LEFT_UP: int
    RIGHT: int
    RIGHT_DOWN: int
    RIGHT_UP: int
    UP: int

class Color:
    BLACK: int
    BLUE: int
    BROWN: int
    GREEN: int
    ORANGE: int
    PURPLE: int
    RED: int
    WHITE: int
    YELLOW: int

class ColorSensor:
    def _close_files(self, *argv) -> Any: ...
    _default_mode: Any
    _ev3dev_driver_name: str
    def _mode(self, *argv) -> Any: ...
    _number_of_values: int
    def _open_files(self, *argv) -> Any: ...
    def _value(self, *argv) -> Any: ...
    def ambient(self, *argv) -> Any: ...
    def color(self, *argv) -> Any: ...
    def reflection(self, *argv) -> Any: ...
    def rgb(self, *argv) -> Any: ...

class Direction:
    CLOCKWISE: int
    COUNTERCLOCKWISE: int

class Ev3devSensor:
    def _close_files(self, *argv) -> Any: ...
    _default_mode: Any
    _ev3dev_driver_name: str
    def _mode(self, *argv) -> Any: ...
    _number_of_values: int
    def _open_files(self, *argv) -> Any: ...
    def _value(self, *argv) -> Any: ...

class Ev3devUartSensor:
    def _close_files(self, *argv) -> Any: ...
    _default_mode: Any
    _ev3dev_driver_name: str
    def _mode(self, *argv) -> Any: ...
    _number_of_values: int
    def _open_files(self, *argv) -> Any: ...
    def _reset(self, *argv) -> Any: ...
    def _reset_port(self, *argv) -> Any: ...
    def _value(self, *argv) -> Any: ...

class GyroSensor:
    def _calibrate(self, *argv) -> Any: ...
    def _close_files(self, *argv) -> Any: ...
    _default_mode: str
    _ev3dev_driver_name: str
    def _mode(self, *argv) -> Any: ...
    _number_of_values: int
    def _open_files(self, *argv) -> Any: ...
    def _reset(self, *argv) -> Any: ...
    def _reset_port(self, *argv) -> Any: ...
    def _value(self, *argv) -> Any: ...
    def angle(self, *argv) -> Any: ...
    def reset_angle(self, *argv) -> Any: ...
    def speed(self, *argv) -> Any: ...

class InfraredSensor:
    def _close_files(self, *argv) -> Any: ...
    _combinations: Any
    _default_mode: Any
    _ev3dev_driver_name: str
    def _mode(self, *argv) -> Any: ...
    _number_of_values: int
    def _open_files(self, *argv) -> Any: ...
    def _value(self, *argv) -> Any: ...
    def beacon(self, *argv) -> Any: ...
    def buttons(self, *argv) -> Any: ...
    def distance(self, *argv) -> Any: ...

class Motor:
    def angle(self, *argv) -> Any: ...
    def dc(self, *argv) -> Any: ...
    def reset_angle(self, *argv) -> Any: ...
    def run(self, *argv) -> Any: ...
    def run_angle(self, *argv) -> Any: ...
    def run_target(self, *argv) -> Any: ...
    def run_time(self, *argv) -> Any: ...
    def run_until_stalled(self, *argv) -> Any: ...
    def set_dc_settings(self, *argv) -> Any: ...
    def set_pid_settings(self, *argv) -> Any: ...
    def set_run_settings(self, *argv) -> Any: ...
    def speed(self, *argv) -> Any: ...
    def stalled(self, *argv) -> Any: ...
    def stop(self, *argv) -> Any: ...
    def track_target(self, *argv) -> Any: ...

class StopWatch:
    def pause(self, *argv) -> Any: ...
    def reset(self, *argv) -> Any: ...
    def resume(self, *argv) -> Any: ...
    def time(self, *argv) -> Any: ...

class TouchSensor:
    def _close_files(self, *argv) -> Any: ...
    _default_mode: Any
    _ev3dev_driver_name: str
    def _mode(self, *argv) -> Any: ...
    _number_of_values: int
    def _open_files(self, *argv) -> Any: ...
    def _value(self, *argv) -> Any: ...
    def pressed(self, *argv) -> Any: ...

class UltrasonicSensor:
    PING_WAIT: int
    def _close_files(self, *argv) -> Any: ...
    _default_mode: Any
    _ev3dev_driver_name: str
    def _mode(self, *argv) -> Any: ...
    _number_of_values: int
    def _open_files(self, *argv) -> Any: ...
    def _value(self, *argv) -> Any: ...
    def distance(self, *argv) -> Any: ...
    def presence(self, *argv) -> Any: ...

def wait() -> None: ...
