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


class _AnyCall:
    def __init__(*args, **_):
        pass

    def __call__(*args, **_):
        pass

    def __getitem__(self, _):
        return _anyCall


_anyCall = _AnyCall()


class _SubscriptableType:
    def __getitem__(self, _):
        return _anyCall


_Subscriptable = _SubscriptableType()


def TypeVar(_, *types, bound = None, covariant=False, contravariant=False, infer_variance=False):
    return None


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


class Protocol:
    pass


AnyStr = str
TypedDict = dict
TypeAlias = object
# Deprecated
# Text = str
# Pattern = str
# Match = str

AbstractSet = _Subscriptable
AsyncContextManager = _Subscriptable
AsyncGenerator = _Subscriptable
AsyncIterable = _Subscriptable
AsyncIterator = _Subscriptable
Awaitable = _Subscriptable
Callable = _Subscriptable
ChainMap = _Subscriptable
Collection = _Subscriptable
Container = _Subscriptable
ContextManager = _Subscriptable
Coroutine = _Subscriptable
Counter = _Subscriptable
DefaultDict = _Subscriptable
Deque = _Subscriptable
Dict = _Subscriptable
FrozenSet = _Subscriptable
Generator = _Subscriptable
Generic = _Subscriptable
Iterable = _Subscriptable
Iterator = _Subscriptable
List = _Subscriptable
Literal = _Subscriptable
LiteralString = _Subscriptable
Mapping = _Subscriptable
MutableMapping = _Subscriptable
MutableSequence = _Subscriptable
MutableSet = _Subscriptable
NamedTuple = _Subscriptable
NotRequired = _Subscriptable
Optional = _Subscriptable
OrderedDict = _Subscriptable
ReadOnly = _Subscriptable
Required = _Subscriptable
Self = _Subscriptable
Sequence = _Subscriptable
Set = _Subscriptable
Tuple = _Subscriptable
Type = _Subscriptable
Union = _Subscriptable

TYPE_CHECKING = False

# snarky way to alias typing_extensions to typing ( saving 59 bytes)
import sys
sys.modules["typing_extensions"] = sys.modules["typing"]
del sys