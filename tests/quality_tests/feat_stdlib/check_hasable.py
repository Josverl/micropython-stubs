"""Validate that a type is hashable.
ref: https://github.com/Josverl/micropython-stubs/issues/723
"""

i = 0
d = {i: "a"}

type_text = "int"
if type_text in {"int", "float", "str", "bool", "tuple", "list", "dict"}:
    order = 1
