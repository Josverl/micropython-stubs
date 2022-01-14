"""
Module: 'example_pub_button' on esp8266 v1.9.4
"""
# MCU: (sysname='esp8266', nodename='esp8266', release='2.2.0-dev(9422289)', version='v1.9.4-8-ga9a3caad0 on 2018-05-11', machine='ESP module with ESP8266')
# Stubber: 1.1.2 - updated
from typing import Any

CLIENT_ID = None


class MQTTClient:
    """"""

    def _recv_len(self, *argv) -> Any:
        pass

    def _send_str(self, *argv) -> Any:
        pass

    def check_msg(self, *argv) -> Any:
        pass

    def connect(self, *argv) -> Any:
        pass

    def disconnect(self, *argv) -> Any:
        pass

    def ping(self, *argv) -> Any:
        pass

    def publish(self, *argv) -> Any:
        pass

    def set_callback(self, *argv) -> Any:
        pass

    def set_last_will(self, *argv) -> Any:
        pass

    def subscribe(self, *argv) -> Any:
        pass

    def wait_msg(self, *argv) -> Any:
        pass


class Pin:
    """"""

    IN = 0
    IRQ_FALLING = 2
    IRQ_RISING = 1
    OPEN_DRAIN = 2
    OUT = 1
    PULL_UP = 1

    def init(self, *argv) -> Any:
        pass

    def irq(self, *argv) -> Any:
        pass

    def off(self, *argv) -> Any:
        pass

    def on(self, *argv) -> Any:
        pass

    def value(self, *argv) -> Any:
        pass


SERVER = "192.168.1.35"
TOPIC = None
button = None
machine = None


def main():
    pass


time = None
ubinascii = None
