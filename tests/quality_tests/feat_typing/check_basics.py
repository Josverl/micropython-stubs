# This doesn't quite test everything but just serves to verify that basic syntax works,
# which for MicroPython means everything typing-related should be ignored.
# ref: https://github.com/micropython/micropython-lib/pull/584/

from typing import *
from typing import _AnyCall

MyAlias = str
Vector = List[float]
Nested = Iterable[Tuple[int, ...]]
UserId = NewType("UserId", int)
T = TypeVar("T", int, float, complex)

hintedGlobal: Any = None


def func_with_hints(c: int, b: MyAlias, a: Union[int, None], lst: List[float] = [0.0]) -> Any:
    return 42


class ClassWithHints(Vector):

    a: Vector = [0,0]

    def foo(self, v:Vector) -> None:
        pass

class GenericClassWithHints(Generic[T]):

    a: T = 0

    def foo(self, other: T) -> None:
        pass

# some runtime exercises 

x = func_with_hints(1, "1", None, lst=3.14)
assert x , "annotated function must return a value"

# klass = ClassWithHints
# assert klass
# print( type(klass) )
# assert type(klass) != type(_AnyCall)

# klass.a = [1,2]
# klass.foo([2,3])


print("Done.")