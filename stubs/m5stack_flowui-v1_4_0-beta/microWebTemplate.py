"""
Module: 'microWebTemplate' on M5 FlowUI v1.4.0-beta
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-284-g5d8e1c867 on 2019-08-30', machine='ESP32 module with ESP32')
# Stubber: 1.3.1 - updated
from typing import Any


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


re = None
