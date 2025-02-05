import sys
from typing import Dict, NamedTuple, Tuple

from typing_extensions import assert_type, get_type_hints

impl = sys.implementation


def is_tuple(imp: Tuple): ...


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
