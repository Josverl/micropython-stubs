import __future__

from pathlib import Path

from mp_evaluator import MicroPythonDocTestEvaluator, MicroPythonEvaluator
from mp_parser import MicroPythonClearNamespaceParser, MicroPythonDocTestParser, MicroPythonSkipParser
from sybil import Sybil
from sybil.parsers.rest import CaptureParser, CodeBlockParser, DocTestDirectiveParser

docs_path = Path(__file__).parent / "examples"
docs_path = Path(__file__).parent / "micropython/docs"
docs_path = Path(__file__).parent

sybil = Sybil(
    path=docs_path.as_posix(),
    parsers=[
        MicroPythonSkipParser(),  # Use MCU-aware skip parser that handles all skip directives
        MicroPythonClearNamespaceParser(),  # Use MicroPython-specific clear namespace
        MicroPythonDocTestParser(),  # Use custom doctest parser that handles both directives and inline doctests
        CodeBlockParser(language="python", evaluator=MicroPythonEvaluator()),  # Re-enabled
    ],
    pattern="*.rst",
)


pytest_collect_file = sybil.pytest()
