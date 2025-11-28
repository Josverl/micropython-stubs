from _typeshed import Incomplete
from collections.abc import Generator

def _f() -> None: ...

FunctionType: Incomplete
LambdaType: Incomplete
CodeType: Incomplete
MappingProxyType: Incomplete
SimpleNamespace: Incomplete

def _g() -> Generator[Incomplete]: ...

GeneratorType: Incomplete

class _C:
    def _m(self) -> None: ...

MethodType: Incomplete
BuiltinFunctionType: Incomplete
BuiltinMethodType: Incomplete
ModuleType: Incomplete
TracebackType: Incomplete
FrameType: Incomplete
tb: Incomplete
GetSetDescriptorType: Incomplete
MemberDescriptorType: Incomplete

def new_class(name, bases=(), kwds=None, exec_body=None):
    """Create a class object dynamically using the appropriate metaclass."""

def prepare_class(name, bases=(), kwds=None):
    """Call the __prepare__ method of the appropriate metaclass.

    Returns (metaclass, namespace, kwds) as a 3-tuple

    *metaclass* is the appropriate metaclass
    *namespace* is the prepared class namespace
    *kwds* is an updated copy of the passed in kwds argument with any
    'metaclass' entry removed. If no kwds argument is passed in, this will
    be an empty dict.
    """

def _calculate_meta(meta, bases):
    """Calculate the most derived metaclass."""
