"""
Module: 'pybricks.parameters' on LEGO EV3 v1.0.0
"""
# MCU: sysname=ev3, nodename=ev3, release=('v1.0.0',), version=('0.0.0',), machine=ev3
# Stubber: 1.3.2

class Align:
    ''
    BOTTOM = 2
    BOTTOM_LEFT = 1
    BOTTOM_RIGHT = 3
    CENTER = 5
    LEFT = 4
    RIGHT = 6
    TOP = 8
    TOP_LEFT = 7
    TOP_RIGHT = 9

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

class Direction:
    ''
    CLOCKWISE = 0
    COUNTERCLOCKWISE = 1

class ImageFile:
    ''
    ACCEPT = '/usr/share/images/ev3dev/mono/information/accept.png'
    ANGRY = '/usr/share/images/ev3dev/mono/eyes/angry.png'
    AWAKE = '/usr/share/images/ev3dev/mono/eyes/awake.png'
    BACKWARD = '/usr/share/images/ev3dev/mono/information/backward.png'
    BOTTOM_LEFT = '/usr/share/images/ev3dev/mono/eyes/bottom_left.png'
    BOTTOM_RIGHT = '/usr/share/images/ev3dev/mono/eyes/bottom_right.png'
    CRAZY_1 = '/usr/share/images/ev3dev/mono/eyes/crazy_1.png'
    CRAZY_2 = '/usr/share/images/ev3dev/mono/eyes/crazy_2.png'
    DECLINE = '/usr/share/images/ev3dev/mono/information/decline.png'
    DIZZY = '/usr/share/images/ev3dev/mono/eyes/dizzy.png'
    DOWN = '/usr/share/images/ev3dev/mono/eyes/down.png'
    EV3 = '/usr/share/images/ev3dev/mono/lego/ev3.png'
    EV3_ICON = '/usr/share/images/ev3dev/mono/lego/ev3_icon.png'
    EVIL = '/usr/share/images/ev3dev/mono/eyes/evil.png'
    FORWARD = '/usr/share/images/ev3dev/mono/information/forward.png'
    KNOCKED_OUT = '/usr/share/images/ev3dev/mono/eyes/knocked_out.png'
    LEFT = '/usr/share/images/ev3dev/mono/information/left.png'
    MIDDLE_LEFT = '/usr/share/images/ev3dev/mono/eyes/middle_left.png'
    MIDDLE_RIGHT = '/usr/share/images/ev3dev/mono/eyes/middle_right.png'
    NEUTRAL = '/usr/share/images/ev3dev/mono/eyes/neutral.png'
    NO_GO = '/usr/share/images/ev3dev/mono/information/no_go.png'
    PINCHED_LEFT = '/usr/share/images/ev3dev/mono/eyes/pinched_left.png'
    PINCHED_MIDDLE = '/usr/share/images/ev3dev/mono/eyes/pinched_middle.png'
    PINCHED_RIGHT = '/usr/share/images/ev3dev/mono/eyes/pinched_right.png'
    QUESTION_MARK = '/usr/share/images/ev3dev/mono/information/question_mark.png'
    RIGHT = '/usr/share/images/ev3dev/mono/information/right.png'
    SLEEPING = '/usr/share/images/ev3dev/mono/eyes/sleeping.png'
    STOP_1 = '/usr/share/images/ev3dev/mono/information/stop_1.png'
    STOP_2 = '/usr/share/images/ev3dev/mono/information/stop_2.png'
    TARGET = '/usr/share/images/ev3dev/mono/objects/target.png'
    THUMBS_DOWN = '/usr/share/images/ev3dev/mono/information/thumbs_down.png'
    THUMBS_UP = '/usr/share/images/ev3dev/mono/information/thumbs_up.png'
    TIRED_LEFT = '/usr/share/images/ev3dev/mono/eyes/tired_left.png'
    TIRED_MIDDLE = '/usr/share/images/ev3dev/mono/eyes/tired_middle.png'
    TIRED_RIGHT = '/usr/share/images/ev3dev/mono/eyes/tired_right.png'
    UP = '/usr/share/images/ev3dev/mono/eyes/up.png'
    WARNING = '/usr/share/images/ev3dev/mono/information/warning.png'
    WINKING = '/usr/share/images/ev3dev/mono/eyes/winking.png'
    _BASE_PATH = '/usr/share/images/ev3dev/mono/'

class Port:
    ''
    A = 65
    B = 66
    C = 67
    D = 68
    S1 = 49
    S2 = 50
    S3 = 51
    S4 = 52

