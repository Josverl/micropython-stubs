"""
Module: 'example_pub_button' on esp8266 v1.11
"""
# MCU: (sysname='esp8266', nodename='esp8266', release='2.2.0-dev(9422289)', version='v1.11-8-g48dcbbe60 on 2019-05-29', machine='ESP module with ESP8266')
# Stubber: 1.1.0 - updated
from typing import Any

CLIENT_ID = None


class MQTTClient:
    """"""

    def _recv_len(self, *args) -> Any:
        pass

    def _send_str(self, *args) -> Any:
        pass

    def check_msg(self, *args) -> Any:
        pass

    def connect(self, *args) -> Any:
        pass

    def disconnect(self, *args) -> Any:
        pass

    def ping(self, *args) -> Any:
        pass

    def publish(self, *args) -> Any:
        pass

    def set_callback(self, *args) -> Any:
        pass

    def set_last_will(self, *args) -> Any:
        pass

    def subscribe(self, *args) -> Any:
        pass

    def wait_msg(self, *args) -> Any:
        pass


class Pin:
    """"""

    IN = 0
    IRQ_FALLING = 2
    IRQ_RISING = 1
    OPEN_DRAIN = 2
    OUT = 1
    PULL_UP = 1

    def init(self, *args) -> Any:
        pass

    def irq(self, *args) -> Any:
        pass

    def off(self, *args) -> Any:
        pass

    def on(self, *args) -> Any:
        pass

    def value(self, *args) -> Any:
        pass


SERVER = "192.168.1.35"
TOPIC = None
button = None
machine = None


def main(*args) -> Any:
    pass


time = None
ubinascii = None
