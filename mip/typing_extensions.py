"""
This module provides runtime support for type hints.	
based on : https://github.com/micropython/micropython-lib/pull/584
"""


def cast(type, val):
    return val


def get_origin(type):
    return None


def get_args(type):
    return ()


def no_type_check(arg):
    return arg


def overload(func):
    return None


def NewType(name, type):
    return type


class _AnyCall:
    """A class to ignore type hints in code."""

    def __init__(*args, **kwargs):
        pass

    def __call__(*args, **kwargs):
        pass

    def __getitem__(self, arg):
        return _any_call


_any_call = _AnyCall()

TYPE_CHECKING = False


# ref: https://github.com/micropython/micropython-lib/pull/584#issuecomment-2317690854
def __getattr__(attr):
    return _any_call
