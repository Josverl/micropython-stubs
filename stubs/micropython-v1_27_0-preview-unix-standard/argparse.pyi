"""
Module: 'argparse' on micropython-v1.27.0-preview-unix-standard
"""
# MCU: {'family': 'micropython', 'version': '1.27.0-preview', 'build': '218', 'ver': '1.27.0-preview-218', 'port': 'unix', 'board': 'standard', 'board_id': 'standard', 'variant': '', 'cpu': 'linux [GCC 12.4.0] version', 'mpy': 'v6.3', 'arch': 'x64'}
# Stubber: v1.26.2
from __future__ import annotations
from typing import Any, Final, Generator
from _typeshed import Incomplete

def _dest_from_optnames(*args, **kwargs) -> Incomplete:
    ...

def namedtuple(*args, **kwargs) -> Incomplete:
    ...


class _ArgError(Exception):
    ...

class _Arg():
    def parse(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...


class ArgumentParser():
    def parse_args(self, *args, **kwargs) -> Incomplete:
        ...

    def usage(self, *args, **kwargs) -> Incomplete:
        ...

    def parse_known_args(self, *args, **kwargs) -> Incomplete:
        ...

    def _parse_args(self, *args, **kwargs) -> Incomplete:
        ...

    def add_argument(self, *args, **kwargs) -> Incomplete:
        ...

    def _parse_args_impl(self, *args, **kwargs) -> Incomplete:
        ...

    def __init__(self, *argv, **kwargs) -> None:
        ...