class SoundFile:
    ''
    ACTIVATE = '/usr/share/sounds/ev3dev/information/activate.wav'
    AIRBRAKE = '/usr/share/sounds/ev3dev/mechanical/airbrake.wav'
    AIR_RELEASE = '/usr/share/sounds/ev3dev/mechanical/air_release.wav'
    ANALYZE = '/usr/share/sounds/ev3dev/information/analyze.wav'
    BACKING_ALERT = '/usr/share/sounds/ev3dev/mechanical/backing_alert.wav'
    BACKWARDS = '/usr/share/sounds/ev3dev/information/backwards.wav'
    BLACK = '/usr/share/sounds/ev3dev/colors/black.wav'
    BLUE = '/usr/share/sounds/ev3dev/colors/blue.wav'
    BOING = '/usr/share/sounds/ev3dev/expressions/boing.wav'
    BOO = '/usr/share/sounds/ev3dev/expressions/boo.wav'
    BRAVO = '/usr/share/sounds/ev3dev/communication/bravo.wav'
    BROWN = '/usr/share/sounds/ev3dev/colors/brown.wav'
    CAT_PURR = '/usr/share/sounds/ev3dev/animals/cat_purr.wav'
    CHEERING = '/usr/share/sounds/ev3dev/expressions/cheering.wav'
    CLICK = '/usr/share/sounds/ev3dev/system/click.wav'
    COLOR = '/usr/share/sounds/ev3dev/information/color.wav'
    CONFIRM = '/usr/share/sounds/ev3dev/system/confirm.wav'
    CRUNCHING = '/usr/share/sounds/ev3dev/expressions/crunching.wav'
    CRYING = '/usr/share/sounds/ev3dev/expressions/crying.wav'
    DETECTED = '/usr/share/sounds/ev3dev/information/detected.wav'
    DOG_BARK_1 = '/usr/share/sounds/ev3dev/animals/dog_bark_1.wav'
    DOG_BARK_2 = '/usr/share/sounds/ev3dev/animals/dog_bark_2.wav'
    DOG_GROWL = '/usr/share/sounds/ev3dev/animals/dog_growl.wav'
    DOG_SNIFF = '/usr/share/sounds/ev3dev/animals/dog_sniff.wav'
    DOG_WHINE = '/usr/share/sounds/ev3dev/animals/dog_whine.wav'
    DOWN = '/usr/share/sounds/ev3dev/information/down.wav'
    EIGHT = '/usr/share/sounds/ev3dev/numbers/eight.wav'
    ELEPHANT_CALL = '/usr/share/sounds/ev3dev/animals/elephant_call.wav'
    ERROR = '/usr/share/sounds/ev3dev/information/error.wav'
    ERROR_ALARM = '/usr/share/sounds/ev3dev/information/error_alarm.wav'
    EV3 = '/usr/share/sounds/ev3dev/communication/ev3.wav'
    FANFARE = '/usr/share/sounds/ev3dev/expressions/fanfare.wav'
    FANTASTIC = '/usr/share/sounds/ev3dev/communication/fantastic.wav'
    FIVE = '/usr/share/sounds/ev3dev/numbers/five.wav'
    FLASHING = '/usr/share/sounds/ev3dev/information/flashing.wav'
    FORWARD = '/usr/share/sounds/ev3dev/information/forward.wav'
    FOUR = '/usr/share/sounds/ev3dev/numbers/four.wav'
    GAME_OVER = '/usr/share/sounds/ev3dev/communication/game_over.wav'
    GENERAL_ALERT = '/usr/share/sounds/ev3dev/system/general_alert.wav'
    GO = '/usr/share/sounds/ev3dev/communication/go.wav'
    GOOD = '/usr/share/sounds/ev3dev/communication/good.wav'
    GOODBYE = '/usr/share/sounds/ev3dev/communication/goodbye.wav'
    GOOD_JOB = '/usr/share/sounds/ev3dev/communication/good_job.wav'
    GREEN = '/usr/share/sounds/ev3dev/colors/green.wav'
    HELLO = '/usr/share/sounds/ev3dev/communication/hello.wav'
    HI = '/usr/share/sounds/ev3dev/communication/hi.wav'
    HORN_1 = '/usr/share/sounds/ev3dev/mechanical/horn_1.wav'
    HORN_2 = '/usr/share/sounds/ev3dev/mechanical/horn_2.wav'
    INSECT_BUZZ_1 = '/usr/share/sounds/ev3dev/animals/insect_buzz_1.wav'
    INSECT_BUZZ_2 = '/usr/share/sounds/ev3dev/animals/insect_buzz_2.wav'
    INSECT_CHIRP = '/usr/share/sounds/ev3dev/animals/insect_chirp.wav'
    KUNG_FU = '/usr/share/sounds/ev3dev/expressions/kung_fu.wav'
    LASER = '/usr/share/sounds/ev3dev/mechanical/laser.wav'
    LAUGHING_1 = '/usr/share/sounds/ev3dev/expressions/laughing_1.wav'
    LAUGHING_2 = '/usr/share/sounds/ev3dev/expressions/laughing_2.wav'
    LEFT = '/usr/share/sounds/ev3dev/information/left.wav'
    LEGO = '/usr/share/sounds/ev3dev/communication/lego.wav'
    MAGIC_WAND = '/usr/share/sounds/ev3dev/expressions/magic_wand.wav'
    MINDSTORMS = '/usr/share/sounds/ev3dev/communication/mindstorms.wav'
    MORNING = '/usr/share/sounds/ev3dev/communication/morning.wav'
    MOTOR_IDLE = '/usr/share/sounds/ev3dev/mechanical/motor_idle.wav'
    MOTOR_START = '/usr/share/sounds/ev3dev/mechanical/motor_start.wav'
    MOTOR_STOP = '/usr/share/sounds/ev3dev/mechanical/motor_stop.wav'
    NINE = '/usr/share/sounds/ev3dev/numbers/nine.wav'
    NO = '/usr/share/sounds/ev3dev/communication/no.wav'
    OBJECT = '/usr/share/sounds/ev3dev/information/object.wav'
    OKAY = '/usr/share/sounds/ev3dev/communication/okay.wav'
    OKEY_DOKEY = '/usr/share/sounds/ev3dev/communication/okey-dokey.wav'
    ONE = '/usr/share/sounds/ev3dev/numbers/one.wav'
    OUCH = '/usr/share/sounds/ev3dev/expressions/ouch.wav'
    OVERPOWER = '/usr/share/sounds/ev3dev/system/overpower.wav'
    RATCHET = '/usr/share/sounds/ev3dev/mechanical/ratchet.wav'
    READY = '/usr/share/sounds/ev3dev/system/ready.wav'
    RED = '/usr/share/sounds/ev3dev/colors/red.wav'
    RIGHT = '/usr/share/sounds/ev3dev/information/right.wav'
    SEARCHING = '/usr/share/sounds/ev3dev/information/searching.wav'
    SEVEN = '/usr/share/sounds/ev3dev/numbers/seven.wav'
    SHOUTING = '/usr/share/sounds/ev3dev/expressions/shouting.wav'
    SIX = '/usr/share/sounds/ev3dev/numbers/six.wav'
    SMACK = '/usr/share/sounds/ev3dev/expressions/smack.wav'
    SNAKE_HISS = '/usr/share/sounds/ev3dev/animals/snake_hiss.wav'
    SNAKE_RATTLE = '/usr/share/sounds/ev3dev/animals/snake_rattle.wav'
    SNEEZING = '/usr/share/sounds/ev3dev/expressions/sneezing.wav'
    SNORING = '/usr/share/sounds/ev3dev/expressions/snoring.wav'
    SONAR = '/usr/share/sounds/ev3dev/mechanical/sonar.wav'
    SORRY = '/usr/share/sounds/ev3dev/communication/sorry.wav'
    SPEED_DOWN = '/usr/share/sounds/ev3dev/movements/speed_down.wav'
    SPEED_IDLE = '/usr/share/sounds/ev3dev/movements/speed_idle.wav'
    SPEED_UP = '/usr/share/sounds/ev3dev/movements/speed_up.wav'
    START = '/usr/share/sounds/ev3dev/information/start.wav'
    STOP = '/usr/share/sounds/ev3dev/information/stop.wav'
    TEN = '/usr/share/sounds/ev3dev/numbers/ten.wav'
    THANK_YOU = '/usr/share/sounds/ev3dev/communication/thank_you.wav'
    THREE = '/usr/share/sounds/ev3dev/numbers/three.wav'
    TICK_TACK = '/usr/share/sounds/ev3dev/mechanical/tick_tack.wav'
    TOUCH = '/usr/share/sounds/ev3dev/information/touch.wav'
    TURN = '/usr/share/sounds/ev3dev/information/turn.wav'
    TWO = '/usr/share/sounds/ev3dev/numbers/two.wav'
    T_REX_ROAR = '/usr/share/sounds/ev3dev/animals/t-rex_roar.wav'
    UH_OH = '/usr/share/sounds/ev3dev/expressions/uh-oh.wav'
    UP = '/usr/share/sounds/ev3dev/information/up.wav'
    WHITE = '/usr/share/sounds/ev3dev/colors/white.wav'
    YELLOW = '/usr/share/sounds/ev3dev/colors/yellow.wav'
    YES = '/usr/share/sounds/ev3dev/communication/yes.wav'
    ZERO = '/usr/share/sounds/ev3dev/numbers/zero.wav'
    _BASE_PATH = '/usr/share/sounds/ev3dev/'

class Stop:
    ''
    BRAKE = 1
    COAST = 0
    HOLD = 2
