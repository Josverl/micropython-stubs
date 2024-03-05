from micropython import const
from typing_extensions import assert_type

case1 = const(11)
assert_type(case1, int)

# Micropython >= 1.19.0
case2 = const(1.0)
assert_type(case2, float)

# case3 = const(True)
# assert_type(case3, bool)

case4 = const("foo")
assert_type(case4, str)

case5 = const(b"foo")
assert_type(case5, bytes)

case6 = const((1, 2, 3))
assert_type(case6, tuple)

case7 = const(1 + 2)
assert_type(case7, int)

case8 = const(1.0 + 2.0)
assert_type(case8, float)

# Should show error
# todo: micropython.const - how to test for incorrect assignments?
# case = const({"foo": "bar"})
# case = const(["foo", "bar"])
