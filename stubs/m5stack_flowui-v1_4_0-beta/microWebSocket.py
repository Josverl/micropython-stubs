"""
Module: 'microWebSocket' on M5 FlowUI v1.4.0-beta
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-284-g5d8e1c867 on 2019-08-30', machine='ESP32 module with ESP32')
# Stubber: 1.3.1 - updated
from typing import Any


class MicroWebSocket:
    """"""

    def Close(self, *argv) -> Any:
        pass

    def IsClosed(self, *argv) -> Any:
        pass

    def SendBinary(self, *argv) -> Any:
        pass

    def SendText(self, *argv) -> Any:
        pass

    def _handshake(self, *argv) -> Any:
        pass

    _handshakeSign = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
    _msgTypeBin = 2
    _msgTypeText = 1
    _opBinFrame = 2
    _opCloseFrame = 8
    _opContFrame = 0
    _opPingFrame = 9
    _opPongFrame = 10
    _opTextFrame = 1

    def _receiveFrame(self, *argv) -> Any:
        pass

    def _sendFrame(self, *argv) -> Any:
        pass

    def _tryAllocByteArray(self, *argv) -> Any:
        pass

    def _tryStartThread(self, *argv) -> Any:
        pass

    def _wsProcess(self, *argv) -> Any:
        pass

    def threadID(self, *argv) -> Any:
        pass


_thread = None


def b2a_base64():
    pass


gc = None


def pack():
    pass


class sha1:
    """"""

    def digest(self, *argv) -> Any:
        pass

    def update(self, *argv) -> Any:
        pass


time = None
