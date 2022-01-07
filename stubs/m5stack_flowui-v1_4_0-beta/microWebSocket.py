"""
Module: 'microWebSocket' on M5 FlowUI v1.4.0-beta
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-284-g5d8e1c867 on 2019-08-30', machine='ESP32 module with ESP32')
# Stubber: 1.3.1

class MicroWebSocket:
    ''
    def Close():
        pass

    def IsClosed():
        pass

    def SendBinary():
        pass

    def SendText():
        pass

    def _handshake():
        pass

    _handshakeSign = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
    _msgTypeBin = 2
    _msgTypeText = 1
    _opBinFrame = 2
    _opCloseFrame = 8
    _opContFrame = 0
    _opPingFrame = 9
    _opPongFrame = 10
    _opTextFrame = 1
    def _receiveFrame():
        pass

    def _sendFrame():
        pass

    def _tryAllocByteArray():
        pass

    def _tryStartThread():
        pass

    def _wsProcess():
        pass

    def threadID():
        pass

_thread = None
def b2a_base64():
    pass

gc = None
def pack():
    pass


class sha1:
    ''
    def digest():
        pass

    def update():
        pass

time = None
