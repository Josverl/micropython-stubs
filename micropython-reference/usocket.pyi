# socket module
# Allow the use of micro-module notation

from socket import *  # type: ignore

from typing_extensions import TypeAlias

_Address: TypeAlias = tuple[str, int] | tuple[str, int, int, int] | str
Socket: TypeAlias = socket
