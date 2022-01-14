"""
Module: 'umqtt.simple' on LEGO EV3 v1.0.0
"""
# MCU: sysname=ev3, nodename=ev3, release=('v1.0.0',), version=('0.0.0',), machine=ev3
# Stubber: 1.3.2 - updated
from typing import Any


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


class MQTTException(Exception):
    """"""


def hexlify():
    pass


socket = None
struct = None
