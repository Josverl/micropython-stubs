# sys.implementation is a namedtuple, not a tuple
# https://github.com/Josverl/micropython-stubs/issues/708

# https://docs.micropython.org/en/latest/library/sys.html#sys.implementation
# name - string "micropython"
# version - tuple (major, minor, micro, releaselevel), e.g. (1, 22, 0, ‘’)
# _machine - string describing the underlying machine
# _mpy - supported mpy file-format version (optional attribute)
# _build - string that can help identify the configuration that MicroPython was built with

import sys
from typing import Any, Tuple, Literal

from typing_extensions import assert_type, get_type_hints

# TODO sys.implementation is not a tuple : https://github.com/Josverl/micropython-stubs/issues/708
# >>> repr(sys.implementation)
# "(name='micropython', version=(1, 28, 0, 'preview'), _machine='linux [GCC 12.5.0] version', _mpy=2822, _build='standard', _thread='unsafe')"

assert_type(sys.implementation.name, str)
assert_type(sys.implementation.version[0], int)
assert_type(sys.implementation.version[1], int)
assert_type(sys.implementation.version[2], int)
# assert_type(sys.implementation.version[3], Literal)
