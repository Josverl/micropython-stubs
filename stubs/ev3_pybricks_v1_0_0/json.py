"""
Module: 'json' on LEGO EV3 v1.0.0
"""
# MCU: sysname=ev3, nodename=ev3, release=('v1.0.0',), version=('0.0.0',), machine=ev3
# Stubber: 1.3.2 - updated
from typing import Any


class JSONDecoder:
    """"""

    def decode(self, *argv) -> Any:
        pass

    def raw_decode(self, *argv) -> Any:
        pass


class JSONEncoder:
    """"""

    def default(self, *argv) -> Any:
        pass

    def encode(self, *argv) -> Any:
        pass

    item_separator = ", "

    def iterencode(self, *argv) -> Any:
        pass

    key_separator = ": "


_default_decoder = None
_default_encoder = None
decoder = None


def dump():
    pass


def dumps():
    pass


encoder = None


def load():
    pass


def loads():
    pass


scanner = None
