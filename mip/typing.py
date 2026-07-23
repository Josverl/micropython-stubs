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


# class _anyCallType:
#     def __getitem__(self, _):
#         return _anyCall


# _anyCall = _anyCall


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

AbstractSet = _anyCall
AsyncContextManager = _anyCall
AsyncGenerator = _anyCall
AsyncIterable = _anyCall
AsyncIterator = _anyCall
Awaitable = _anyCall
Callable = _anyCall
ChainMap = _anyCall
Collection = _anyCall
Container = _anyCall
ContextManager = _anyCall
Coroutine = _anyCall
Counter = _anyCall
DefaultDict = _anyCall
Deque = _anyCall
Dict = _anyCall
FrozenSet = _anyCall
Generator = _anyCall
Generic = _anyCall
Iterable = _anyCall
Iterator = _anyCall
List = _anyCall
Literal = _anyCall
LiteralString = _anyCall
Mapping = _anyCall
MutableMapping = _anyCall
MutableSequence = _anyCall
MutableSet = _anyCall
NamedTuple = _anyCall
NotRequired = _anyCall
Optional = _anyCall
OrderedDict = _anyCall
ReadOnly = _anyCall
Required = _anyCall
Self = _anyCall
Sequence = _anyCall
Set = _anyCall
Tuple = _anyCall
Type = _anyCall
Union = _anyCall

TYPE_CHECKING = False

# snarky way to alias typing_extensions to typing ( saving 59 bytes)
import sys
sys.modules["typing_extensions"] = sys.modules["typing"]
del sys