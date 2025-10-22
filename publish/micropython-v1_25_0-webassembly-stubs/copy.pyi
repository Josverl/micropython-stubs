from _typeshed import Incomplete

__all__ = ["Error", "copy", "deepcopy"]

class Error(Exception): ...

error = Error

def copy(x):
    """Shallow copy operation on arbitrary Python objects.

    See the module's __doc__ string for more info.
    """

def deepcopy(x, memo: Incomplete | None = None, _nil=[]):
    """Deep copy operation on arbitrary Python objects.

    See the module's __doc__ string for more info.
    """

class _EmptyClass: ...
