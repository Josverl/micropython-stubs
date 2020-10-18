"""
Module: 'pybricks.ev3devices' on LEGO EV3 v1.0.0
"""
# MCU: sysname=ev3, nodename=ev3, release=('v1.0.0',), version=('0.0.0',), machine=ev3
# Stubber: 1.3.2

class Button:
    ''
    BEACON = 256
    CENTER = 32
    DOWN = 4
    LEFT = 16
    LEFT_DOWN = 2
    LEFT_UP = 128
    RIGHT = 64
    RIGHT_DOWN = 8
    RIGHT_UP = 512
    UP = 256

class Color:
    ''
    BLACK = 1
    BLUE = 2
    BROWN = 7
    GREEN = 3
    ORANGE = 8
    PURPLE = 9
    RED = 5
    WHITE = 6
    YELLOW = 4

class ColorSensor:
    ''
    def _close_files():
        pass

    _default_mode = None
    _ev3dev_driver_name = 'lego-ev3-color'
    def _mode():
        pass

    _number_of_values = 3
    def _open_files():
        pass

    def _value():
        pass

    def ambient():
        pass

    def color():
        pass

    def reflection():
        pass

    def rgb():
        pass


class Direction:
    ''
    CLOCKWISE = 0
    COUNTERCLOCKWISE = 1

class Ev3devSensor:
    ''
    def _close_files():
        pass

    _default_mode = None
    _ev3dev_driver_name = 'none'
    def _mode():
        pass

    _number_of_values = 1
    def _open_files():
        pass

    def _value():
        pass


class Ev3devUartSensor:
    ''
    def _close_files():
        pass

    _default_mode = None
    _ev3dev_driver_name = 'none'
    def _mode():
        pass

    _number_of_values = 1
    def _open_files():
        pass

    def _reset():
        pass

    def _reset_port():
        pass

    def _value():
        pass


class GyroSensor:
    ''
    def _calibrate():
        pass

    def _close_files():
        pass

    _default_mode = 'GYRO-G&A'
    _ev3dev_driver_name = 'lego-ev3-gyro'
    def _mode():
        pass

    _number_of_values = 2
    def _open_files():
        pass

    def _reset():
        pass

    def _reset_port():
        pass

    def _value():
        pass

    def angle():
        pass

    def reset_angle():
        pass

    def speed():
        pass


class InfraredSensor:
    ''
    def _close_files():
        pass

    _combinations = None
    _default_mode = None
    _ev3dev_driver_name = 'lego-ev3-ir'
    def _mode():
        pass

    _number_of_values = 8
    def _open_files():
        pass

    def _value():
        pass

    def beacon():
        pass

    def buttons():
        pass

    def distance():
        pass


class Motor:
    ''
    def angle():
        pass

    def dc():
        pass

    def reset_angle():
        pass

    def run():
        pass

    def run_angle():
        pass

    def run_target():
        pass

    def run_time():
        pass

    def run_until_stalled():
        pass

    def set_dc_settings():
        pass

    def set_pid_settings():
        pass

    def set_run_settings():
        pass

    def speed():
        pass

    def stalled():
        pass

    def stop():
        pass

    def track_target():
        pass


class StopWatch:
    ''
    def pause():
        pass

    def reset():
        pass

    def resume():
        pass

    def time():
        pass


class TouchSensor:
    ''
    def _close_files():
        pass

    _default_mode = None
    _ev3dev_driver_name = 'lego-ev3-touch'
    def _mode():
        pass

    _number_of_values = 1
    def _open_files():
        pass

    def _value():
        pass

    def pressed():
        pass


class UltrasonicSensor:
    ''
    PING_WAIT = 300
    def _close_files():
        pass

    _default_mode = None
    _ev3dev_driver_name = 'lego-ev3-us'
    def _mode():
        pass

    _number_of_values = 1
    def _open_files():
        pass

    def _value():
        pass

    def distance():
        pass

    def presence():
        pass

def wait():
    pass

