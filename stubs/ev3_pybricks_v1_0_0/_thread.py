"""
Module: '_thread' on LEGO EV3 v1.0.0
"""
# MCU: sysname=ev3, nodename=ev3, release=('v1.0.0',), version=('0.0.0',), machine=ev3
# Stubber: 1.3.2 - updated
from typing import Any


class LockType:
    """"""

    def acquire(self, *argv) -> Any:
        pass

    def locked(self, *argv) -> Any:
        pass

    def release(self, *argv) -> Any:
        pass


def allocate_lock():
    pass


def exit():
    pass


def get_ident():
    pass


def stack_size():
    pass


def start_new_thread():
    pass
