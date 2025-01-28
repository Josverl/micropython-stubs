from collections import OrderedDict


d1 = OrderedDict()
d1["a"] = 1
d1["b"] = 2

d2 = OrderedDict({"a": 1, "b": 2})
d2["c"] = 3

# To make benefit of ordered keys, OrderedDict should be initialized
# from sequence of (key, value) pairs.
d3 = OrderedDict(
    [("z", 1), ("a", 2)]  # stubs-ignore:  linter in ["pyright"]
)  # TODO: This @overload#3  used to work before a custom stdlib was added



d3["w"] = 5
d3["b"] = 3
for k, v in d3.items():
    print(k, v)

# Argument of type "list[tuple[str, int]]"
# cannot be assigned to parameter "map" of type "Mapping[_KT@OrderedDict, _VT@OrderedDict]" in function "__init__"
# "list[tuple[str, int]]" is not assignable to "Mapping[_KT@OrderedDict, _VT@OrderedDict]" (reportArgumentType)
