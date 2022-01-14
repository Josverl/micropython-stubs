"""
Module: 'microWebSrv' on esp32_LoBo
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


class MicroWebSrv:
    """"""

    def GetMimeTypeFromFilename(self, *args) -> Any:
        pass

    def GetRouteHandler(self, *args) -> Any:
        pass

    def HTMLEscape(self, *args) -> Any:
        pass

    def IsStarted(self, *args) -> Any:
        pass

    def SetNotFoundPageUrl(self, *args) -> Any:
        pass

    def Start(self, *args) -> Any:
        pass

    def State(self, *args) -> Any:
        pass

    def Stop(self, *args) -> Any:
        pass

    _client = None
    _docoratedRouteHandlers = None

    def _fileExists(self, *args) -> Any:
        pass

    _html_escape_chars = None
    _indexPages = None

    def _isPyHTMLFile(self, *args) -> Any:
        pass

    _mimeTypes = None

    def _physPathFromURLPath(self, *args) -> Any:
        pass

    _pyhtmlPagesExt = ".pyhtml"
    _response = None

    def _serverProcess(self, *args) -> Any:
        pass

    def _tryAllocByteArray(self, *args) -> Any:
        pass

    def _tryStartThread(self, *args) -> Any:
        pass

    def _unquote(self, *args) -> Any:
        pass

    def _unquote_plus(self, *args) -> Any:
        pass

    def route(self, *args) -> Any:
        pass

    def threadID(self, *args) -> Any:
        pass


class MicroWebSrvRoute:
    """"""


class MicroWebTemplate:
    """"""

    def Execute(self, *args) -> Any:
        pass

    INSTRUCTION_ELIF = "elif"
    INSTRUCTION_ELSE = "else"
    INSTRUCTION_END = "end"
    INSTRUCTION_FOR = "for"
    INSTRUCTION_IF = "if"
    INSTRUCTION_INCLUDE = "include"
    INSTRUCTION_PYTHON = "py"
    TOKEN_CLOSE = "}}"
    TOKEN_CLOSE_LEN = 2
    TOKEN_OPEN = "{{"
    TOKEN_OPEN_LEN = 2

    def Validate(self, *args) -> Any:
        pass

    def _parseBloc(self, *args) -> Any:
        pass

    def _parseCode(self, *args) -> Any:
        pass

    def _processInstructionELIF(self, *args) -> Any:
        pass

    def _processInstructionELSE(self, *args) -> Any:
        pass

    def _processInstructionEND(self, *args) -> Any:
        pass

    def _processInstructionFOR(self, *args) -> Any:
        pass

    def _processInstructionIF(self, *args) -> Any:
        pass

    def _processInstructionINCLUDE(self, *args) -> Any:
        pass

    def _processInstructionPYTHON(self, *args) -> Any:
        pass

    def _processToken(self, *args) -> Any:
        pass


_thread = None


def dumps(*args) -> Any:
    pass


gc = None


def loads(*args) -> Any:
    pass


network = None
re = None
socket = None


def stat(*args) -> Any:
    pass


time = None
