"""
Module: 'ntptime' on esp8266 v1.11
"""
# MCU: (sysname='esp8266', nodename='esp8266', release='2.2.0-dev(9422289)', version='v1.11-8-g48dcbbe60 on 2019-05-29', machine='ESP module with ESP8266')
# Stubber: 1.1.0 - updated
from typing import Any

NTP_DELTA = 3155673600
host = "pool.ntp.org"


def settime(*args) -> Any:
    pass


socket = None
struct = None


def time(*args) -> Any:
    pass
