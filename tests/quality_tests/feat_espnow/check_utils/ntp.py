import machine
import ntptime

server = "192.168.10.1"


def settime(host=None):
    host = host or server
    try:
        ntptime.host = host
        ntptime.settime()
        print("Time set to:", machine.RTC().datetime())
    except (OSError, OverflowError) as e:
        print("ntptime.settime():", e)
