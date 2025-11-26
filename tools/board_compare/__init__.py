"""
MicroPython Board Comparison Tool

A tool to compare modules, classes, methods, and parameters across different
MicroPython boards and versions.
"""

__version__ = "1.0.0"

from .models import Board, Module, Class, Method, Parameter, DatabaseSchema
from .scan_stubs import StubScanner, scan_board_stubs
from .build_database import DatabaseBuilder, build_database_for_version

__all__ = [
    "Board",
    "Module",
    "Class",
    "Method",
    "Parameter",
    "DatabaseSchema",
    "StubScanner",
    "scan_board_stubs",
    "DatabaseBuilder",
    "build_database_for_version",
]
