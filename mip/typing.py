__version__ = "1.28.0"


def cast(_, val):
    return val


def get_origin(_):
    return None


def get_args(_):
    return ()


def no_type_check(func):
    return func


def overload(_):
    return None


def override(func):
    return func


def reveal_type(key):
    return key


class _AnyCall:
    def __init__(*args, **_):
        pass

    def __call__(*args, **_):
        pass

    def __getitem__(self, _):
        return _any_call


_any_call = _AnyCall()


def TypeVar(key, *types, bound=None, covariant=False, contravariant=False, infer_variance=False):
    return key


def TypeVarTuple(key):
    return key


def NewType(_, type):
    return type


class Any:
    pass


class BinaryIO:
    pass


class ClassVar:
    pass


class Final:
    pass


class Hashable:
    pass


class IO:
    pass


class NoReturn:
    pass


class Sized:
    pass


class SupportsInt:
    pass


class SupportsFloat:
    pass


class SupportsComplex:
    pass


class SupportsBytes:
    pass


class SupportsIndex:
    pass


class SupportsAbs:
    pass


class SupportsRound:
    pass


class TextIO:
    pass


# must be a real class to allow `class Foo(Protocol):`
class Protocol:
    pass


AnyStr = str
TypedDict = dict
TypeAlias = object
# Deprecated
# Text = str
# Pattern = str
# Match = str

AbstractSet = _any_call
AsyncContextManager = _any_call
AsyncGenerator = _any_call
AsyncIterable = _any_call
AsyncIterator = _any_call
Awaitable = _any_call
Callable = _any_call
ChainMap = _any_call
Collection = _any_call
Container = _any_call
ContextManager = _any_call
Coroutine = _any_call
Counter = _any_call
DefaultDict = _any_call
Deque = _any_call
Dict = _any_call
FrozenSet = _any_call
Generator = _any_call
Generic = _any_call
Iterable = _any_call
Iterator = _any_call
List = _any_call
Literal = _any_call
LiteralString = _any_call
Mapping = _any_call
MutableMapping = _any_call
MutableSequence = _any_call
MutableSet = _any_call
NamedTuple = _any_call
NotRequired = _any_call
Optional = _any_call
OrderedDict = _any_call
ReadOnly = _any_call
Required = _any_call
Reversible = _any_call
Self = _any_call
Sequence = _any_call
Set = _any_call
Tuple = _any_call
Type = _any_call
Union = _any_call
Unpack = _any_call

TYPE_CHECKING = False

# snarky way to alias typing_extensions to typing ( saving 59 bytes)
import sys

sys.modules["typing_extensions"] = sys.modules["typing"]
del sys
