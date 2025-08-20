from _typeshed import Incomplete, structseq, AnyStr_co
from typing_extensions import TypeAlias, TypeVar
from array import array
from typing import Union

Buffer : TypeAlias= Union[bytes, bytearray, memoryview]

# ------------------------------------------------------------------------------------
# TODO: need some to allow string to be passed in : uart_1.write("hello")
AnyReadableBuf: TypeAlias = bytearray | array | memoryview | bytes | Incomplete
AnyWritableBuf: TypeAlias = bytearray | array | memoryview | Incomplete
