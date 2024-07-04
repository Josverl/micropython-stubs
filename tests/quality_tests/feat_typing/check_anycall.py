from typing import Any, Generic, TypeVar

from typing_extensions import TYPE_CHECKING

T = TypeVar('T')

class Foo(Generic[T]):
   pass

class Bar(Foo[Any]):
   pass
