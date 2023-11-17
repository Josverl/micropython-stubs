# board : ESP32
# ref : https://docs.micropython.org/en/latest/esp32/quickref.html
import utime as time

import machine

machine.freq()  # get the current frequency of the CPU
machine.freq(240000000)  # set the CPU frequency to 240 MHz


# Real time clock (RTC)

from machine import RTC

rtc = RTC()
rtc.datetime((2017, 8, 23, 1, 12, 48, 0, 0))  # set a specific date and time
rtc.datetime()  # get date and time


# WDT (Watchdog timer)

from machine import WDT

# enable the WDT with a timeout of 5s (1s is the minimum)
wdt = WDT(timeout=5000)
wdt.feed()


