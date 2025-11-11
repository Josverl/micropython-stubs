# Test Timer with hard parameter (added in MicroPython v1.27+)

from machine import Timer


def mycallback(t):
    pass


# Timer with hard interrupt context
tim = Timer(-1)
tim.init(mode=Timer.PERIODIC, freq=1000, callback=mycallback, hard=True)

# Timer with soft interrupt context
tim.init(mode=Timer.PERIODIC, period=100, callback=mycallback, hard=False)

# Timer with hard parameter using freq
tim.init(freq=500, callback=mycallback, hard=True)

# Constructor with hard parameter
tim2 = Timer(-1, mode=Timer.ONE_SHOT, period=1000, callback=mycallback, hard=False)
