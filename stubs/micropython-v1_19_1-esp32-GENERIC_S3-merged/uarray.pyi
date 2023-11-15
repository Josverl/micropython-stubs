from typing import List, Optional, Any
from _typeshed import Incomplete as Incomplete

class array(List):
    """
    Create array with elements of given type. Initial contents of the
    array are given by *iterable*. If it is not provided, an empty
    array is created.
    """

    def extend(self, iterable) -> Incomplete:
        """
        Append new elements as contained in *iterable* to the end of
        array, growing it.
        """
    def decode(self, *args, **kwargs) -> Any: ...
    def append(self, val) -> Incomplete:
        """
        Append new element *val* to the end of array, growing it.
        """
    def __init__(self, typecode, iterable: Optional[Any] = ...) -> None: ...
