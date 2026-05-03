"""
Module: 'unittest.__init__' on micropython-v1.28.0-unix-standard
"""
# MCU: {'family': 'micropython', 'version': '1.28.0', 'build': '', 'ver': '1.28.0', 'port': 'unix', 'board': 'standard', 'board_id': 'standard', 'variant': '', 'cpu': 'linux [GCC 12.5.0] version', 'mpy': 'v6.3', 'arch': 'x64'}
# Stubber: v1.28.3
from __future__ import annotations
from typing import Any, Final, Generator, AsyncGenerator
from _typeshed import Incomplete

def skip(*args, **kwargs) -> Incomplete:
    ...

def skipIf(*args, **kwargs) -> Incomplete:
    ...

def _handle_test_exception(*args, **kwargs) -> Incomplete:
    ...

def _capture_exc(*args, **kwargs) -> Incomplete:
    ...

def _run_suite(*args, **kwargs) -> Incomplete:
    ...

def skipUnless(*args, **kwargs) -> Incomplete:
    ...

def expectedFailure(*args, **kwargs) -> Incomplete:
    ...

def main(*args, **kwargs) -> Incomplete:
    ...


class TestSuite():
    def addTest(self, *args, **kwargs) -> Incomplete:
        ...

    def _load_module(self, *args, **kwargs) -> Incomplete:
        ...

    def run(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class AssertRaisesContext():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class TextTestRunner():
    def run(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class TestRunner():
    def run(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class TestResult():
    def wasSuccessful(self, *args, **kwargs) -> Incomplete:
        ...

    def printErrorList(self, *args, **kwargs) -> Incomplete:
        ...

    def printErrors(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class SkipTest():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class NullContext():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class SubtestContext():
    def __init__(self, *argv, **kwargs) -> None:
        ...


class TestCase():
    def assertIsNone(self, *args, **kwargs) -> Incomplete:
        ...

    def assertIsNotNone(self, *args, **kwargs) -> Incomplete:
        ...

    def assertNotAlmostEqual(self, *args, **kwargs) -> Incomplete:
        ...

    def assertIsNot(self, *args, **kwargs) -> Incomplete:
        ...

    def assertIs(self, *args, **kwargs) -> Incomplete:
        ...

    def assertIsInstance(self, *args, **kwargs) -> Incomplete:
        ...

    def assertRaises(self, *args, **kwargs) -> Incomplete:
        ...

    def assertTrue(self, *args, **kwargs) -> Incomplete:
        ...

    def assertIn(self, *args, **kwargs) -> Incomplete:
        ...

    def assertFalse(self, *args, **kwargs) -> Incomplete:
        ...

    def assertWarns(self, *args, **kwargs) -> Incomplete:
        ...

    def subTest(self, *args, **kwargs) -> Incomplete:
        ...

    def skipTest(self, *args, **kwargs) -> Incomplete:
        ...

    def assertAlmostEqual(self, *args, **kwargs) -> Incomplete:
        ...

    def doCleanups(self, *args, **kwargs) -> Incomplete:
        ...

    def addCleanup(self, *args, **kwargs) -> Incomplete:
        ...

    def assertLessEqual(self, *args, **kwargs) -> Incomplete:
        ...

    def assertGreaterEqual(self, *args, **kwargs) -> Incomplete:
        ...

    def fail(self, *args, **kwargs) -> Incomplete:
        ...

    def assertNotEqual(self, *args, **kwargs) -> Incomplete:
        ...

    def assertEqual(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

traceback: Incomplete ## <class 'NoneType'> = None
