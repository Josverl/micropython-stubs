from typing import Any

class Align:
    BOTTOM: int
    BOTTOM_LEFT: int
    BOTTOM_RIGHT: int
    CENTER: int
    LEFT: int
    RIGHT: int
    TOP: int
    TOP_LEFT: int
    TOP_RIGHT: int

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

class DriveBase:
    def drive(self, *argv) -> Any: ...
    def drive_time(self, *argv) -> Any: ...
    def stop(self, *argv) -> Any: ...

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

class ImageFile:
    ACCEPT: str
    ANGRY: str
    AWAKE: str
    BACKWARD: str
    BOTTOM_LEFT: str
    BOTTOM_RIGHT: str
    CRAZY_1: str
    CRAZY_2: str
    DECLINE: str
    DIZZY: str
    DOWN: str
    EV3: str
    EV3_ICON: str
    EVIL: str
    FORWARD: str
    KNOCKED_OUT: str
    LEFT: str
    MIDDLE_LEFT: str
    MIDDLE_RIGHT: str
    NEUTRAL: str
    NO_GO: str
    PINCHED_LEFT: str
    PINCHED_MIDDLE: str
    PINCHED_RIGHT: str
    QUESTION_MARK: str
    RIGHT: str
    SLEEPING: str
    STOP_1: str
    STOP_2: str
    TARGET: str
    THUMBS_DOWN: str
    THUMBS_UP: str
    TIRED_LEFT: str
    TIRED_MIDDLE: str
    TIRED_RIGHT: str
    UP: str
    WARNING: str
    WINKING: str
    _BASE_PATH: str

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

class Port:
    A: int
    B: int
    C: int
    D: int
    S1: int
    S2: int
    S3: int
    S4: int

class SoundFile:
    ACTIVATE: str
    AIRBRAKE: str
    AIR_RELEASE: str
    ANALYZE: str
    BACKING_ALERT: str
    BACKWARDS: str
    BLACK: str
    BLUE: str
    BOING: str
    BOO: str
    BRAVO: str
    BROWN: str
    CAT_PURR: str
    CHEERING: str
    CLICK: str
    COLOR: str
    CONFIRM: str
    CRUNCHING: str
    CRYING: str
    DETECTED: str
    DOG_BARK_1: str
    DOG_BARK_2: str
    DOG_GROWL: str
    DOG_SNIFF: str
    DOG_WHINE: str
    DOWN: str
    EIGHT: str
    ELEPHANT_CALL: str
    ERROR: str
    ERROR_ALARM: str
    EV3: str
    FANFARE: str
    FANTASTIC: str
    FIVE: str
    FLASHING: str
    FORWARD: str
    FOUR: str
    GAME_OVER: str
    GENERAL_ALERT: str
    GO: str
    GOOD: str
    GOODBYE: str
    GOOD_JOB: str
    GREEN: str
    HELLO: str
    HI: str
    HORN_1: str
    HORN_2: str
    INSECT_BUZZ_1: str
    INSECT_BUZZ_2: str
    INSECT_CHIRP: str
    KUNG_FU: str
    LASER: str
    LAUGHING_1: str
    LAUGHING_2: str
    LEFT: str
    LEGO: str
    MAGIC_WAND: str
    MINDSTORMS: str
    MORNING: str
    MOTOR_IDLE: str
    MOTOR_START: str
    MOTOR_STOP: str
    NINE: str
    NO: str
    OBJECT: str
    OKAY: str
    OKEY_DOKEY: str
    ONE: str
    OUCH: str
    OVERPOWER: str
    RATCHET: str
    READY: str
    RED: str
    RIGHT: str
    SEARCHING: str
    SEVEN: str
    SHOUTING: str
    SIX: str
    SMACK: str
    SNAKE_HISS: str
    SNAKE_RATTLE: str
    SNEEZING: str
    SNORING: str
    SONAR: str
    SORRY: str
    SPEED_DOWN: str
    SPEED_IDLE: str
    SPEED_UP: str
    START: str
    STOP: str
    TEN: str
    THANK_YOU: str
    THREE: str
    TICK_TACK: str
    TOUCH: str
    TURN: str
    TWO: str
    T_REX_ROAR: str
    UH_OH: str
    UP: str
    WHITE: str
    YELLOW: str
    YES: str
    ZERO: str
    _BASE_PATH: str

class Stop:
    BRAKE: int
    COAST: int
    HOLD: int

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

brick: Any

def print() -> None: ...
def wait() -> None: ...
