"""
Module: 'microWebSocket' on esp32_LoBo
MCU: (sysname='esp32_LoBo', nodename='esp32_LoBo', release='3.2.24', version='ESP32_LoBo_v3.2.24 on 2018-09-06', machine='ESP32 board with ESP32')
Stubber: 1.0.0 - updated
"""
from typing import Any


class MicroWebSocket:
    """"""

    def Close(self, *args) -> Any:
        pass

    def IsClosed(self, *args) -> Any:
        pass

    def SendBinary(self, *args) -> Any:
        pass

    def SendText(self, *args) -> Any:
        pass

    def _handshake(self, *args) -> Any:
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

    def _receiveFrame(self, *args) -> Any:
        pass

    def _sendFrame(self, *args) -> Any:
        pass

    def _tryAllocByteArray(self, *args) -> Any:
        pass

    def _tryStartThread(self, *args) -> Any:
        pass

    def _wsProcess(self, *args) -> Any:
        pass

    def threadID(self, *args) -> Any:
        pass


_thread = None


def b2a_base64(*args) -> Any:
    pass


gc = None


def pack(*args) -> Any:
    pass


class sha1:
    """"""

    def digest(self, *args) -> Any:
        pass

    def update(self, *args) -> Any:
        pass


time = None
