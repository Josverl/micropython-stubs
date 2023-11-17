from typing_extensions import assert_type

import re
Substring ='.*Python'
String1 = "MicroPython"
m =re.match(Substring, String1)

assert m is not None
assert_type(m, re.Match[str])
