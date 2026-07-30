"""
Module: 'unittest.__init__' on micropython-v1.28.0-webassembly-pyscript
"""
# MCU: {'family': 'micropython', 'version': '1.28.0', 'build': '', 'ver': '1.28.0', 'port': 'webassembly', 'board': 'pyscript', 'board_id': 'pyscript', 'variant': '', 'cpu': 'Emscripten', 'mpy': 'v6.3', 'arch': ''}
# Stubber: v1.28.3
from __future__ import annotations
from typing import Any, Final, Generator, AsyncGenerator
from _typeshed import Incomplete

def _capture_exc(x0, x1) -> Incomplete:
    ...

def expectedFailure(x0) -> Incomplete:
    ...

def _run_suite(x0, x1, x2) -> Incomplete:
    ...

def _handle_test_exception(x0, x1, x2, x3) -> Incomplete:
    ...

def skip(x0) -> Incomplete:
    ...

def main(x0, x1) -> Incomplete:
    ...

def skipUnless(x0, x1) -> Incomplete:
    ...

def skipIf(x0, x1) -> Incomplete:
    ...


class TestSuite():
    def addTest(self, x1) -> Incomplete:
        ...

    def run(self, x1) -> Incomplete:
        ...

    def _load_module(self, x1) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

traceback: Incomplete ## <class 'NoneType'> = None

class TextTestRunner():
    def run(self, x1) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class AssertRaisesContext():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class TestRunner():
    def run(self, x1) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class TestCase():
    def assertNotEqual(self, x1, x2, x3) -> Incomplete:
        ...

    def assertRaises(self, x1, x2) -> Incomplete:
        ...

    def assertIsNotNone(self, x1, x2) -> Incomplete:
        ...

    def assertNotAlmostEqual(self, x1, x2, x3, x4, x5) -> Incomplete:
        ...

    def assertLessEqual(self, x1, x2, x3) -> Incomplete:
        ...

    def fail(self, x1) -> Incomplete:
        ...

    def skipTest(self, x1) -> Incomplete:
        ...

    def assertTrue(self, x1, x2) -> Incomplete:
        ...

    def doCleanups(self) -> Incomplete:
        ...

    def assertWarns(self, x1) -> Incomplete:
        ...

    def subTest(self, x1) -> Incomplete:
        ...

    def assertEqual(self, x1, x2, x3) -> Incomplete:
        ...

    def assertFalse(self, x1, x2) -> Incomplete:
        ...

    def assertIsNot(self, x1, x2, x3) -> Incomplete:
        ...

    def assertAlmostEqual(self, x1, x2, x3, x4, x5) -> Incomplete:
        ...

    def addCleanup(self, x1) -> Incomplete:
        ...

    def assertIsInstance(self, x1, x2, x3) -> Incomplete:
        ...

    def assertIsNone(self, x1, x2) -> Incomplete:
        ...

    def assertGreaterEqual(self, x1, x2, x3) -> Incomplete:
        ...

    def assertIs(self, x1, x2, x3) -> Incomplete:
        ...

    def assertIn(self, x1, x2, x3) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class TestResult():
    def printErrors(self) -> Incomplete:
        ...

    def wasSuccessful(self) -> Incomplete:
        ...

    def printErrorList(self, x1) -> Incomplete:
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

