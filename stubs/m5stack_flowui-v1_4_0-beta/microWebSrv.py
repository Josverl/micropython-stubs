"""
Module: 'microWebSrv' on M5 FlowUI v1.4.0-beta
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


class MicroWebSrv:
    """"""

    def GetMimeTypeFromFilename(self, *argv) -> Any:
        pass

    def GetRouteHandler(self, *argv) -> Any:
        pass

    def HTMLEscape(self, *argv) -> Any:
        pass

    def IsStarted(self, *argv) -> Any:
        pass

    def SetNotFoundPageUrl(self, *argv) -> Any:
        pass

    def Start(self, *argv) -> Any:
        pass

    def State(self, *argv) -> Any:
        pass

    def Stop(self, *argv) -> Any:
        pass

    _client = None
    _docoratedRouteHandlers = None

    def _fileExists(self, *argv) -> Any:
        pass

    _html_escape_chars = None
    _indexPages = None

    def _isPyHTMLFile(self, *argv) -> Any:
        pass

    _mimeTypes = None

    def _physPathFromURLPath(self, *argv) -> Any:
        pass

    _pyhtmlPagesExt = ".pyhtml"
    _response = None

    def _serverProcess(self, *argv) -> Any:
        pass

    def _tryAllocByteArray(self, *argv) -> Any:
        pass

    def _tryStartThread(self, *argv) -> Any:
        pass

    def _unquote(self, *argv) -> Any:
        pass

    def _unquote_plus(self, *argv) -> Any:
        pass

    def route(self, *argv) -> Any:
        pass

    def threadID(self, *argv) -> Any:
        pass


class MicroWebSrvRoute:
    """"""


class MicroWebTemplate:
    """"""

    def Execute(self, *argv) -> Any:
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

    def Validate(self, *argv) -> Any:
        pass

    def _parseBloc(self, *argv) -> Any:
        pass

    def _parseCode(self, *argv) -> Any:
        pass

    def _processInstructionELIF(self, *argv) -> Any:
        pass

    def _processInstructionELSE(self, *argv) -> Any:
        pass

    def _processInstructionEND(self, *argv) -> Any:
        pass

    def _processInstructionFOR(self, *argv) -> Any:
        pass

    def _processInstructionIF(self, *argv) -> Any:
        pass

    def _processInstructionINCLUDE(self, *argv) -> Any:
        pass

    def _processInstructionPYTHON(self, *argv) -> Any:
        pass

    def _processToken(self, *argv) -> Any:
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
