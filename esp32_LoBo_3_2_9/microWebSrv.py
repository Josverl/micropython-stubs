"""
Module: 'microWebSrv' on esp32_LoBo 3.2.9
"""
# MCU: (sysname='esp32_LoBo', nodename='esp32_LoBo', release='3.2.9', version='ESP32_LoBo_v3.2.9 on 2018-04-12', machine='ESP32 board with ESP32')
# Stubber: 1.1.2

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


class MicroWebSrv:
    ''
    def GetMimeTypeFromFilename():
        pass

    def GetRouteHandler():
        pass

    def HTMLEscape():
        pass

    def IsStarted():
        pass

    def SetNotFoundPageUrl():
        pass

    def Start():
        pass

    def State():
        pass

    def Stop():
        pass

    _client = None
    _docoratedRouteHandlers = None
    def _fileExists():
        pass

    _html_escape_chars = None
    _indexPages = None
    def _isPyHTMLFile():
        pass

    _mimeTypes = None
    def _physPathFromURLPath():
        pass

    _pyhtmlPagesExt = '.pyhtml'
    _response = None
    def _serverProcess():
        pass

    def _tryAllocByteArray():
        pass

    def _tryStartThread():
        pass

    def _unquote():
        pass

    def _unquote_plus():
        pass

    def route():
        pass

    def threadID():
        pass


class MicroWebSrvRoute:
    ''

class MicroWebTemplate:
    ''
    def Execute():
        pass

    INSTRUCTION_ELIF = 'elif'
    INSTRUCTION_ELSE = 'else'
    INSTRUCTION_END = 'end'
    INSTRUCTION_FOR = 'for'
    INSTRUCTION_IF = 'if'
    INSTRUCTION_INCLUDE = 'include'
    INSTRUCTION_PYTHON = 'py'
    TOKEN_CLOSE = '}}'
    TOKEN_CLOSE_LEN = 2
    TOKEN_OPEN = '{{'
    TOKEN_OPEN_LEN = 2
    def Validate():
        pass

    def _parseBloc():
        pass

    def _parseCode():
        pass

    def _processInstructionELIF():
        pass

    def _processInstructionELSE():
        pass

    def _processInstructionEND():
        pass

    def _processInstructionFOR():
        pass

    def _processInstructionIF():
        pass

    def _processInstructionINCLUDE():
        pass

    def _processInstructionPYTHON():
        pass

    def _processToken():
        pass

_thread = None
def dumps():
    pass

gc = None
def loads():
    pass

network = None
re = None
socket = None
def stat():
    pass

time = None
websocket = None
