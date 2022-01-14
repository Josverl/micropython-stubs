"""
Module: 'gsm' on esp32_LoBo
MCU: (sysname='esp32_LoBo', nodename='esp32_LoBo', release='3.2.24', version='ESP32_LoBo_v3.2.24 on 2018-09-06', machine='ESP32 board with ESP32')
Stubber: 1.0.0 - updated
"""
from typing import Any

SMS_ALL = 0
SMS_READ = 2
SMS_UNREAD = 1
SORT_ASC = 1
SORT_DESC = 2
SORT_NONE = 0


def atcmd(*args) -> Any:
    pass


def checkSMS(*args) -> Any:
    pass


def connect(*args) -> Any:
    pass


def debug(*args) -> Any:
    pass


def deleteSMS(*args) -> Any:
    pass


def disconnect(*args) -> Any:
    pass


def ifconfig(*args) -> Any:
    pass


def readSMS(*args) -> Any:
    pass


def sendSMS(*args) -> Any:
    pass


def sms_cb(*args) -> Any:
    pass


def start(*args) -> Any:
    pass


def status(*args) -> Any:
    pass


def stop(*args) -> Any:
    pass
