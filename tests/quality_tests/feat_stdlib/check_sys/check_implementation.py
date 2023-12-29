import sys
from typing import Dict, NamedTuple, Tuple

from typing_extensions import assert_type, get_type_hints

impl = sys.implementation


def is_tuple(imp: Tuple):
    ...


# indirect check if sys implementation has a base class of a tuple
# there must be a cleaner way to do this but I can't find it
is_tuple(impl) # type: ignore # TODO 


assert_type(impl, NamedTuple)  # type: ignore # TODO sys.implementation is not a tuple


# assert_type(sys.implementation.name, str)
# assert_type(sys.implementation.version, Tuple[int, int, int])
# assert_type(sys.implementation._machine, str)
# assert_type(sys.implementation._mpy, int)

# mpy = (
#             sys.implementation._mpy
#             if "_mpy" in dir(sys.implementation)
#             else sys.implementation.mpy
#             if "mpy" in dir(sys.implementation)
#             else ""
#         )

# TODO - improve sys.implementation in stubs
_ = """
file sys.pyi

implementation: _mpy_implementation

# from stdlib.sys import _version_info
class _mpy_implementation:
    name: str
    version: Tuple[int, int, int]
    _machine: str
    _mpy: int
    # Define __getattr__, as the documentation states:
    # > sys.implementation may contain additional attributes specific to the Python implementation.
    # > These non-standard attributes must start with an underscore, and are not described here.
    def __getattr__(self, name: str) -> Any: ...

"""
