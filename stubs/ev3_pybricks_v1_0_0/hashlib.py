"""
Module: 'hashlib' on LEGO EV3 v1.0.0
"""
# MCU: sysname=ev3, nodename=ev3, release=('v1.0.0',), version=('0.0.0',), machine=ev3
# Stubber: 1.3.2 - updated
from typing import Any

_sha224 = None
_sha256 = None
_sha384 = None
_sha512 = None


def init():
    pass


def new():
    pass


class sha1:
    """"""

    def digest(self, *argv) -> Any:
        pass

    def update(self, *argv) -> Any:
        pass


class sha224:
    """"""

    block_size = 64

    def copy(self, *argv) -> Any:
        pass

    def digest(self, *argv) -> Any:
        pass

    digest_size = 28
    digestsize = 28

    def hexdigest(self, *argv) -> Any:
        pass

    def update(self, *argv) -> Any:
        pass


class sha256:
    """"""

    def digest(self, *argv) -> Any:
        pass

    def update(self, *argv) -> Any:
        pass


class sha384:
    """"""

    block_size = 128

    def copy(self, *argv) -> Any:
        pass

    def digest(self, *argv) -> Any:
        pass

    digest_size = 48
    digestsize = 48

    def hexdigest(self, *argv) -> Any:
        pass

    def update(self, *argv) -> Any:
        pass


class sha512:
    """"""

    block_size = 128

    def copy(self, *argv) -> Any:
        pass

    def digest(self, *argv) -> Any:
        pass

    digest_size = 64
    digestsize = 64

    def hexdigest(self, *argv) -> Any:
        pass

    def update(self, *argv) -> Any:
        pass


uhashlib = None
