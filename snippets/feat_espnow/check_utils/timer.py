# """
# timer.py: A module for creating convenient timers based on generators

# Examples:

#     machine_test = False
#     for t in timer_ms(1500, sleep_ms=200):
#         print(t)
#         if machine_test:
#             break
#     else:
#         print("Timed out - no data")

#     try:
#         for t in timer_ms(30000, 1000, raise_on_timeout=True):
#             print(t)
#     except TimeoutError as err:
#         print(err)

#     for t in timer_ms():
#         print(t)
#         if utime.time() == 0:
#             break

#     timer = timer_ms(timeout_ms=30000, countdown=True)
#     timer = countdown_timer_ms(timeout_ms=30000)

#     with Timer(10000) as t:
#         while t.check():
#             print("Waiting", t.time())
# """

from utime import sleep, sleep_ms, ticks_diff, ticks_ms


class TimeoutError(Exception):
    pass


# A timer generator: on each iteration, yield milliseconds since the first call.
def _timer_ms():
    start = ticks_ms()
    while True:
        reset = yield ticks_diff(ticks_ms(), start)
        if type(reset) in [int, float]:
            start = ticks_ms() - reset


# Reset the start value of a timer
def reset(timer, time_ms=0):
    timer.send(time_ms)


# A timeout generator (milliseconds)
def _timeout_ms(timer, timeout_ms):
    for dt in timer:
        if dt >= timeout_ms:
            break
        yield dt


# Add a busy sleep on every iteration through the timer.
def _sleep_ms(timer, delay_ms):
    for i, dt in enumerate(timer):
        yield dt
        if delay_ms:
            sleep_ms((i + 1) * delay_ms - next(timer))


# Make a timer generator which raises exception if the timeout is reached
def _raise_on_timeout(timer, exc=True):
    yield from timer
    raise TimeoutError if exc is True else exc  # type: ignore


# Make a timer generator a countdown timer
def _countdown(timer, start):
    return (start - dt for dt in timer)


def check(timer):
    try:
        next(timer)
        return True
    except StopIteration:
        return False


def is_expired(timer):
    return not check(timer)


def start(timer):
    return next(timer)


# Construct a timer/timeout generator in milliseconds
def timer_ms(timeout_ms, sleep_ms=0, countdown=False, exc=None):
    timer = _timer_ms()
    if sleep_ms > 0:
        timer = _sleep_ms(timer, sleep_ms)
    if timeout_ms > 0:
        timer = _timeout_ms(timer, timeout_ms)
        if countdown:
            timer = _countdown(timer, timeout_ms)
        if exc is not None:
            timer = _raise_on_timeout(timer, exc)
    return timer


def countdown_timer_ms(t=0, sleep_ms=0, exc=None):
    return timer_ms(t, sleep_ms, True, exc)


# Construct a timer/timeout generator in seconds
def timer_s(timeout_s, sleep_s=0, countdown=False, exc=None):
    return (dt / 1000 for dt in timer_ms(timeout_s * 1000, sleep_s * 1000, countdown, exc))


class Timer:
    def __init__(self, timeout):
        self.timeout = timeout
        self.timer = None

    def start(self):
        self.timer = enumerate(timer_ms(self.timeout, exc=True))
        return next(self.timer)  # This starts the timer!

    def reset(self):
        self.timer = enumerate(timer_ms(self.timeout, exc=True))
        return

    def time(self):
        return next(self.timer)[1] if self.timer else None

    def check(self):
        dt = self.time()
        return dt is not None

    def check_wait(self, delay_ms=0):
        i, dt = next(self.timer)  # type: ignore
        if i > 0 and delay_ms:
            sleep_ms(delay_ms)
        return dt is not None

    def __enter__(self):
        self.timer = enumerate(timer_ms(self.timeout, exc=True))
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if isinstance(exc_value, TimeoutError):
            self.timer = None
            return True
