"""
Module: 'unittest.__init__' on micropython-v1.27.0-preview-webassembly-pyscript
"""
# MCU: {'family': 'micropython', 'version': '1.27.0-preview', 'build': '252', 'ver': '1.27.0-preview-252', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.26.2
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

def _capture_exc(*args, **kwargs) -> Incomplete:
    ...

def expectedFailure(*args, **kwargs) -> Incomplete:
    ...

def _run_suite(*args, **kwargs) -> Incomplete:
    ...

def _handle_test_exception(*args, **kwargs) -> Incomplete:
    ...

def skip(*args, **kwargs) -> Incomplete:
    ...

def main(*args, **kwargs) -> Incomplete:
    ...

def skipUnless(*args, **kwargs) -> Incomplete:
    ...

def skipIf(*args, **kwargs) -> Incomplete:
    ...


class TestSuite():
    def addTest(self, *args, **kwargs) -> Incomplete:
        ...

    def run(self, *args, **kwargs) -> Incomplete:
        ...

    def _load_module(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

traceback: Incomplete ## <class 'NoneType'> = None

class TextTestRunner():
    def run(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class AssertRaisesContext():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class TestRunner():
    def run(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class TestCase():
    def assertNotEqual(self, *args, **kwargs) -> Incomplete:
        ...

    def assertRaises(self, *args, **kwargs) -> Incomplete:
        ...

    def assertIsNotNone(self, *args, **kwargs) -> Incomplete:
        ...

    def assertNotAlmostEqual(self, *args, **kwargs) -> Incomplete:
        ...

    def assertLessEqual(self, *args, **kwargs) -> Incomplete:
        ...

    def fail(self, *args, **kwargs) -> Incomplete:
        ...

    def skipTest(self, *args, **kwargs) -> Incomplete:
        ...

    def assertTrue(self, *args, **kwargs) -> Incomplete:
        ...

    def doCleanups(self, *args, **kwargs) -> Incomplete:
        ...

    def assertWarns(self, *args, **kwargs) -> Incomplete:
        ...

    def subTest(self, *args, **kwargs) -> Incomplete:
        ...

    def assertEqual(self, *args, **kwargs) -> Incomplete:
        ...

    def assertFalse(self, *args, **kwargs) -> Incomplete:
        ...

    def assertIsNot(self, *args, **kwargs) -> Incomplete:
        ...

    def assertAlmostEqual(self, *args, **kwargs) -> Incomplete:
        ...

    def addCleanup(self, *args, **kwargs) -> Incomplete:
        ...

    def assertIsInstance(self, *args, **kwargs) -> Incomplete:
        ...

    def assertIsNone(self, *args, **kwargs) -> Incomplete:
        ...

    def assertGreaterEqual(self, *args, **kwargs) -> Incomplete:
        ...

    def assertIs(self, *args, **kwargs) -> Incomplete:
        ...

    def assertIn(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class TestResult():
    def printErrors(self, *args, **kwargs) -> Incomplete:
        ...

    def wasSuccessful(self, *args, **kwargs) -> Incomplete:
        ...

    def printErrorList(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class NullContext():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class SubtestContext():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class SkipTest():
    def __init__(self, *argv, **kwargs) -> None:
        ...

